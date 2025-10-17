---
title:  "🦆 Confessing My Love for DuckDB"
date: 2023-07-24
draft: false
tags: ["Code"]
---

Recently, I had to do a transformation which involved converting a json struct into individual rows. While on face of it this might seem very simple, I quickly realized this was not one of those quick rodeos. 

A sample snippet of the dataset I have been trying to transform -
{{< wide-table >}}
| product_code | name   | price                                                                                  | quantity                        |
|--------------|--------|----------------------------------------------------------------------------------------|---------------------------------|
| 100          | onion  | {"chennai":{"cp":23,"sp":28},"mumbai":{"cp":25,"sp":28},"bangalore":{"cp":27,"sp":30}} | {"min":850,"max":980,"qty":"g"} |
| 101          | potato | {"chennai":{"cp":19,"sp":23},"bangalore":{"cp":21,"sp":25}} | {"min":1,"max":5, "qty":"kg"}   |
| 102          | tomato | {"chennai":{"cp":75,"sp":79},"mumbai":{"cp":70,"sp":75}} | {"min":400,"max":560,"qty":"g"} |
{{< /wide-table >}}  
If you want to follow along with me, here's a json equivalent for you to download - <a href="/code/20230724-confessing-my-love-for-duckdb/products.json" target="blank">products.json</a>

For easier data analysis, I wanted to transform above table in below flattened and de-normalized form,

{{< wide-table >}}
| product_code | name   | city      | cp | sp | min | max | qty |
|--------------|--------|-----------|----|----|-----|-----|-----|
| 100          | onion  | chennai   | 23 | 28 | 850 | 980 | g   |
| 100          | onion  | mumbai    | 25 | 28 | 850 | 980 | g   |
| 100          | onion  | bangalore | 27 | 30 | 850 | 980 | g   |
| 101          | potato | chennai   | 19 | 23 | 1   | 5   | kg  |
| 101          | potato | bangalore | 21 | 25 | 1   | 5   | kg  |
| 102          | tomato | chennai   | 75 | 79 | 400 | 560 | g   |
| 102          | tomato | mumbai    | 70 | 75 | 400 | 560 | g   |
{{< /wide-table >}}

Okay, if you are someone who is familiar with such data wrangling, you might have already come up with a solution in your mind. Your solution might involve using tools built for this like pandas, snowflake, spark, or even ones not intended for this like postgres, sqlite or if you are feeling adventurous you might even brute force it using a programming language. 

Any approach is fine as long as it fits your use case and does not eat up resources like a hungry hippo. 

For me I choose **Pandas**, since I already had done some amount of transformation to get here using python and pandas was just easier to integrate with it. 

*Oh, boy! I was in for a wild trip.*


## Import Pandas

Just some disclosure, I don't code avidly in pandas. I use it occasionally for such data wrangling stuff. So, as it is for a lot of data people out there, Pandas is not like a second nature for me. More so, some of its concepts are still alien to me. So do keep that in mind, before moving ahead.

My intuition did say that it would be much simpler to flatten quantity column, and that was the case. All I had to do was -

```python
import pandas as pd

df = pd.read_json("products.json")

pd.concat(
    [
        df,
        pd.json_normalize(df["quantity"]),
    ],
    axis=1,
)
```

Isn't that short and concise? *Yes*. Isn't that intuitive? *Maybe*.

It took me some time to understand that I had to pass `axis=1` for adding new Dataframe columns to original Dataframe (horizontally). As by default `concat` would concatenate 2 dataframes by index (vertically).

Here's one of my first problem with Pandas, why have same method do multiple things? Why not let `concat` just do the column concatenation and `append` do the row concatenation? Why not have a set operation available to be more simplistic for row append cases? 

This might seem like a nitpick, but consider beginners who have to maintain some production code written in Pandas. From above snippet, `axis=1` is the only clue I have to know that I am doing a column concatenation and not a row concatenation, which is easy to miss.

Maybe my scenario is a bit too simple for leveraging Pandas' flexibility? To test this, thankfully, I do have one more column I had to flatten - `price`.

```json
{
    "chennai":{
        "cp":23,
        "sp":28
    },
    "mumbai":{
        "cp":25,
        "sp":28
    },
    "bangalore":{
        "cp":27,
        "sp":30
    }
}
```

I had 2 things to do here - 
1. Create a Dataframe with just this column flattened and 
2. Merge this new Dataframe with original Dataframe.

Soon, I got a solution - 

