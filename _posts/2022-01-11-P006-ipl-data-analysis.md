---
title:  "🗄️ Data Engineering | Analysing IPL Data From Day Zero"
layout: post
categories: [data-engineering, sql]
image: /assets/img/P006/cover.png
description: "SQL Problems based off ipl-data from 2008 to 2020."
customexcerpt: "Want to learn SQL? Want to make it Fun? This post includes SQL problems for ipl-dataset from 2008 to 2020 for all skill levels."
---
![Data](/assets/img/P006/cover.png)
Illustration Source: "Data" from [https://undraw.co](https://undraw.co/){:target="_blank"}

When I started learning SQL, it felt like the most easiest language out there. I had even falsely thought I had mastered it in a few days. Dear god, I was so wrong. More complex your questions are, more wide your dataset is, the more tricky your queries get.

Also, as a beginner it's really easy to know where to start but it's really hard to go ahead once you gain some level of understanding. Solving SQL problems requires you to think in a way which is quite different from solving other programming problems. 

This is not a Tutorial, but rather just a set of problems that should act as a bridge to more advanced topics of SQL. You should have some prior hands-on with SQL before you could continue solving the problems.

# What is IPL all about?

This post is entirely focused on analysis of IPL Dataset. If you are already an IPL fanatic, then just [skip](#house-rules) ahead. Otherwise [this](https://en.wikipedia.org/wiki/Indian_Premier_League){:target="_blank"} wikipedia page should be able to give you a basic understanding of the same.

And for those who would like to skip reading wiki, here's a tldr; for you *(this is a very quick intro and will be no way enough for you to understand the entire format properly, I would strongly suggest to do your part of study before going ahead)* -

The Indian Premier League (IPL) is a professional [Twenty20](https://www.youtube.com/watch?v=ktORZqRy-iM){:target="_blank"} [cricket](https://www.youtube.com/watch?v=g-beFHld19c){:target="_blank"} league, contested by eight to ten [teams based out of Indian cities](https://www.iplt20.com/teams/men){:target="_blank"}. It is usually held between March and May of every year. There have been fourteen seasons of the IPL tournament so far, from [2008 to 2021](https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_seasons_and_results){:target="_blank"}. 

In League Phase, each team plays in a [round-robin](https://en.wikipedia.org/wiki/Round-robin_tournament){:target="_blank"} format, with each team playing other team exactly twice, one at home ground and one away. At the conclusion of the league phase, the top four teams will qualify for the playoffs. 

In Playoff Phase, top two teams will play against each other in the first Qualifying match, with the winner going straight to the IPL final and the loser getting another chance to qualify for the IPL final by playing the second Qualifying match. Meanwhile, the third and fourth place teams from league phase play against each other in an eliminator match and the winner from that match will play the loser from the first Qualifying match. The winner of the second Qualifying match will move onto the final to play the winner of the first Qualifying match in the IPL Final match, where the winner will be crowned the Indian Premier League champions.

Here's a diagram, that visualizes the same - 

![IPL Format](/assets/img/P006/01.png)

Now, it's okay even if it's not completely clear yet. Just having a basic understanding should be more than enough. I will try to give you enough context as and when questions are established later on...

# House Rules

Before we get to dataset, here are some rules to follow along while reading this blog -

1. [https://github.com/gauthamchettiar/ipl-data-analysis](https://github.com/gauthamchettiar/ipl-data-analysis){:target="_blank"} - clone this repository and keep it with you. 
2. **Make sure to look at solutions only after you have written yours down.** 
3. Code provided is written in PostgreSQL, while you are free to work with your prefered flavor of SQL. I would suggest you to install [PostgreSQL](https://www.postgresql.org/download/){:target="_blank"} for comparing solutions.
4. Dataset is available as part of above repositoy at [data/](https://github.com/gauthamchettiar/ipl-data-analysis/tree/main/data){:target="_blank"} directory. Provided data is a cleaned version of dataset taken from [kaggle](https://www.kaggle.com/patrickb1912/ipl-complete-dataset-20082020){:target="_blank"}
5. You are free to look at the dataset and make sense of it on your own.
6. You will be able to setup your PostgresSQL with required tables by following instructions in above github readme.
7. Bonus questions are just as important as main question, try to solve both.
8. Look at Hints only if you are stuck (hover over grey-box for revealing them).
9. Each question may have multiple solutions, I will include any one of those working solution. As long as your solution matches "Expected Output" you are good to go!

# Unwinding the Dataset
There are 2 datasets available as part of this exercise,
1. **ipl_m_2008-2020.csv** : Contains records of all matches that were played from year 2008 to 2020.   
![ipm_m table](/assets/img/P006/02.png)

2. **ipl_byb_2008-2020.csv** : Contains a Ball-By-Ball record for each of the above matches. *We won't be using this table as a part of this exercise, so you are free to skip directly to problems.*
![ipm_byb table](/assets/img/P006/03.png)

# Let's get Started!


## Problem 1 : Get the number of seasons
IPL has been held every year since 2008. A Season is nothing but the year on which an edition of IPL was held. Going by this, there have been 13 seasons till 2020. 

List all the seasons in `ipm_m` table.

**Expected Output** (Column = 1, Row = 13) :
![P1 Output](/assets/img/P006/04.png){:width="120"}

{% include spoiler-hover.html head="Hint :" text="Look for a function to obtain year from `date` column."%}

Also, this `season` information is pretty useful. We will be using it frequently in upcoming problems.

Create a view that has all columns from `ipl_m` along with season information. Name this view as `v_ipl_m_with_season`.

**Bonus :** Count the total number of seasons.

**Expected Output** (Column = 1, Row = 1) :

![P1 Bonus Output](/assets/img/P006/05.png){:width="180"}

**Solution :** [/solutions/problem_1.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_1.sql){:target="_blank"}

## Problem 2 : Get all teams who participated for a given season
Teams have gone through several name changes and some teams didn't participate for certain seasons. Due to this, not all seasons have all the teams or there were some extra teams introduced midway. 

Define a variable called `season` initialize it with some year - say `2019`. List all teams that participated for that season from view `v_ipl_m_with_season`. 

**Expected Output** (For Season = 2019 : Column = 1, Row = 8) :

![P2 Output](/assets/img/P006/06.png){:width="200"}

{% include spoiler-hover.html head="Hint :" text="Filter by `season` and return DISTINCT on `team1` or `team2` column."%}

**Bonus :** Get number of teams who participated in each season.

**Expected Output** (Column = 2, Row = 13) :

![P2 Bonus Output](/assets/img/P006/07.png){:width="200"}

**Solution :** [/solutions/problem_2.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_2.sql){:target="_blank"}

## Problem 3 : Get the team who won the most number of times
Retrieve the teams and their respective `win_count` in entirety of IPL. Also order by `win_count` so that it's clear, who won the most!

**Expected Output** (Column = 2, Row = 15) :

![P3 Output](/assets/img/P006/08.png){:width="300"}

{% include spoiler-hover.html head="Hint :" text="As name suggests `winner` column contains winner for any particular match. Run GROUP BY and COUNT on this column."%}

**Bonus :** Also try to retrieve `win_count` by `team` per `season`. Output should have 3 columns (`team`, `season` and `win_count`). Every row should only contain `win_count` for that `team` for that `season`. 

**Expected Output** (Column = 3, Row = 111) : 

![P3 Bonus Output](/assets/img/P006/09.png){:width="300"}

**Solution :** [/solutions/problem_3.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_3.sql){:target="_blank"}

## Problem 4 : Get teams and maximum run margins for each team
Now, there are 2 columns which are of significance here - `result` and `result_margin`. Since we are looking for matches that has been won by defending *(winning team batted in 1st innings, put some runs on scoreboard and later in 2nd innings tried to defend that score)*, we should only focus on matches won by 'runs'.

**Expected Output** (Column = 2, Row = 14) :

![P4 Output](/assets/img/P006/10.png){:width="300"}

{% include spoiler-hover.html head="Hint :" text="Filter by `result` = 'runs' and GROUP BY `winner`, then retrieve the MAX of `result_margin`"%}

**Bonus :** Get teams and minimum wicket margins for matches that have been won by chasing (i.e: when winning team batted in 2nd innings and tried to chase the score set by other team). Also make sure that this wicket margin is equal to or lower than 3.

**Expected Output** (Column = 2, Row = 10) :

![P4 Bonus Output](/assets/img/P006/11.png){:width="300"}

**Solution :** [/solutions/problem_4.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_4.sql){:target="_blank"}

## Problem 5 : Get the count of bat/field toss_decision for every venue
Cricket is a game where pitch condition and weather is as important as players of a team. This would act as one of factor in deciding whether to bat/field first. So winning a toss and making bat/field decision thereafter is equally important.

Get the Venue, Bat/Field Decision and corresponding win count for each decision made.

**Expected Output** (Column = 3, Row = 63) :

![P5 Output](/assets/img/P006/12.png){:width="500"}

{% include spoiler-hover.html head="Hint :" text="GROUP BY `venue` & `toss_decision`, then retrieve the COUNT of `toss_decision`"%}

**Bonus :** Get an additional column of total number of wins for any particular decision.

**Expected Output** (Column = 4, Row = 63) :

![P5 Bonus Output](/assets/img/P006/13.png){:width="550"}

{% include spoiler-hover.html head="Hint :" text="Try to use CASE statement creatively. Column should include count of cases when `winner` is equal to `toss_winner`."%}

**Solution :** [/solutions/problem_5.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_5.sql){:target="_blank"}

## Problem 6 : Get total matches played by each team
While getting win_count for each team was easy, calculating total matches played by each team is slightly tricky. Each team has either played as team1 (home) or team2 (away). So you have to somehow combine data from 2 columns to aquire the required analytics.

**Expected Output** (Column = 2, Row = 14) :

![P6 Output](/assets/img/P006/14.png){:width="300"}

{% include spoiler-hover.html head="Hint :" text="You can use CTE (Common Table Expressions). Try to use UNION to combine two columns before running COUNT."%}

**Bonus :** Some matches go till last ball or with last few wickets remaining. In order to get count of only such matches. Filter above data based on few additional parameters, was the match won with 3 runs or less of a margin or was the match won with 2 or less wickets.

**Expected Output** (Column = 2, Row = 13) :

![P6 Bonus Output](/assets/img/P006/15.png){:width="300"}

{% include spoiler-hover.html head="Hint :" text="Have an additional CTE that will filter before running the UNION."%}

**Solution :** [/solutions/problem_6.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_6.sql){:target="_blank"}

## Problem 7 : Get the final match for a given season
Finals are one of the most watched match of the entire season regardless of teams playing. Try to retrieve the teams reaching the finals for any given season.

**Expected Output** (For Season = 2018 : Column = 2, Row = 1) :

![P7 Output](/assets/img/P006/16.png){:width="400"}

{% include spoiler-hover.html head="Hint :" text="This is relatively simple. Use ORDER BY and LIMIT to get the last match of a given season."%}

**Bonus :** Get final matches for each season, along with season column. 

**Expected Output** (Column = 3, Row = 13) :

![P7 Bonus Output](/assets/img/P006/17.png){:width="450"}

{% include spoiler-hover.html head="Hint :" text="This will require you to use window function ROW_NUMBER() with PARTITION BY and ORDER BY clauses."%}

**Solution :** [/solutions/problem_7.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_7.sql){:target="_blank"}

## Problem 8 : Get league and playoffs (semi-finals and finals) for a given season 
League matches are played and top 4 teams get to playoffs, where they play eliminator type matches to get to finals. Now, getting this information is slightly tricky considering the fact that format of this was different before 2010. Before 2010 there were only 2 playoffs being played, which changed and 4 playoff matches are being played since (this format is explained [above](#what-is-ipl-all-about)). 

Using this info, add an extra column `match_type` that tags each match as - 'League', 'Playoffs' or 'Finals' depending on that match type. You may save this as a view called `v_ipl_m_with_match_type`

**Expected Output** (Column = 20, Row = 816) :

![P8 Output](/assets/img/P006/18.png)

{% include spoiler-hover.html head="Hint :" text="This is similar to last bonus question. Just use CASE statement to check `season` and `row_number` and categorize accordingly."%}

**Bonus :**  Get number of times each team has reached playoffs as `playoffs_played`, finals as `finals_played` and actually gone ahead and won finals as `finals_won`.

**Expected Output** (Column = 4, Row = 14) :

![P8 Bonus Output](/assets/img/P006/19.png){:width="500"}

{% include spoiler-hover.html head="Hint : " text="Solution is very similar to problem 6. Just use CASE along with that solution for solving this one."%}

**Solution :** [/solutions/problem_8.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_8.sql){:target="_blank"}

## Problem 9 : Get total matches played, matches won and win percentage per season
In order to find the most consistent team of IPL. It is not enough to find who won the most number of seasons. Instead you will require a metric called `win_percentage`. Which is calculated as `matches_played`/`matches_won`*100. Instead of finding overall metric, try to group the same as per season.

**Expected Output** (Column = 5, Row = 108) :

![P9 Output](/assets/img/P006/20.png){:width="500"}

{% include spoiler-hover.html head="Hint :" text="This is an extension to 'Problem 6 - Bonus' Problem. Solution should be very similar to that one."%}

**Bonus :** Above data fetched is very difficult to analyse. It would have been much better if season were used as column names instead. Write a query that would display just `matches_won` for each team over seasons. 

Looking at below output should make it clear. 

**Expected Output** (Column = 14, Row = 14) :

![P9 Bonus Output](/assets/img/P006/21.png)

{% include spoiler-hover.html head="Hint : " text="This is called as 'pivoting' a table. Try to search for this term and you will be able to find a solution. You will be using a lot of CASE statements."%}

As a preparation for final question, create a VIEW `v_aggregated_ipl_m` which will include following columns, `matches_played`, `matches_won`, `playoffs_played`, `finals_played`, `finals_won` aggregated over `team` and `season`. 

You must just have to extend the solution of "Problem 8 - Bonus" question. 

**Expected View** (Column = 7, Row = 108) :

![P9 Preparation](/assets/img/P006/22.png)

**Solution :** [/solutions/problem_9.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_9.sql){:target="_blank"}

## Problem 10 : Get a wide column view of win_percentage of teams over season
Similar to getting `matches_won` in above bonus question, try to list `win_percentage`. You can use the above created VIEW `v_aggregated_ipl_m` for it.

**Expected Output** (Column = 14, Row = 14) :

![P9 Output](/assets/img/P006/23.png)

{% include spoiler-hover.html head="Hint :" text="Again use of CASE will be required as previous bonus problem."%}

**Bonus :** Real improvement/detorioration in performance can only be calculated if it is compared with last season's performance. We can consider `win_percentage` as a performance factor for the same. 

Try to retrieve the difference between a season's `win_percentage` figure with last season's figure. 

*e.g*: In below table for row value 'Chennai Super Kings' and year '2009' value is 0.89 which is calculated as, win_percentage(2009) - win_percentage(2008) -> (57.14 - 56.25 = 0.89)

**Expected Output** (Column = 14, Row = 14) :

![P9 Bonus Output](/assets/img/P006/24.png)

{% include spoiler-hover.html head="Hint : " text="Use a window function called LAG and get the difference."%}

**Bonus x2 :** Another performance measurement would be comparing each year's performance with each team's overall average performance.

**Expected Output** (Column = 14, Row = 14) :

![P9 Bonus Output](/assets/img/P006/25.png)

{% include spoiler-hover.html head="Hint : " text="Use a window function called AVG and get the difference."%}

**Solution :** [/solutions/problem_10.sql](https://github.com/gauthamchettiar/ipl-data-analysis/blob/main/solutions/problem_10.sql){:target="_blank"}

&nbsp;

Now that concludes the first set of problems. This was mostly focused on `ipl_m` dataset. In second part, we would focus on a combination of both datasets, so expect more JOINS!

[Hit me up](/about) with any queries or improved solutions to any of the above problems. I will make sure to resolve as many of your queries as possible.

Hope I was able to give you a challenging day! 