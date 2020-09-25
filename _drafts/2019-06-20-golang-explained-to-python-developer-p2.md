---
layout: post
title:  "Golang Explained to a Python Developer | Part 2"
# date:   2020-07-09 14:00:00 +0530
categories: technical golang
permalink: /golang-explained-to-python-developer-p2
---
This is Part 2 of "Golang Explained to Python Developer" Series. Make sure to go through [Part 1](/golang-explained-to-python-developer-p1) first if your are new to the language.  

[Skip to index >](#index#part-2)
![GOPHER-RIDING-REX](https://github.com/ashleymcnamara/gophers/blob/master/GOPHER%20RIDING%20REX.png?raw=true)
Picture Credits: [https://github.com/ashleymcnamara/gophers](https://github.com/ashleymcnamara/gophers)

In the first part, we learnt Go language constructs like,
- Writing and running a Go "Hello World" program
- Various data types that Go supports like `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `float32`, `float64`,  `complex64`, `complex128`, `byte`, `rune` and `string` 
- How constants are unique in Go.
- `if... else if... else...` and `switch{...}` in Go
- Using `for` to repeat. 
- What is `range` keyword all about in Go, we will explore this keyword more in detail this part.

So let's just get to the really good part...
<div class="tenor-gif-embed" data-postid="4106597" data-share-method="host" data-width="100%" data-aspect-ratio="2.4174757281553396"><a href="https://tenor.com/view/the-interview-seth-rogen-james-franco-its-showtime-showtime-gif-4106597">Showtime - The Interview GIF</a> from <a href="https://tenor.com/search/theinterview-gifs">Theinterview GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>

## Index
- [Part 1](/golang-explained-to-python-developer-p1)
- Part 2
  - [Wait, there's more variety! - Types #2](#wait-theres-more-variety---types-2)
  - [Is it a class? Is it an object? - It's Struct!](#is-it-a-class-is-it-an-object---its-struct)
  - [The todo list - Interface](#the-todo-list---interface)
  - [It wasn't me, he did it! - Pointers](#it-wasnt-me-he-did-it---pointers)
  - [To Err is Huuan- Error Handling](#to-err-is-huuan--error-handling)
  - [I will do it later - Defer](#i-will-do-it-later---defer)

## Wait, there's more variety! - Types #2
Apart from primitive data types Go supports arrays/slices and maps which are synonymous to lists and dictionaries in python. As always, Go has choosen to keep it's implementation unique to the language, 

### Arrays
Arrays in Go is just a collection of primitive data types; of **a fixed length**. I can hear python enthusiasts grunting as they read through that. Even though arrays lacks flexibility of lists from python, they are a lot more efficient. And who said Go didn't allow variable length, list like, implementation... 😉 More on that later.

```go
// defining an array in Go
var groceryList [4]string
```
Classic go, that likes to play everything in reverse - array notation `[]` along with element count `4` comes first followed by element type `string`.

Let's drop the verbose declaration syntax,
```go
// since := notation guesses a variable's type from
// it's assignment, you have to initialize the variable as follows
groceryList := [4]string{"sugar", "egg", "baking-soda", "cocoa powder"}
// going by that groceryList; they are baking a CAKE!!!
```

Vegetarian? Here's an ingredient list for an eggless cake,
```go
groceryList := [4]string{"sugar", "baking-soda", "cocoa powder"}
// that's some sweet egg-less CAKE!
```
Also yes, you don't have to initialize an array upto it's full length.

Since arrays are fixed length it is important to note that you cannot exceed that length, which means in this case you are only restricted to a maximum of 4 ingredients 😟. (Slices solve this, which we will explore soon...) 

Meanwhile here are some other important workings of arrays in Go,

1. What about accessing an item from an array?
```go
// good old square brackets to the rescue,
groceryList[0]
```

2. What is initialized in an empty array?
```go
// empty string in string array
groceryList := [4]string{}
fmt.Println(groceryList[0]) // will print empty string
// 0 in numerical variables
groceryCount := [4]int{}
fmt.Println(groceryList[0]) // will print 0
```

3. Getting length of an array.
```go
// using len function
groceryList := [4]string{}
len(groceryList) // will return 4
```

4. Three intelligent dots : Instead of passing array length in advance you can make Go deduct it with the help of `...` notation
```go
groceryList := [...]string{"sugar", "baking-soda", "cocoa powder"}
// above array will automatically create an array of length 3 
// with given elements
```

5. Reassigning an array
```go
groceryListWith3Items := [...]string{"honey", "butter", "cinnamon"}
groceryListWith2Items := [2]string{"raisins","cashews"}
// even if both are of type string their length differs
// thus reassigninment doesn't work
groceryListWith3Items = groceryListWith2Items //this will fail
```
With respect to arrays, element count is a part of type. So you can only assign an array to a different array, only if both are of same type and length.


6. Going 3D : Multidimensional arrays can be declared as,
```go
// this will create an array with,
// 3 arrays each of length 4
multiGroceryList := [3][4]string{
  {"sugar"},
  {"salt","milk","egg"},
  {"bread","butter"}, // this comma... kinda important
}
```
*&nbsp;A comma `,` at tha end of last element is compulsory.*{: class="note-red"}

> Arrays are **copied and passed by value**. So, if you assign a new variable with an existing array, both are stored as two distinct arrays. Modifying one array does not affect other one. This is also true when you pass a variable to any function.
{: class="note-yellow" }

### Slices - Arrays that grow
Slices are similar to lists in python. They are an alternative to a more restrictive array, such that, slices are flexible in it's size.

> Slices are just a wrapper around arrays. That is, slices don't store the underlying values but just points to some array that stores the actual value. *(Confused? Keep reading...)*
{: class="note-yellow"}

```go
// slice declaration is similar to arrays
// but just skip the length part
variableGroceryList := []string{"sugar", "salt", "milk", "egg"}
```


#### Capacity - How slices grow?

#### Ranges - Revisited

### Maps
## Is it a class? Is it an object? - It's Struct!

## The todo list - Interface

## It wasn't me, he did it! - Pointers

## To Err is Huuan- Error Handling

## I will do it later - Defer
