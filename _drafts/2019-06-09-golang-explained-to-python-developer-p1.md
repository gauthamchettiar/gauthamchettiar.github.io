---
layout: post
title:  "Golang Explained to a Python Developer"
# date:   2020-07-09 14:00:00 +0530
categories: programming golang
permalink: /golang-explained-to-python-developer-p1
---

[Let's skip formality and just dive in >](#thinking-in-golang)

![GOPHER_LEARN](https://github.com/ashleymcnamara/gophers/blob/master/GOPHER_LEARN.png?raw=true)
Photo Credit : [https://github.com/ashleymcnamara/gophers](https://github.com/ashleymcnamara/gophers)

> I wish there was only a single programming language to learn!
{: class="note_grey"}

In theory such a language is possible but it has to be extremely well designed to cater every programmer's need. Each language was incepted out of frustration or limitation of some other language. For Example, out of an extremely verbose java was born some of the beloved languages - Kotlin and Scala.

Likewise, Golang and Python are designed for two very distinct usecases - former being adopted as more of a networking and microservices language and later as a backend web and data analytics language. It should be noted that both are general purpose laguage and can be used to implement any variety of applications. 

This article should act as a goto reference for developers used to python or any programming language and looking to add another language under their belt. Most of the formal introduction to programming concepts has been skipped to make it as concise as possible. Links have been provided, wherever necessary in case you are new to any of the concepts. 

So, here we go...

## Thinking in Golang
Ok, Wait... Before we dive. We must know how deep the pool is, right?

> Go picked some concepts from procedural programming, functional programming and object oriented programming, and put them together, and left out other concepts to create its own unique flavour of idiomatic programming style. [(source)](https://flaviocopes.com/golang-is-go-object-oriented/)
{: class="note_grey"}

Golang is a **compiled language** - Write -> Compile -> Run. Being a compiled language it has benefits of one like SPEED! While overall development time may increase, due to constant compilation and execution, execution speed is a lot better than it's interpreted cousin. [Difference explained](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/) \| [G](https://www.google.com/search?q=compiled+vs+interpreted+language)

Golang is a **statically typed language** - So a cat can only be a cat and not a dog or a pigeon or a tiger or anything. Golang will complain at compile time if you try to reassign an integer variable with string. In python all variables are allowed to dream, anyone can be anyone! [Difference explained](https://android.jlelse.eu/magic-lies-here-statically-typed-vs-dynamically-typed-languages-d151c7f95e2b) \| [G](https://www.google.com/search?q=statically+typed+vs+dynamically+typed+language)

Golang is **object oriented**, well partially - Go has a toned down version of OOPs concepts.
[Golang's version of OOPs](https://flaviocopes.com/golang-is-go-object-oriented/) \| [G](https://www.google.com/search?q=is+golang+object+oriented)  
Some of the OOPs concept implemented in Golang,
- Go has no concept of **classes**, so no **inheritance** or **objects**! But, Go supports struct type (borrowed from procedural language - C) which coupled with interfaces is the closest you can get to classes in Golang.
- **encapsulation** - Private/Public fields and methods? Heck yeah, Go supports that!
- **interfaces** - Go has a very different implementation of Interface, different from any other language. Interfaces in Go effectvely manages to implement **polymorphism** and **inheritance** as well, which will be explained later.

Golang has... deep inhale... **pointers** - This single point might have made the pool more than 10 feet deep. Well, It's not as bad as you might have heard or used in C. Rather Golang has this modern approach towards pointers. This could very well be major chunk of re-learning that this article might offer. [Pointers explained](https://www.quora.com/What-are-pointers) \| [G](https://www.google.com/search?q=what+are+pointers+in+programming)

Golang has excellent **concurrency** support - Go has concurrency running in it's veins. Goroutines are go's version of implementing concurrency, and it sure does implement it better than most languages. Another feature that makes Golang popular for networking applications. [Concurrency vs Parallelism](https://medium.com/@tilaklodha/concurrency-and-parallelism-in-golang-5333e9a4ba64) \| [G](https://www.google.com/search?q=concurrency+vs+parallelism)

Golang has a **garbage collector** - A ninja saving some sweet sweet memory. [Garbage Collector explained](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals) \| [G](https://www.google.com/search?q=what+is+garbage+collector+in+java)

Golang builds apps into a **single binary** - So you want to run a program? Sure, It's tiny just an MB in size, but don't forget to install these 400MB dependencies aswell! Golang doesn't have that issue, as it compiles any application into a single binary along with all the dependencies. This swells the binary size, but on the other hand simplifies deployments - no wonder container people love it! [Portable Golang](https://codeburst.io/why-golang-is-great-for-portable-apps-94cf1236f481) \| [G](https://www.google.com/search?q=golang+single+binary)

## The boring stuff - Installation and Setup
Go Installation is as simple as any software installation can get,  
Download appropriate package from here : [https://golang.org/dl/](https://golang.org/dl/)

Follow OS Specific Instructions as below,  
- Mac? - [https://golang.org/doc/install#macos](https://golang.org/doc/install#macos)  
- Windows? - [http://golang.org/doc/install#windows](http://golang.org/doc/install#windows)  
- Linux? - [https://golang.org/doc/install#tarball](https://golang.org/doc/install#tarball)  
- Feeling adventurous? Install Go from source - [https://golang.org/doc/install/source](https://golang.org/doc/install/source)

Just to make life easier, let's setup an IDE (completely optional though),  
- Coming from Pycharm? - [https://www.jetbrains.com/go/](https://www.jetbrains.com/go/)  
- What about Visual Studio Code? - [https://code.visualstudio.com/docs/languages/go](https://code.visualstudio.com/docs/languages/go)  
- Nah, I am more of a Sublime person... - [https://packagecontrol.io/packages/GoSublime](https://packagecontrol.io/packages/GoSublime)  

> Go 1.14 was the latest release, when this article was written.
{: class="note_yellow"}

## No language can be learnt without you - Dear, Hello World!

## Keep your values fresh - Variables

## Anyone asked for variety? - Typesystem #1

## Apple or Pineapple? - Logic

## Eat. Sleep. Repeat. - Loops

## Go green, reduce code footprint - Functions

## Wait, there's more variety! - Typesystem #2

## Is it a class? Is it an object? - It's Struct!

## The todo list - Interface

## It wasn't me, he did it! - Pointers

## To Err is Huuan- Error Handling

## I will do it later - Defer
