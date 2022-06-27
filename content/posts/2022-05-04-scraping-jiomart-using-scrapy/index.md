---
title:  "⛏️ Web Scraping | Scraping Jiomart For Daily Product Prices"
slug: "scraping-jiomart-using-scrapy"
date: 2022-05-04
lastmod: 2022-05-04
draft: false
cover: images/cover.svg
tags: [python, web-scraping]
categories: ["Projects"]
---

<br>

---

# tldr; incase you only need the tool
This article is more of an insight into how I figured out a way to scrape data off {{<newtabref title="jiomart.com" href="https://jiomart.com">}}. If you are more interested in using the tool - Setup instructions and detailed documentation is available here - {{<newtabref title="Setup Instructions" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers" >}} & {{<newtabref title="Jiomart Configuration" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/tree/main/jiomart" >}}

---

For those who have never heard of Jiomart, it is an Indian e-commerce website by Reliance. As of now, Jiomart provides free delivery without any minimum purchase limit. Believe me, I have ordered for groceries as low as INR 20 and got it delivered.

![free delivery, no minimum order promotion image](images/01.png)

Being one of cheapest store to buy vegetables online it had become our goto store during pandemic. In fact, the habit has stuck with us till now - kudos to company! 

Since we still buy so frequently from the store, I thought it would be useful for us to have metrics that answered a few things - What is the cheapest product today? How the price of a particular product changed overtime? Is price increasing? - then it's hoarding time! 

While such questions may seem too much for grocery products like rice or wheat, whose price doesn't change that frequently. For vegetables and fruits, these metrics can come in quite handy.

But before analysis, you need data. And jiomart won't provide me their daily data, even if I ask nicely. So, the only way to quench my curiosity was to scrape the data off their website. While I have performed analytics on a small set of data, this article focuses on the scraping part rather than on the analytical part. 

Web scraping can usually be divided into 3 major steps,
1. [Understanding the structure](#understanding-the-structure) and [Recognizing scrape-able data](#recognizing-scrape-able-data).
2. [Testing your theory](#testing-your-theory) and [Writing script to actually scrape data](#writing-script-to-scrape-data).
3. [Cleaning the scraped data](#cleaning-the-scraped-data).


# Understanding the structure
My main motivation was to scrape product prices, so pages (called subdirectories) that list products seemed like a good starting point. And pages that directly have a list of products are category pages,
- `/c/groceries/fruits-vegetables/219`
- `/c/groceries/snacks-branded-foods/10`
- `/c/groceries/home-kitchen/kitchenware/1710` 
- &nbsp;and so on...

![sample tag image](images/02.png)

I would like to assume that these links will not change in future, and directly scrape right off them, but that's not always the case. So, I thought, it would be a good strategy to get these very category links before scraping for product. 

I needed a page that listed all categories, thankfully Jiomart did have one - `/all-category`,

![all-category page screenshot](images/03.png)

Clicking on each category did take me exactly to the respective category pages, that was quite easy!

Apart from category pages, there are other URLs that list products like - 
- `/all-topdeals`
- `/c/groceries/bestdeals/hotspot/706`
- `/c/bestdeals/summer-may-2022-main-banner/5871`

![top-deals page](images/04.png)

Some promotional links are short lived, some are frequently added and removed, thus scraping them daily had no real purpose other than keeping an archive of products that were in a particular promotional offer. 

Final implementation does have provision to scrape both category and non-category pages.

# Recognizing Scrape-able Data
Before we start we need to check the data that we can actually acquire. Our original motivation was to compare the prices of products, so we definitely need Product Name and Product Price, we also need one more metric that is Product Quantity. Reason? If listed quantity changes in future there cannot be a 1 to 1 comparison done purely based on price, you might have to somehow normalize it w.r.t quantity before comparison. 

So we need 3 metrics,
- Product name
- Product Price
- Product Quantity

Product listing page does have list of products along with price... but there is'nt a separate field for Quantity. 

{{<img-resize src="images/05.png" alt="watermelon product listing" height="300">}}

What if you open individual product page? Does it have a separate Quantity value?

{{<img-resize src="images/06.png" alt="watermelon product page">}}

Yes, it does have a separate "Net Quantity" entry. But, same quantity information is also available in the name of product in previous product listing page.

I had a decision to make here - If I can extract quantity and product name directly from listing page's name - "Watermelon Kiran Big 1 pc (Approx 2800 g - 4000 g)", is it worth parsing one more hierarchy of page just to get a more accurate bit of information?

While it isn't hard to do crawl the product pages as well, I didn't think it was right to bombard the website with even more hits. So I settled, with only getting the name and quantity. Cleaning this data to then acquire Quantity and Name is a problem than can be handled later.

# Testing your theory
Now since I had decided what to scrape, I did a quick {{<newtabref title="Inspect" href="https://developer.chrome.com/docs/devtools/open/">}} to get an idea of website's HTML elements. 

I got to know, each product item was defined in below hierarchy -
```html
<div class="cat-item viewed">
    ...
    <span class="clsgetname">
        Watermelon Kiran Big 1 pc (Approx 2800 g - 4000 g)
    </span>
    <span id="final_price"> 
        ₹ 49.00
    </span>
    ...
</div>
```

Then I tested the water with a simple {{<newtabref title="requests" href="https://docs.python-requests.org/en/latest/#">}} + {{<newtabref title="beautifulsoup" href="https://beautiful-soup-4.readthedocs.io/en/latest/">}} combo -


```python
import requests
from bs4 import BeautifulSoup

# sending requests to a product listing page
req = requests.get("https://www.jiomart.com/c/groceries/fruits-vegetables/219")

soup = BeautifulSoup(req.content, features="html.parser")

# Get Product Name, Measure and Quantity from RawName of the product
for scr in soup('span', {'class': 'clsgetname'}):
    print(scr.contents[0])
# Get price of the product
for scr in soup('span', {'id': 'final_price'}):
    print(scr.contents[0])

```

Results were as expected -
```
Watermelon Kiran Big 1 pc (Approx 2800 g - 4000 g)
Onion 1 kg
Sweet Corn 1 pc (Approx 250 g - 450 g)
Potato per kg
Onion 5 kg (Pack)
...

₹ 49.00
₹ 19.00
₹ 16.00
₹ 28.00
₹ 90.00
...
```

Now what about getting category links from`/all-category`?

Inspection observation -
```html
...
<div class="cat_details">
    <a href="https://www.jiomart.com/c/groceries/fruits-vegetables/219">
        <span class="cat_name">
            Fruits & Vegetables
        </span>
    </a>
</div>
...
```

Test code -
```python
import requests
from bs4 import BeautifulSoup

# sending requests to all-category URL
req = requests.get("https://www.jiomart.com/all-category")

soup = BeautifulSoup(req.content, features="html.parser")

# fetch the divisions having both category link and name
for div in soup.findAll('div',attrs={'class':'cat_details'}):
    link = div.find('a')
    if link is not None:
        print(link.get("href"))
        print(link.find("span").text)
```

Result -
```
https://www.jiomart.com/c/groceries/fruits-vegetables/219
Fruits & Vegetables
https://www.jiomart.com/c/groceries/premium-fruits/3107
Premium Fruits
https://www.jiomart.com/c/groceries/dairy-bakery/61
Dairy & Bakery
https://www.jiomart.com/c/groceries/staples/13
Staples
...
```

There was one last bit of trial I had to do before I could start implementing a full-fledged crawler. Jiomart is available pan-india, but not all products are available everywhere also price changes as per region. So, to get region specific results I had to somehow provide PINCODE in my request.

On their website I could do it by setting my pincode here,
![pincode setting](images/07.png)

But mimicking the same using requests was quite a task. So, after digging through the html, I found an interesting snippet of code related to pincode,
```js
var login_pincode = localStorage.getItem('nms_mgo_pincode');
```
I figured maybe setting a cookie item `nms_mgo_pincode` would make it believe I was requesting from that particular region. 

So tried adding it in previous queries,
```python
req = requests.get(
    "https://www.jiomart.com/c/groceries/fruits-vegetables/219",
    cookies = { "nms_go_pincode": "400007" })
```

And somehow that worked! Changing this cookie gave me region specific results :)

# Writing Script to Scrape Data
It's possible to write a custom script using just requests and beautifulsoup, But in long run it would get increasingly difficult to maintain it. So I chose to use a dedicated framework - {{<newtabref title="scrapy" href="https://scrapy.org/">}}.

What's the benefit of using scrapy you ask?
- It allows to add multiple destinations for your scraped data - {{<newtabref title="feeds" href="https://docs.scrapy.org/en/latest/topics/feed-exports.html">}}
- Output file format chan be changes with a simple change of setting - {{<newtabref title="feeds" href="https://docs.scrapy.org/en/latest/topics/feed-exports.html">}}
- It allows you to extend the functionality easily due to it's modularity - just add a new {{<newtabref title="spider" href="https://docs.scrapy.org/en/latest/topics/spiders.html">}}}. 



Scrapy web-scraping code is available in repo - {{<newtabref title="github.com/gauthamchettiar/scrapy-mini-crawlers" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers" >}}. 
Jiomart's scraper is available in subfolder - {{<newtabref title="jiomart/" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/tree/main/jiomart">}}

Most important piece of scrapy code is {{<newtabref title="jiomart/settings.py" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/blob/main/jiomart/settings.py">}}. This includes all the settings required to change the behavior of crawler.

There are 3 spiders (as per scrapy these are classes that crawls websites and has logic to fetch data from the fetched html) written for fetching 3 different types of urls,
1. jio-by-category : Refer {{<newtabref title="jiomart/spiders/category_spider.py" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/blob/main/jiomart/spiders/category_spider.py">}}
    ```python
    # related setting @ jiomart/settings.py
    URL_CATEGORY = "https://www.jiomart.com/all-category"
    CATEGORIES_TO_PARSE = ["Fruits & Vegetables"]
    ```
    
2. jio-by-top-deals : Refer {{<newtabref title="jiomart/spiders/top_deals_spider.py" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/blob/main/jiomart/spiders/top_deals_spider.py">}}
    ```python
    # related setting @ jiomart/settings.py
    URL_TOP_DEALS = "https://www.jiomart.com/all-topdeals"
    ```
3. jio-by-url : Refer {{<newtabref title="jiomart/spiders/url_spider.py" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/blob/main/jiomart/spiders/url_spider.py">}}
    ```python
    # related setting @ jiomart/settings.py
    URLS = {
    "Hotspot Deals" : "https://www.jiomart.com/c/groceries/bestdeals/hotspot/706",
    "Hot Food Fest" : "https://www.jiomart.com/c/groceries/bestdeals/hot-food-fest-2022/4515"
    }
    ```

What's the benefit of defining a spider? Well you can simply run a scraping job by running below command -
```bash
# set project (one time thing)
export SCRAPY_PROJECT=jiomart
# run desired spider
scrapy crawl jio-by-category
```

The crawled data is available in a json in below format -
```json
[
    {
        "name": "Watermelon Kiran 1 pc (Approx 2300 g - 3000 g)", 
        "price": 49.0, 
        "category": "Fruits & Vegetables"
    },
    { 
        "name": "Tomato 1 kg", 
        "price": 35.0, 
        "category": "Fruits & Vegetables"
    }
]
```

More details on usage is available in the github repo {{<newtabref title="github.com/gauthamchettiar/scrapy-mini-crawlers" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers" >}} itself.

# Cleaning the Scraped Data
One of the paramount task in this project was that of cleaning the acquired data. Primarily due to inconsistency and diversity in listed products -

1. Difference in Quantity Measure (Piece & Kg) for same Product  
    {{<img-inline src="images/08.png" alt="muskmelon-1pc" width="225" height="275">}} {{<img-inline src="images/09.png" alt="muskmelon-1kg" width="225"  height="275">}}  
2. Difference in Quantity (1 Kg & 5 Kg) for same Product  
    {{<img-inline src="images/10.png" alt="onion-1kg" width="225"  height="275">}} {{<img-inline src="images/11.png" alt="onion-5kg" width="225"  height="275">}}  
3. Different Varieties (Robusta & Yellaki) of Same Product  
    {{<img-inline src="images/12.png" alt="onion-1kg" width="225" height="275">}} {{<img-inline src="images/13.png" alt="onion-5kg" width="225"  height="275">}}

My end goal, after cleaning, was to achieve something like this -
```json
[
    {
        "name": "Watermelon Kiran Big 1 pc (Approx 2800 g - 4000 g)", 
        "price": 45.0, 
        "category": "Fruits & Vegetables", 
        "quantity": 1.0, 
        "type": "piece",
        "group_name": "watermelon kiran"
    },
    { 
        "name": "Tomato 1 kg", 
        "price": 35.0, 
        "category": "Fruits & Vegetables",
        "quantity": 1.0,
        "type": "kilogram",
        "group_name": "tomato"
    }
]
```

Where,  
1. "type" can be one of 4 - "piece", "bunch", "kilogram" & "gram"
2. "group_name" is a generic name given to a type of product "Water Melon Kiran", "Watermelon Kiran Big", "Watermelon Kiran Medium" everything will fall under a general "watermelon kiran" umbrella.

As to how I achieved it is by defining a set of rules that has a mix of string matching and regex defined for fetching name and quantity. 

Code for running cleaning job is available here - {{<newtabref title="jiomart/cleaners/" href="https://github.com/gauthamchettiar/scrapy-mini-crawlers/tree/main/jiomart/cleaners">}}. You can run a batch cleaning job just by running the python script `extract_quantity.py`.

Rules at `cleaning_rules.json` govern how name and quantity will be fetched from a product.

A snippet from file,
```json
{
    "fetch_quantity_rules": {
        "musk melon": [
            {
                "type": "kilogram",
                "regex": "([0-9.]+) kg"
            },
            {
                "type": "piece",
                "regex": "([0-9.]+) pc"
            }
        ],
        "papaya": [
            {
                "type": "piece",
                "regex": "each",
                "quantity": 1
            },
            {
                "type": "kilogram",
                "regex": "([0-9.]+)kg"
            }
        ]
    },
    "exclude_keywords": [
        "trikaya",
        "trueganic",
        "microgreen",
        "microgreens"
    ]
}
```
Here, 
1. Each key - "musk melon", "papaya" is your product's "group_name".
2. "regex" fetches the numeric quantity from the name
3. "type" is the corresponding Quantity Measure.
4. "quantity" is the field when quantity cannot be fetched via regex (i.e: quantity is not numeric but mentioned as "per", "each", etc.).
5. "exclude_keywords" define the products that should be filtered out from cleaned file.

So running `extract_quantity.py` will do following things -
1. Checks for any uncleaned file from `scraped_data/jiomart`. 
2. Uses rules defined in `cleaning_rules.json` to -  
    a. filter out unwanted items and   
    b. extract quantity and type from name
3. Stores cleaned files at `cleaned_data/jiomart`.
4. Stores Error Data at `error_data/jiomart`, this data includes  
    a. items for which there is no rules present ({file_name}-new_entry.json)  
    b. items for which riles were present but regex did not match ({file_name}-no_regex_rule.json)  

<br>

That concludes this article, feel free to check the script out yourself. I would love to hear your feedback. 

Do be mindful about it's usage though, don't overuse it. Crawl responsibly. There is a possibility that your IP may get blacklisted otherwise. 

I do hope that script finds it's use outside my computer!