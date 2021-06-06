---
title:  "🖐️ Listed | 5 Features Unique To Python"
layout: post
categories: [python]
image: /assets/img/P003/cover.png
description: "Including a list of language-specific features that I wish I knew when I had started using python for my projects."
customexcerpt: "Including a list of language-specific features that I wish I knew when I had started using python for my projects."
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
Suppose you want to print *"First Element in list [1,2,3,4,5] is 1"*, you can do one of the following things,

Using Old Approach

```python
arr = [1,2,3,4,5]
print("First Element in List %s is %s" % (arr, arr[0]))
```

Using `str.format()`

```python
arr = [1,2,3,4,5]
print('First Element in List {} is {}'.format(arr, arr[0]))
# OR
print('First Element in List {0} is {1}'.format(arr, arr[0]))
# OR
print('First Element in List {arr} is {first_element}'.format(arr=arr, first_element=arr[0]))
```

Using f-strings

```python
arr = [1,2,3,4,5]
print(f'First Element in List {arr} is {arr[0]}')
# Now that's the cleanest of the lot, isn't it?
```

String formatting is not limited to just introducing a variable in-between string, you can do a variety of [fancy things](https://docs.python.org/3.4/library/string.html#formatspec){:target="_blank"} while formating. F-Strings also supports those, here is a [Python String Formatting Mini Language Quick Reference](https://gist.github.com/gauthamchettiar/fa3f32758616611bfecf941809fd598b){:target="_blank"} in case you are curious.

### Reference Material:
- [https://realpython.com/python-f-strings](https://realpython.com/python-f-strings/){:target="_blank"}
- [https://realpython.com/python-string-formatting/](https://realpython.com/python-string-formatting/){:target="_blank"}
- [https://www.python.org/dev/peps/pep-0498/](https://www.python.org/dev/peps/pep-0498/){:target="_blank"}

<br>

## Generic \| Multiple Assignment Unpacking
### Usecase: Unpacking Multiple Return Values
Python does not exactly allow multiple return values, but it can be done with a mix of returning a tuple and assigning it to multiple variables using multiple assignment unpacking feature. How does it exactly work tho?
### Code Example:
In Python, Multiple variables can be assigned on a single line as,

```python
a,b = 1,2
```

Now if value on right  (➡) is a `Tuple ()` or `List []` all values will be unpacked and individually assigned to each variable on left (⬅), this is called "Multiple Assignment Unpacking"

```python
a,b = [1,2]     # a=1 and b=2
a,b,c = [1,2,3] # a=1 , b=2 and c=3
```

In case any value needs to be ignored `'_'` can be used

```python
_,b = [3,5] # 5 will be set to 'b' and 3 will be ignored
# similarly,
a,_ = [4,6] # 4 will be set to 'a' and 6 will be ignored
# also,
a,_,c = [4,6,8] 
# 4 and 8 will be set to 'a' and 'c' respectively 
# and 6 will be ignored
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

In examples we have seen so far, number of variables in left (⬅) and values on right (➡) have been equal. Now what if number of variables on left (⬅) and number of values on right (➡) differ?

```python
a,b = [1,2,3,4] # THIS WILL THROW AN ERROR!
# -> ValueError: too many values to unpack (expected 2)

# But python does have one cool trick up it's sleeve,
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
In Python, strings are just like a list of characters. Which makes it possible to use list operations on strings as well. Slicing and Striding are one of the most useful feature of list, that can be used to extract certain portions of list.
### Code Example:
Let's take an example of below list,

```python
a = [1,2,3,4,5]
# list  = [1,2,3,4,5]
# index = [0,1,2,3,4]
```

Now when you say lists can be slices, it literally means that -

```python
# a[start_index:end_index]
a[1:3] # Returns [2,3]
# Starts at index=1(inclusive), ends at index=3(exclusive)
a[:3] # Returns [1,2,3]
# leaving start_index starts from first value (index 0)
a[2:] # Returns [3,4,5]
# Leaving end_index ends at the last value
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
# So this is not really a robust solution
```

Things to remember,
1. For slicing - `arr[start_index:end_index]`, where *start_index* is **inclusive** and *end_index* is **exclusive**.
2. For striding - `arr[start_index:end_index:step]`, where *step - 1* elements will be **skipped in-between**.  

### Reference Material:
- [https://realpython.com/lessons/string-slicing/](https://realpython.com/lessons/string-slicing/){:target="_blank"}
- [https://www.datacamp.com/community/tutorials/python-string-tutorial](https://www.datacamp.com/community/tutorials/python-string-tutorial){:target="_blank"}

<br>

## List \| Negative Indexing
### Usecase: Reversing a list
Along with [slicing, striding](#list--slicing-and-striding) and negative indexing, any list can be easily reversed without using any functions.
### Code Example:
Let's take an example of below list,
```python
a = [1,2,3,4,5]
```

What is negative index? Well, in python It's possible to access a list from right to left (⬅) instead of left to right (➡) with a negative index,

```python
a[-1] # returns 5
a[-3] # returns 3
# list_val  = [ 1 , 2 , 3 , 4 , 5 ]
# neg_index = [-5, -4, -3, -2, -1 ]
# pos_index = [ 0 , 1 , 2 , 3 , 4 ]
```

So how can you reverse a string?

```python
a[::-1] # [5,4,3,2,1]
# How cool is that!
```

Working with negative index and slicing/striding

```python
a[-3:-1] # [3,4]
a[-1:-3:-1] #  [5,4]
```

⚠ CAUTION! While negative indexes look cool they can introduce hard to debug bugs in your code... How you ask?

```python
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
```

While above example does seem far fetched, one might fall into this trap if they don't consider that index below *0* can be accessed in python, unlike other programming language.


### Reference Material:
- [https://www.quora.com/What-is-negative-index-in-Python](https://www.quora.com/What-is-negative-index-in-Python){:target="_blank"}
- [https://www.programiz.com/python-programming/methods/list/reverse](https://www.programiz.com/python-programming/methods/list/reverse){:target="_blank"}

<br>

## List \| List Comprehension
### Usecase: Map and/or Filter a list easily
While python does have Map and Filter functions to do exactly that, list comprehensions are more beginner-friendly.
### Code Example: 

Map: Convert all words in a list to uppercase()

```python
strings = ["hello,","say","this","louder!"]

# With For Loops
capital_strings = []
for s in strings:
    capital_strings.append(s.upper())

# With list comprehension
capital_strings = [s.upper() for s in strings]

# Returns ['HELLO,', 'SAY', 'THIS', 'LOUDER!']
```

Filter: Only fetch words with letter 'o'

```python
strings = ["hello,","say","this","louder!"]

# With For Loops
words_with_o = []
for s in strings:
    if 'o' in s:
        words_with_o.append(s)

# With list comprehension
words_with_o = [s for s in strings if 'o' in s]

# Returns ['hello,', 'louder!']
```

Map and Filter: Capitalize only words with 'o'

```python
strings = ["hello,","say","this","louder!"]

# With For Loops
capitalize_words_with_o = []
for s in strings:
    if 'o' in s:
        capitalize_words_with_o.append(s.capitalize())
    else:
        capitalize_words_with_o.append(s)

# With List Comprehension
capitalize_words_with_o = [s.capitalize() if 'o' in s else s for s in strings]

# Returns ['Hello,', 'say', 'this', 'Louder!']
```

Things to Remember,
1. `[f(x) for x in sequence]`, here *f(x)* denote any function that can be applied, *x* is every element in *sequence* (List, Tuple, etc.)
2. `[f(x) for x in sequence if condition]`, here condition denotes any condition.
3. `[f(x) if condition else g(x) for x in sequence]`, where *g(x)* denotes any function defined in else construct.
4. While it's possible to work with nested lists using list comprehensions, I would advice against it. As it can quickly get unreadable and really inconvenient.

### Reference Material: 
- [https://realpython.com/list-comprehension-python/](https://realpython.com/list-comprehension-python/){:target="_blank"}
- [https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions){:target="_blank"}


<br><br>


If you felt these items were too basic for your tastes. I have decided to do a Part 2 with slightly more useful features of Python. Don't forget to check later!

Also, Have a nice day!