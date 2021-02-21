---
layout: post
title:  "🧩 OPP | Nth Digit of an Integer | [EASY]"
description: "OPP or Overanalyzing Programming Problems is a Series that explores different ways to solve a programming problem, this article explores - 'Nth Digit of an Integer'"
thumb_image: "overanalysing-programming-problems-nth-digit-of-an-integer/undraw_counting_stars_rrnl.png"
tags: [python, opp]
---
{% include static_image.html path="overanalysing-programming-problems-nth-digit-of-an-integer/undraw_counting_stars_rrnl.png" alt="Cover - Counting Stars" %}
*Illustration Source: "Counting Stars" from [https://undraw.co](https://undraw.co/)*  
&nbsp;  

Just as I submitted my problem and got a green check across all the tests, I wondered - "How I could have improved it?"

There are often several ways to solve a problem. The most efficient problem is not the easiest for humans to understand and vice versa. So the best bet is finding a middle ground. One that would not make you go "What the heck does this do?" - When you get back to it after a year or so. Also, one that would probably not suck your CPU dry.

A few notes about this article,
1. You can find [Index](#index) at the bottom of this article, but I would suggest go blind and discover topics as discussed.
2. Although all code snippets are written in Python, concepts that are specific to Language are explained in the [Appendix](#appendix) below, just to keep this article generic.
3. This article is useful in one of the below scenarios,
    - You are new to solving programming problems and would like to learn how to approach one.
    - You are new to Python and would like to learn it by doing.

This problem is relatively easy, it's a teeny tiny warm-up problem to get started with, if it seems too easy for your appetite, hold tight, upcoming ones would get gradually difficult!

&nbsp;  

# Problem : Nth Digit of an Integer
> **Statement :** Given an integer find the digit at Nth place from right, assuming 1 is the Units place. E.g: If `Integer=1975` and `N=3`, then the output should be `9`. (This example would be considered in all the examples and illustrations below)

> Here's a simple illustration to understand the above problem statement,
{% include image.html path="overanalysing-programming-problems-nth-digit-of-an-integer/Nth_digit_of_an_Integer_Illustration.png" path-detail="overanalysing-programming-problems-nth-digit-of-an-integer/Nth_digit_of_an_Integer_Illustration.png" alt="Nth Digit Of an Integer" %}

Before we start solving this problem, here's an empty method description in python to get you started with. Just copy it over to your preferred editor, code in your solution and RUN IT!

{% highlight python %}
import unittest

def nth_digit_of_integer(integer, n):
    # write your logic here
    # start with the simplest thing that comes to your mind
    # it doesn't have to be fast, it doesn't have to be short
    # rather focus on getting the correct answer


# you may ignore the test definition below
class TestNthDigitOfInteger(unittest.TestCase):
    def test_with_proper_inputs(self):
        assert 9 == nth_digit_of_integer(1975, 3)
        assert 5 == nth_digit_of_integer(1975, 1)
        assert 6 == nth_digit_of_integer(654321, 6)

if __name__ == '__main__':
    unittest.main()
{% endhighlight %}


*Before committing to continue reading this article I would recommend you to pause and solve this yourself. Maybe this article includes and analyses one of your solutions or maybe you came up with a better solution. As some wise man once said - The best way to learn to code is to DIY!*

## Solution 1 : Pythonic way
The most pythonic way to do it would be to convert integers to strings and get the negative Nth index. If you are not that familiar with Python you can find more on it here, [Appendix - Python : Strings and Indices](#python--strings-and-indices).
{% highlight python %}
# S1 - Pythonic Way
def nth_digit_of_integer(integer, n):
    # str() converts integer to string to make it traversable
    # [-n] negative index allows to traverse that string backwards
    # int() converts the fetched character string back to integer
    return int(str(integer)[-n])
{% endhighlight %}
Wow! That's a fancy one-line solution for sure. But the thing is it's not the most efficient way to do it, neither it's a generic solution.

## Solution 2 : Using Loop
Getting the last digit of any number is as simple as dividing the number by 10 and getting the remainder. Using this, every digit in an integer can be traversed by constantly reducing the integer (divide it by 10) and getting the last digit each time.
{% highlight python %}
# S2 - Using Loop
import math
def nth_digit_of_integer(integer, n):
    # logic can be understood better in the illustration below
    while n > 0:
        # mod (%) operator returns remainder after
        #   dividing by the number to it's right - here it's 10
        last_digit = integer % 10
        # math.floor() rounds any foating point value to
        #   an integer, such that integer is lower than the given float
        #   e.g: 
        #   math.floor(8.99) == 8
        #   math.floor(2.12) == 2
        integer = math.floor(integer / 10)
        n = n - 1
    return last_digit
{% endhighlight %}
Here is an illustration detailing the logic above,
{% include image.html path="overanalysing-programming-problems-nth-digit-of-an-integer/Problem1-Solution2_While_loop.png" path-detail="overanalysing-programming-problems-nth-digit-of-an-integer/Problem1-Solution2_While_loop.png" alt="Problem 1 - Solution 2 : Reduce by 10 (Loop)" %}

This is a possible solution. It does get solved in O(n) time but there is an even better solution out there (no it's not recursion).

## Solution 3 : Using Recursion
Often recursion is not the best way to go by for solving problems, as they do more harm than good. This is due to the fact that, with each call there is a stack call made, which adds overhead to the solution. Still, they are extremely fun to implement. Same problem can also be solved using recursion as, 
{% highlight python %}
# S3 - Using Recursion
def nth_digit_of_integer(integer, n):
    if n == 1:
        return integer % 10
    else:
        return nth_digit_of_integer(integer // 10, n-1)
{% endhighlight %}
Recursion works in ways similar to loops. Just instead of reducing inside a loop, we reduce and re-call the same function. Again an illustration to simplify this,
{% include image.html path="overanalysing-programming-problems-nth-digit-of-an-integer/Problem1-Solution3_Recursion.png" path-detail="overanalysing-programming-problems-nth-digit-of-an-integer/Problem1-Solution3_Recursion.png" alt="Problem 1 - Solution 2 : Reduce by 10 (Recursion)" %}

## Solution 4 : Mathematically
Usually the ones that is not easy to come up with, but also the ones that are the most efficient of all. If this is what you used to solve this problem, then kudos - "You are a mathematical Nerd!"
{% highlight python %}
# S4 - Mathematically
import math
def nth_digit_of_integer(integer, n):
    # below solution might seem complex at first but it is
    #   actually a lot simpler
    # here's an explainer, 
    #   math.pow(10, 3-1) -> returns 10 raise to 2 = 100
    #   1975 / 100 -> returns 19.75
    #   math.floor(19.75) -> returns 19
    #   19 % 10 -> returns 9
    return math.floor(integer / math.pow(10, n-1)) % 10
{% endhighlight %}
Also, these type of solutions are the most boring and requires you to have a really good mathematical fundamentals!  

That actually concludes Problem 1, but we still have issues in all our solutions. We never thought about error handlings...

## Error Handling

Now, 
1. What if `n` provided is greater than our integer's digit size? 
2. What if `n` is `0` or a negative number like `-3`

Some of our solutions would certainly fail for them right? I will add a few more test-cases to cater to this scenario. Also since it's not clearly given in problem statement as to what to do in such cases, let's just return `-1`.

{% highlight python %}
# Nth Digit of an Integer
import unittest

def nth_digit_of_integer(integer, n):
    # write your logic here

class TestNthDigitOfInteger(unittest.TestCase):
    def test_with_proper_inputs(self):
        assert 9 == nth_digit_of_integer(1975, 3)
        assert 5 == nth_digit_of_integer(1975, 1)
        assert 6 == nth_digit_of_integer(654321, 6)
        assert -1 == nth_digit_of_integer(654321, 7)
        assert -1 == nth_digit_of_integer(654321, 0)
        assert -1 == nth_digit_of_integer(654321, -3) 
{% endhighlight %}
Take this up like an assignment, pick one of your favorite solution from above (or your own solution) and try to cater to newly added test-cases.

## Bonus Problems

### Problem : Nth digit of an Integer (counted from left)
> **Statement :** Given an integer find the digit at Nth place from left, with index starting from 1. E.g: If `Integer=1975` and `N=3`, then the output should be `7`.

> **Illustration :**
{% include image.html path="overanalysing-programming-problems-nth-digit-of-an-integer/Nth_digit_of_an_Integer_Reverse_Illustration.png" path-detail="overanalysing-programming-problems-nth-digit-of-an-integer/Nth_digit_of_an_Integer_Reverse_Illustration.png" alt="Nth Digit Of an Integer (Counted From Left)" %}

That concludes this article. Thanks for your patience! ❤️

Any mistakes I made? Constructive criticism is welcome! Feel free to contact me on [LinkedIn](https://www.linkedin.com/in/gauthamchettiar)

&nbsp;  

# Appendix
## Python : Strings and Indices
Some Python features are really unique to the language, Strings can be traversed like a list and there are negative indexes in python. Explained in detail below,
{% highlight python %}
integer = 1975
# string conversion in python is simple, just call str() function
integer_str = str(integer) # integer_str containes '1975' string
# characters in strings can be accessed just like an array
integer_str[0] # this would return -> 1
integer_str[1] # this would return -> 9
# unlike other languages, python include negative indexes
# negative indexes are used to traverse an array/list/string in reverse
integer_str[-1] # this would return -> 5
integer_str[-2] # this would return -> 7
{% endhighlight %}

## Python : math.floor() and math.pow() shortcuts
Python does have some nifty tricks up it's sleeve. One of them are 2 commonly used operators that are unique to the language,
{% highlight python %}
import math
floored_float = math.floor(1975 / 10)
floored_float_2 = 1975 // 10
# (//) operator is similar to (/) division operator but
#   instead of returning a float, it returns a floored integer
#   this is quite useful in scenarios where only
#   quotient is expected out of a division
raise_to_2 = math.pow(10, 2)
raise_ro_2_operator = 10 ** 2
# (**) operator is alternative to math.pow()
{% endhighlight %}
&nbsp;  

# Index
- [Problem : Nth Digit of an Integer](#problem--nth-digit-of-an-integer)
  - [Solution 1 : Pythonic way](#solution-1--pythonic-way)
  - [Solution 2 : Using Loop](#solution-2--using-loop)
  - [Solution 3 : Using Recursion](#solution-3--using-recursion)
  - [Solution 4 : Mathematically](#solution-4--mathematically)
  - [Error Handling](#error-handling)
- [Appendix](#appendix)
  - [Python : Strings and Indices](#python--strings-and-indices)
  - [Python : math.floor() and math.pow() shortcuts](#python--mathfloor-and-mathpow-shortcuts)