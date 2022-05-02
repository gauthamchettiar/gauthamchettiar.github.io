---
title:  "🖐️ Listed | 5 Features that Define Python"
slug: "features-that-define-python"
date: 2021-06-04
lastmod: 2022-05-01
draft: true
cover: images/cover.svg
tags: [python, python-listed-series]
categories: ["Tutorials"]
---
<br>  
Python has topped as one of the most sought-after programming language in recent times. Mostly due to its simplicity and a feature-set that makes coding a breeze. This has in turn lead to several tutorials for pythons focusing more on beginner-level topics, but when you look for places to get out of that initial shell, the material is scarce. I am writing this article to act as a bridge in such a case.

This article focuses on really simple but useful features of Python. You can use below [Index](#index) as a reference and skip to topics that are relevant to you. Each item is complete in itself and does not require reading any of the prior items, unless explicitly mentioned.

<br>

# Index
1. [Generic \| Interpolated f-strings](#generic--interpolated-f-strings)
2. [Generic \| Multiple Assignment Unpacking](#generic--multiple-assignment-unpacking)
3. [List \| Slicing and Striding](#list--slicing-and-striding)
4. [List \| Negative Indexing](#list--negative-indexing)
5. [List \| List Comprehension](#list--list-comprehension) 

[Next Part](/features-that-define-python-p2)

<br>

## Generic \| Interpolated f-strings
There are often times when you need to print/write certain variables to console, file or web. This generally includes formatting variables in-between strings - "e.g: Last Element in list `[1,2,3,4,5]` is `5`". There are several ways to do this - using {{< newtabref  href="https://realpython.com/python-string-split-concatenate-join/" title="string concatenation">}}, {{< newtabref  href="https://www.geeksforgeeks.org/python-format-function/" title="str.format() function">}} and {{< newtabref  href="https://www.geeksforgeeks.org/string-formatting-in-python-using/" title="% operator">}}. But most of the above listed approaches are extremely verbose or hard to maintain. In order to solve those problems, f-strings were introduced in python 3.6. 

**Only supported in Python Version >= 3.6**, and is probably not the best way to go by if you are not sure about run-time python version of your deployment.

### Code Example:
Suppose you want to print *"First Element in list [1,2,3,4,5] is 1"*, you can do one of the following things,

Let's consider below list,
```python
arr = [1,2,3,4,5]
```

Using % Operator -

```python
print("First Element in List %s is %s" % (arr, arr[0]))
```

Using str.format() -

```python
print('First Element in List {} is {}'.format(arr, arr[0]))
# OR
print('First Element in List {0} is {1}'.format(arr, arr[0]))
# OR
print('First Element in List {arr} is {first_element}'.format(arr=arr, first_element=arr[0]))
```

Using f-strings - 

```python
arr = [1,2,3,4,5]
print(f'First Element in List {arr} is {arr[0]}')
# Now that's the cleanest of the lot, isn't it?
```

String formatting is not limited to just introducing a variable in-between string, you can do a variety of fancy things while formating. Here is a {{< newtabref  href="https://gist.github.com/gauthamchettiar/fa3f32758616611bfecf941809fd598b" title="Python String Formatting Mini Language Quick Reference">}} I made, in case you are curious.

### Reference Material:
- {{< newtabref  href="https://realpython.com/python-f-strings/" title="https://realpython.com/python-f-strings/">}}
- {{< newtabref  href="https://realpython.com/python-string-formatting/" title="https://realpython.com/python-string-formatting/">}}
- {{< newtabref  href="https://www.python.org/dev/peps/pep-0498/" title="https://www.python.org/dev/peps/pep-0498/">}}

<br>

## Generic \| Multiple Assignment Unpacking
It's possible to return multiple values from a function using a special behavior of Python. Now, Python does not exactly allow multiple return values, but it can be done with a mix of returning a tuple and assigning it to multiple variables using multiple assignment unpacking feature. 

How does it exactly work though?
### Code Example:
In Python, Multiple variables can be assigned on a single line as,

```python
a,b = 1,2
```

Now if value on right is a `Tuple ()` or `List []` all values will be unpacked and individually assigned to each variable on left, this is called "Multiple Assignment Unpacking"

```python
a,b = [1,2]     # a=1 and b=2
a,b,c = [1,2,3] # a=1, b=2 and c=3
```

In case any value needs to be ignored `'_'` can be used

```python
_,b = [3,5] # b=5 and 3 will be ignored

a,_ = [4,6] # a=4 and 6 will be ignored

a,_,c = [4,6,8] # a=4, c=8 and 6 will be ignored
```

Suppose, you know a function can fail, but don't want to handle the error, instead return a default value on failure. Let's take an exmple of *division by zero error*, let's say you want to *return 0* on failure and also know if an error has occured or not, you can return a `Tuple ()` as `(return_value, error)`.

```python
def get_division(a, b):
    try:
        a / b
    except Exception as e:
        return (0, e)
    return (a / b, None)

div, error = get_division(1,2)
div, error = get_division(1,0)
```

In examples we have seen so far, number of variables in left and values on right have been equal. 

Now what if number of variables on left and right differ?

```python
a,b = [1,2,3,4] # THIS WILL THROW AN ERROR!
#   -> ValueError: too many values to unpack (expected 2)

# But python does have one cool trick up it's sleeve,
a,*b = [1,2,3,4]   # a=1 and b=[2,3,4]

*a,b = [1,2,3,4]   # a=[1,2,3] and b=4

a,*b,c = [1,2,3,4] # a=1, b=[2,3] and c=4
```

### Reference Material:
- {{< newtabref  href="https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/" title="https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/">}}
- {{< newtabref  href="https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment" title="https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment">}}
- {{< newtabref  href="https://www.python.org/dev/peps/pep-3132/" title="https://www.python.org/dev/peps/pep-3132/">}}

<br>

## List \| Slicing and Striding
In Python, strings are just like a list of characters. Which makes it possible to use list operations on strings as well. Slicing and Striding are one of the most useful feature of list, that can be used to extract certain portions of list.
### Code Example:
Let's take an example of below list,

```python
a = [1,2,3,4,5]
#   [0,1,2,3,4]   <- INDEX
```

Now when you say lists can be slices, it literally means that -

```python
a[1:3] # Returns [2,3]
    # Starts at index=1(inclusive), 
    # ends at index=3(exclusive)
a[:3] # Returns [1,2,3]
    # leaving start_index blank,
    # starts from first value (index 0)
a[2:] # Returns [3,4,5]
    # leaving end_index blank,
    # ends at the last value
```

You can also give a step value that is useful to step over certain values -

```python
a[1:4:2] # Returns [2,4]
# Starts at index=1 (i.e:2), 
# ends at index=4(exclusive) (i.e:4),
# steps over index=3(i.e:3)
```

This could be very confusing for first timers, here's some more example to make it easier to understand

```python
a[::2] # Returns [1,3,5], step=2 means skip every 1 value
a[::3] # Returns [1,4], step=3 means skip every 2 values
```

Slicing is especially useful if you want to extract certain characters from start or end of string. Let's say you need to return first 4 digits or last 4 digits of creditcard -

```python
credit_card = "4000056655665556"
credit_card[:4] # Returns '4000'
credit_card[12:] # Returns '5556'
# Creditcard number length can differ based on length,
# -> So this is not really a robust solution
```

#### ✍ Things to remember,
1. For slicing - `arr[start_index:end_index]`, where *start_index* is **inclusive** and *end_index* is **exclusive**.
2. For striding - `arr[start_index:end_index:step]`, where *step - 1* elements will be **skipped in-between**.  

### Reference Material:
- {{< newtabref  href="https://realpython.com/lessons/string-slicing/" title="https://realpython.com/lessons/string-slicing/">}}
- {{< newtabref  href="https://www.datacamp.com/community/tutorials/python-string-tutorial" title="https://www.datacamp.com/community/tutorials/python-string-tutorial">}}

<br>

## List \| Negative Indexing
Along with [slicing, striding](#list--slicing-and-striding) and negative indexing, any list can be easily reversed without using any functions.
### Code Example:
Let's take an example of below list,
```python
a = [5,3,4,7,2]
```

What is negative index? Well, in python It's possible to access a list from right to left (⬅) instead of left to right (➡) with a negative index,

![Negative Indexing](images/01.svg)

```python
a[-1] # -> 2
a[-3] # -> 4
```

🤔 So how can you reverse a string?

```python
a[::-1] # -> [2,7,4,3,5]
# how cool is that? 😎
```

Working with negative index and slicing/striding

```python
a[-3:-1] # -> [4,7]
a[-1:-3:-1] # -> [2,7]
```

🛑 CAUTION! While negative indexes look cool they can introduce hard to debug bugs in your code... How you ask?

```python
len_a = len(a)
while True:
    try:
        print(a[len_a - 1])
        len_a -= 1
    except IndexError as ie:
        break
```
Instead of going out of index at index -1, due to negative indexing, it loops the list twice ->

```python
# prints each of the below in new line
# 2 7 4 3 5 2 7 4 3 5
```

While above example does seem far fetched, one might fall into this trap if they don't consider that index below *0* can be accessed in python, unlike other programming language.


### Reference Material:
- {{< newtabref  href="https://www.quora.com/What-is-negative-index-in-Python" title="https://www.quora.com/What-is-negative-index-in-Python">}}
- {{< newtabref  href="https://www.programiz.com/python-programming/methods/list/reverse" title="https://www.programiz.com/python-programming/methods/list/reverse">}}

<br>

## List \| List Comprehension
Python has "map()" and "filter()" methods to map or filter values in an iterable. Same can be done using list comprehensions, which is a more accessible and easy to understand version of the prior methods.

### Code Example: 
Consider following list,
```python
strings = ["to,","infinity","and","beyond!"]
```

🤔 Map : Convert all words in a list to upper case

```python
# With For Loops - 
capital_strings = []
for s in strings:
    capital_strings.append(s.upper())

# With List Comprehension - 
capital_strings = [s.upper() for s in strings]
```

🤔 Filter: Only fetch words with letter 'o'

```python
# With For Loops -
words_with_o = []
for s in strings:
    if 'o' in s:
        words_with_o.append(s)

# With list comprehension -
words_with_o = [s for s in strings if 'o' in s]
```

🤔 Map and Filter: Capitalize only words with 'o'
```python
# With For Loops -
capitalize_words_with_o = []
for s in strings:
    if 'o' in s:
        capitalize_words_with_o.append(s.capitalize())
    else:
        capitalize_words_with_o.append(s)

# With List Comprehension -
capitalize_words_with_o = [
    s.capitalize() if 'o' in s else s for s in strings
    ]
```

#### ✍ Things to Remember,
1. `[f(x) for x in sequence]`, here *f(x)* denote any function that can be applied, *x* is every element in *sequence* (List, Tuple, etc.)
2. `[f(x) for x in sequence if condition]`, here condition denotes any condition.
3. `[f(x) if condition else g(x) for x in sequence]`, where *g(x)* denotes any function defined in else construct.
4. While it's possible to work with nested lists using list comprehensions, I would advice against it. As it can quickly get unreadable and really inconvenient.

### Reference Material: 
- {{< newtabref  href="https://realpython.com/list-comprehension-python/" title="https://realpython.com/list-comprehension-python/">}}
- {{< newtabref  href="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions" title="https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions">}}


<br><br>


If you felt these items were too basic for your tastes. I do have a [Part 2](/features-that-define-python-p2) that has slightly more useful features. Do check it out!
