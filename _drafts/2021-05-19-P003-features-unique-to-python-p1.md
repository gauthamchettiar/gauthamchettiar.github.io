---
title:  "🖐️ Listed | 5 Features Unique to Python"
layout: post
categories: [python]
image: /assets/img/P003/cover.png
description: "Including a list of language specific features that I wish I knew when I had started using python for my projects. This part lists features specific to Lists, Dicts and Functions."
customexcerpt: "Including a list of language specific features that I wish I knew when I had started using python for my projects. This part lists features specific to Lists, Dicts and Functions."
---
![Cover](assets/img/P003/cover.png)
Illustration Source: "Online Reading" from [https://undraw.co](https://undraw.co/){:target="_blank"}

Python has topped as one of the most sought-after programming language in recent times. Mostly due to its simplicity and a feature-set that makes coding a breeze. This has in turn lead to several tutorials for pythons focusing more on beginner-level topics, but when you look for places to get out of that initial shell, the material is scarce. I am writing this article to act as a bridge in such a case.

This article focuses on Lists, Dictionaries, and Functions. You can use below [Index](#index) as a reference and skip to topics that are relevant to you. Each item is complete in itself and does not require reading any of the prior items, unless explicitly mentioned.

Each list item is divided into 3 sections,
- Usecase
- Code Example 
- More Reference Material 

<br>

# Index
1. [Generic \| Interpolated f-strings](#generic--interpolated-f-strings)
2. [Generic \| Assignment Expressions](#generic--assignment-expressions)
3. [Generic \| Multiple Assignment Unpacking](#generic--multiple-assignment-unpacking)
4. [List \| List Comprehension](#list--list-comprehension)
5. [List \| Slicing and Striding](#list--slicing-and-striding)

<br>

## Generic \| Interpolated f-strings
### Usecase: Formatting Variables in-between String
There are often times when you need to print/write certain variables to console, file or web. This generally includes formatting variables in-between strings - "e.g: Last Element in list `[1,2,3,4,5]` is `5`". There are several ways to do this, using [string concatenation](https://realpython.com/python-string-split-concatenate-join/){:target="_blank"}, [str.format() function](https://www.geeksforgeeks.org/python-format-function/){:target="_blank"} and [% operator](https://www.geeksforgeeks.org/string-formatting-in-python-using/){:target="_blank"}. But most of the above listed approaches are extremely verbose or hard to maintain. In order to solve those problems, f-strings were introduced in python 3.6. 

**Only supported in Python Version >= 3.6**, and is probably not the best way to go by if you are not sure about run-time python version of your deployment.

### Code Example:
```python
num_list = [1,2,3,4,5]
# If we want to print : 
#   "Last Element in list [1,2,3,4,5] is 5"
# Old Approach
print("Last Element in List %s is %s" % (num_list, num_list[-1]))
# Using str.format()
print('Last Element in List {} is {}'.format(num_list, num_list[-1]))
print('Last Element in List {0} is {1}'.format(num_list, num_list[-1]))
print('Last Element in List {num_list} is {last_element}'.format(num_list=num_list, last_element=num_list[-1]))
# Using f-strings
print(f'Last Element in List {num_list} is {num_list[-1]}')
```
String formatting, is not limited to just introducing a variable in-between string, you can do a variety of [fancy things](https://docs.python.org/3.4/library/string.html#formatspec){:target="_blank"} while formating. F-Strings also supports those, here is a [Python String Formatting Mini Language Quick Reference](https://gist.github.com/gauthamchettiar/fa3f32758616611bfecf941809fd598b){:target="_blank"} in case you are curious.

### Reference Material:
- [https://realpython.com/python-f-strings](https://realpython.com/python-f-strings/){:target="_blank"}
- [https://realpython.com/python-string-formatting/](https://realpython.com/python-string-formatting/){:target="_blank"}
- [https://www.python.org/dev/peps/pep-0498/](https://www.python.org/dev/peps/pep-0498/){:target="_blank"}

<br>

## Generic \| Assignment Expressions
### Usecase: Variables that only has to be scoped inside a code block (`if` or `while`)
Scoping in python is slightly confusing. Variables defined inside a function cannot be accessed outside of it which is fair, but variables declared inside a code block like `if` or `while` can be accessed outside that code block. This is called scope-leak and often leads to hard-to-debug bugs. So in use-cases where a variable has to be declared exclusively for evaluation inside such a code block, it's best to use Assignment Expressions.

If you are wondering what about `for` loops? Well, it's impossible to not leak for loop variables, that's just how python is designed. You may go ahead and delete assigned variables at the end of for loop if that's what you want. Here's a snippet explaining 


### Code Example:
### Reference Material:
- [https://realpython.com/python-scope-legb-rule/](https://realpython.com/python-scope-legb-rule/){:target="_blank"}
- [https://www.python.org/dev/peps/pep-0572/](https://www.python.org/dev/peps/pep-0572/){:target="_blank"}

<br>

## Generic \| Multiple Assignment Unpacking
### Usecase: 
### Code Example:
### Reference Material:

<br>

## List \| List Comprehension
### Usecase: 
### Code Example:
### Reference Material:

<br>

## List \| Slicing and Striding
### Usecase: 
### Code Example:
### Reference Material:
