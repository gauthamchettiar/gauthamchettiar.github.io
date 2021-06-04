---
title:  "🖐️ Listed | 5 Features Unique To Python"
layout: post
categories: [python]
image: /assets/img/P003/cover.png
description: "Including a list of language specific features that I wish I knew when I had started using python for my projects."
customexcerpt: "Including a list of language specific features that I wish I knew when I had started using python for my projects."
---
![Cover](assets/img/P003/cover.png)
Illustration Source: "Online Reading" from [https://undraw.co](https://undraw.co/){:target="_blank"}

Python has topped as one of the most sought-after programming language in recent times. Mostly due to its simplicity and a feature-set that makes coding a breeze. This has in turn lead to several tutorials for pythons focusing more on beginner-level topics, but when you look for places to get out of that initial shell, the material is scarce. I am writing this article to act as a bridge in such a case.

This article focuses on really simple but useful features of Python. You can use below [Index](#index) as a reference and skip to topics that are relevant to you. Each item is complete in itself and does not require reading any of the prior items, unless explicitly mentioned.

Each list item is divided into 3 sections,
- Usecase
- Code Example 
- More Reference Material 

<br>

# Index
1. [Generic \| Interpolated f-strings](#generic--interpolated-f-strings)
2. [Generic \| Multiple Assignment Unpacking](#generic--multiple-assignment-unpacking)
3. [List \| Slicing and Striding](#list--slicing-and-striding)
4. [List \| Negative Indexing](#list--negative-indexing)
5. [List \| List Comprehension](#list--list-comprehension) 

<br>

## Generic \| Interpolated f-strings
### Usecase: Formatting Variables in-between String
There are often times when you need to print/write certain variables to console, file or web. This generally includes formatting variables in-between strings - "e.g: Last Element in list `[1,2,3,4,5]` is `5`". There are several ways to do this, using [string concatenation](https://realpython.com/python-string-split-concatenate-join/){:target="_blank"}, [str.format() function](https://www.geeksforgeeks.org/python-format-function/){:target="_blank"} and [% operator](https://www.geeksforgeeks.org/string-formatting-in-python-using/){:target="_blank"}. But most of the above listed approaches are extremely verbose or hard to maintain. In order to solve those problems, f-strings were introduced in python 3.6. 

**Only supported in Python Version >= 3.6**, and is probably not the best way to go by if you are not sure about run-time python version of your deployment.

### Code Example:
```python
a = [1,2,3,4,5]
# If we want to print : 
#   "Last Element in list [1,2,3,4,5] is 5"
# Old Approach
print("Last Element in List %s is %s" % (a, a[-1]))

# Using str.format()
print('Last Element in List {} is {}'.format(a, a[-1]))
print('Last Element in List {0} is {1}'.format(a, a[-1]))
print('Last Element in List {a} is {last_element}'.format(a=a, last_element=a[-1]))

# Using f-strings
print(f'Last Element in List {a} is {a[-1]}')
# Now that's the cleanest of the lot, isn't it?
```
String formatting, is not limited to just introducing a variable in-between string, you can do a variety of [fancy things](https://docs.python.org/3.4/library/string.html#formatspec){:target="_blank"} while formating. F-Strings also supports those, here is a [Python String Formatting Mini Language Quick Reference](https://gist.github.com/gauthamchettiar/fa3f32758616611bfecf941809fd598b){:target="_blank"} in case you are curious.

### Reference Material:
- [https://realpython.com/python-f-strings](https://realpython.com/python-f-strings/){:target="_blank"}
- [https://realpython.com/python-string-formatting/](https://realpython.com/python-string-formatting/){:target="_blank"}
- [https://www.python.org/dev/peps/pep-0498/](https://www.python.org/dev/peps/pep-0498/){:target="_blank"}

<br>

## Generic \| Multiple Assignment Unpacking
### Usecase: Unpacking Multiple Return Values
Python does not exactly allow multiple return values, but it can be done with a mix of returning a tuple and assiging it to multiple variables using multiple assignment unpacking feature. How does it exactly work tho?
### Code Example:
```python
# Multiple variables can be assigned on a single line
a,b = 1,2

# Now if value on right is a tuple or list
# all values will be unpacked and 
# individually assigned to each variable
a,b = [1,2]     # a=1 and b=2
a,b,c = [1,2,3] # a=1 , b=2 and c = 3

# In case any value needs to be ignored '_' can be used
# in below construct 5 will be set to b and 3 will be ignored
_,b = [3,5]
# similarly,
a,_ = [4,6]

# Following can be used if you don't want program to fail
# but instead return a default value in case of failure
def get_division(a, b):
    try:
        a / b
    except Exception as e:
        return (0, e)
    return (a / b, None)

div, error = get_division(1,2)
div, error = get_division(1,0)

# That's cool right?
# Now what if you number of variables on left and
# number of values on right differ?
a,b = [1,2,3,4] # THIS WILL THROW AN ERROR!
# -> ValueError: too many values to unpack (expected 2)

# But python does have one another cool trick up it's sleeve,
a,*b = [1,2,3,4]   # a = 1 and b = [2,3,4]
# Similarly,
*a,b = [1,2,3,4]   # a = [1,2,3] and b = 4
# What about?
a,*b,c = [1,2,3,4] # a = 1 , b = [2,3] and c = 4
```

### Reference Material:
- [https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/){:target="_blank"}
- [https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment){:target="_blank"}
- [https://www.python.org/dev/peps/pep-3132/](https://www.python.org/dev/peps/pep-3132/){:target="_blank"}

<br>

## List \| Slicing and Striding
### Usecase: Extracting Parts Of Strings
In Python, strings are just like a list of characters. Which makes it possible to use list operations possible on strings as well. Slicing and Striding are one of the most useful feature of list, that can be used to extract certain portions of list.
### Code Example:
```python
a = [1,2,3,4,5]
# list  = [1,2,3,4,5]
# index = [0,1,2,3,4]

# When you say lists can be sliced, it literally means that
# a[start_index:end_index]
a[1:3] # Returns [2,3]
# Starts at index=1(inclusive), ends at index=3(exclusive)
a[:3] # Returns [1,2,3]
# leaving start_index starts from first value (index 0)
a[2:] # Returns [3,4,5]
# Leaving end_index ends at the last value

# You can also give a step value that is useful
# to step over certain values
# a[start_index:end_index:step]
a[1:4:2] # Returns [2,4]
# Starts at index=1(i.e:2), ends at index=4(exclusive)(i.e:4),
# steps over index=3(i.e:3)
# This could be very confusing for first timers,
# here's some more example to make it easier to understand
a[::2] # Returns [1,3,5], step=2 means skip every 1 value
a[::3] # Returns [1,4], step=3 means skip every 2 value

# It's especially useful if you want to extract,
# certain characters from start or end of string
# Get first 4 digits of creditcard
credit_card = "4000056655665556"
credit_card[:4] # Returns '4000'
credit_card[12:] # Returns '5556'
# Creditcard number length can differ based on length,
# So this is not really a robust solution
```
### Reference Material:
- [https://realpython.com/lessons/string-slicing/](https://realpython.com/lessons/string-slicing/){:target="_blank"}
- [https://www.datacamp.com/community/tutorials/python-string-tutorial](https://www.datacamp.com/community/tutorials/python-string-tutorial){:target="_blank"}

<br>

## List \| Negative Indexing
### Usecase: Reversing a list
Along with [slicing, striding](#list--slicing-and-striding) and negative indexing, any list can be easily reversed without using any functions.
### Code Example:
```python
a = [1,2,3,4,5]
# What is negative index tho?
# It's possible to access a list from right to left
# instead of left to right with negative index
a[-1] # returns 5
a[-3] # returns 3
# List  = [ 1 , 2 , 3 , 4 , 5 ]
# Index = [-5, -4, -3, -2, -1 ]

# So how can you reverse a list?
a[::-1] # [5,4,3,2,1]
# How cool is that!

# Working with negative index and slicing/striding
a[-3:-1] # Returns [3,4]
a[-1:-3:-1] # Returns [5,4]

# CAUTION!
# While negative indexes look cool, 
# they can introduce hard to debug bugs in your code
# How you ask?
a = [1,2,3,4,5]
len_a = len(a)
while True:
    try:
        print(a[len_a - 1])
        len_a -= 1
    except IndexError as ie:
        break
# Instead of going out of index at index -1,
# due to negative indexing,
# it loops the list twice
# prints (each on a new line)-> 5 4 3 2 1 5 4 3 2 1

# While above example is a really bad example
# often one might fall into this trap, 
# if he/she is not aware about negative indexes
```

### Reference Material:
- [https://www.quora.com/What-is-negative-index-in-Python](https://www.quora.com/What-is-negative-index-in-Python){:target="_blank"}
- [https://www.programiz.com/python-programming/methods/list/reverse](https://www.programiz.com/python-programming/methods/list/reverse){:target="_blank"}

<br>

## List \| List Comprehension
### Usecase: 
### Code Example: 
### Reference Material: 

These items could have been too basic for your tastes. I have decided a Part 2 with slightly more useful features of Python. Don't forget to check later!

Also, Have a nice day!