```python
flat_json = pd.DataFrame(
    [
        (id, city, price["cp"], price["sp"])
        for id, v in zip(df["product_code"], df["price"].to_list())
        for city, price in v.items()
    ],
    columns=["product_code", "city", "cp", "sp"],
)

df = flat_json.merge(df, on="product_code", how="left")
```

This is what quick googling got me to. I am sure, there might be other better ways to do it which I am not aware of, but this confusing mess got me to what I wanted. So... I am not complaining. 

This is another thing with Pandas, the tool set is so diverse that no one exactly knows if what they are doing is the right way to do it. Pandas is a tool to get things done fast, it's only later when data grows that this approach falls apart. 

Now look at above snippet, let me ask the question again - Isn't that short and concise? *Maybe*. Isn't that intuitive? *Not at all!*.

Even after I wrote it I was not sure how this exactly works. And that's a bad sign for maintainability. Adding comments might help, but it can only get you to a certain level of readability, in the end if your code is a bad no level of commenting can help you.

## Enter DuckDB

Similar to pandas, I have previously used [duckdb](https://duckdb.org/) for data wrangling and analysis. For those uninitiated, it's an analytical counterpart of SQLite (not affiliated with it). 

One thing that really sold me the idea of using DuckDB was of course that all queries are in SQL and it is blazing-ly fast. In some instances I have seen it process sufficiently larger dataset faster than spark on databricks [^*](#footnotes). 

Added to this is the learning curve, all you need to know is a good understanding of SQL, some data analytics dialect and casual browsing through DuckDB documentation. Pretty much making a SQL person's learning curve flat. 

Okay now getting to how actual query looks like for flattening `price` -

```sql
SELECT * EXCLUDE price,
    price.*
from (
    UNPIVOT (
        SELECT product_code,
            price.*
        FROM read_json_auto("products.json")
    ) ON COLUMNS(* EXCLUDE (product_code)) INTO NAME city VALUE price
)
```

I will not lie, to understand you might need to know some of DuckDB's features. But even without any, you should be able to make something out of it. Still, here's quickly how it works -

`EXCLUDE` can be used if you want to select everything except some columns.  
`price.*` in sub-query will automatically flatten each individual keys into new column, with value as entry.  
{{< wide-table >}}
| product_code | Chennai           | Mumbai            | Bangalore         |
|--------------|-------------------|-------------------|-------------------|
| 100          | {"cp":23,"sp":28} | {"cp":25,"sp":28} | {"cp":27,"sp":30} |
| 101          | {"cp":19,"sp":23} |                   | {"cp":21,"sp":25} |
| 102          | {"cp":75,"sp":79} | {"cp":70,"sp":75} |                   |
{{< /wide-table >}}  
`UNPIVOT` will get those columns into row entries  
{{< wide-table >}}
| product_code | city      | price             |
|--------------|-----------|-------------------|
| 100          | Chennai   | {"cp":23,"sp":28} |
| 101          | Chennai   | {"cp":19,"sp":23} |
| 102          | Chennai   | {"cp":75,"sp":79} |
| 100          | Mumbai    | {"cp":25,"sp":28} |
| 101          | Mumbai    |                   |
| 102          | Mumbai    | {"cp":70,"sp":75} |
| 100          | Bangalore | {"cp":27,"sp":30} |
| 101          | Bangalore | {"cp":21,"sp":25} |
| 102          | Bangalore |                   |
{{< /wide-table >}}


Ain't that a beauty. Now once, you learn this, it's very difficult to forget. You can come back to this code a year later, and at least some part of it might still make sense. Unlike the spaghetti of a code from Pandas. 

*You can find complete code for both the examples in footnotes [^**](#footnotes).*

I do realize that working in SQL and working in procedural language require completely different set of brain cells at work. And I very much acknowledge it, that's why I did not name it Pandas vs DuckDB. This essay is more like my love letter to DuckDB and in no way dismisses Pandas capability, which lies in flexibility.

Whether you may be a 🦆 person or a 🐼 person, feel free to get in [touch](/contact) with me. Would ove to hear your thoughts!

&nbsp;

### ^FootNotes
- [*] : This is quite a loose comparison. Even though dataset was same, they were both running on different machines with almost similar configuration. So it's not an apples to apples comparison, more so like apple to pear. 
- [**] : <a href="/code/20230724-confessing-my-love-for-duckdb/flatten.py" target="_blank">Pandas Code</a> & <a href="/code/20230724-confessing-my-love-for-duckdb/flatten.sql" target="_blank">Duckdb SQL</a>