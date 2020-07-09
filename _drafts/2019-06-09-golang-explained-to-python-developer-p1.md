---
layout: post
title:  "Golang Explained to a Python Developer | Part 1"
# date:   2020-07-09 14:00:00 +0530
categories: technical golang
permalink: /:categories/golang-explained-to-python-developer-p1
---


[Let's skip formality and just dive in >](#thinking-in-go)  
[Jump to Index >](#index)  

![GOPHER_LEARN](https://github.com/ashleymcnamara/gophers/blob/master/GOPHER_LEARN.png?raw=true)
Photo Credit : [https://github.com/ashleymcnamara/gophers](https://github.com/ashleymcnamara/gophers)

> I wish there was just one universal programming language to learn!
{: class="note_grey"}

In theory such a language is possible but it has to be extremely well designed to cater every programmer's need. Each language was incepted out of frustration or limitation of some other language. For Example, out of an extremely verbose java was born some of the beloved languages - Kotlin and Scala.

Likewise, Go and Python are designed for two very distinct usecases - former being adopted as more of a networking and microservices language and later as a backend web and data analytics language. Though, both are general purpose laguage and can be used to implement any variety of applications. 

This article should act as a goto reference for developers used to python or any programming language and looking to add another language under their belt. Most of the formal introduction to programming concepts has been skipped to make it as concise as possible. Links have been provided, wherever necessary in case you are new to any of the concepts. 

So, here we go...

## Index
- Part 1
  - [Thinking in Go](#thinking-in-go)
  - [The boring stuff - Installation and Setup](#the-boring-stuff---installation-and-setup)
  - [Dear, Hello World!](#dear-hello-world)
  - [Keep your values fresh - Variables](#keep-your-values-fresh---variables)
  - [Anyone asked for variety? - Types #1](#anyone-asked-for-variety---types-1)
  - [Apple or Pineapple? - Logic](#apple-or-pineapple---logic)
  - [Eat. Sleep. Repeat. - Loops](#eat-sleep-repeat---loops)
  - [Reduce code footprint - Functions](#reduce-code-footprint---functions)
- Part 2 (Yet to be uploaded)
  - [Wait, there's more variety! - Types #2](#wait-theres-more-variety---types-2)
  - [Is it a class? Is it an object? - It's Struct!](#is-it-a-class-is-it-an-object---its-struct)
  - [The todo list - Interface](#the-todo-list---interface)
  - [It wasn't me, he did it! - Pointers](#it-wasnt-me-he-did-it---pointers)
  - [To Err is Huuan- Error Handling](#to-err-is-huuan--error-handling)
  - [I will do it later - Defer](#i-will-do-it-later---defer)

## Thinking in Go
Ok, Wait... Before we dive. We must know how deep the pool is, right?

> Go picked some concepts from procedural programming, functional programming and object oriented programming, and put them together, and left out other concepts to create its own unique flavour of idiomatic programming style. [[source]](https://flaviocopes.com/golang-is-go-object-oriented/)
{: class="note_grey"}

Above expression is all it takes to understand the philosophy of Go. Go was publicly announced in 2009, time when most of the languages were already mature. So developers had a lot of reference to work with. This unique language with cherry-picked feature set, helps to circumvent most of the issues you have with other languages and solves some of them in it's own way. That in no way means Go is superior to any language. You are the judge here, understand and decide for yourself...

Language features and limitations of Go are listed below:

1. Go is a **compiled language** - Write -> Compile -> Run. Being a compiled language it has benefits of one like SPEED! While overall development time may increase, due to constant compilation and execution, execution speed is a lot better than it's interpreted cousin. [Difference explained](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/) \| [G](https://www.google.com/search?q=compiled+vs+interpreted+language)

2. Go is a **statically typed language** - So a cat can only be a cat and not a dog or a pigeon or a tiger or anything. Go will complain at compile time if you try to reassign an integer variable with string. In python all variables are allowed to dream, anyone can be anyone! [Difference explained](https://android.jlelse.eu/magic-lies-here-statically-typed-vs-dynamically-typed-languages-d151c7f95e2b) \| [G](https://www.google.com/search?q=statically+typed+vs+dynamically+typed+language)

3. Go has... deep inhale... **pointers** - This single point might have made the pool more than 10 feet deep. Well, It's not as bad as you might have heard or used in C. Rather Go has this modern approach towards pointers. This could very well be major chunk of re-learning that this article might offer. [Pointers explained](https://www.quora.com/What-are-pointers) \| [G](https://www.google.com/search?q=what+are+pointers+in+programming)

4. Go has excellent **concurrency** support - Go has concurrency running in it's veins. Goroutines are go's version of implementing concurrency, and it sure does implement it better than most languages. Another feature that makes Go popular for networking applications. [Concurrency vs Parallelism](https://medium.com/@tilaklodha/concurrency-and-parallelism-in-golang-5333e9a4ba64) \| [G](https://www.google.com/search?q=concurrency+vs+parallelism)

5. Go has a **garbage collector** - A ninja saving some sweet sweet memory. [Garbage Collector explained](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals) \| [G](https://www.google.com/search?q=what+is+garbage+collector+in+java)

6. Go builds apps into a **single binary** - So you want to run a program? Sure, It's tiny just an MB in size, but don't forget to install these 400MB dependencies aswell! Go doesn't have that issue, as it compiles any application into a single binary along with all the dependencies. This swells the binary size, but on the other hand simplifies deployments - no wonder container people love it! [Portable Go](https://codeburst.io/why-golang-is-great-for-portable-apps-94cf1236f481) \| [G](https://www.google.com/search?q=golang+single+binary)

7. Go is **object oriented**, well partially - Go has a toned down version of OOP concepts.
[Go's version of OOP](https://flaviocopes.com/golang-is-go-object-oriented/) \| [G](https://www.google.com/search?q=is+golang+object+oriented)  
Some of the them implemented in Go,
   - Go has no concept of **classes**, so no **inheritance** or **objects**! But, Go supports struct type (borrowed from procedural language - C) which coupled with interfaces is the closest you can get to classes in Go.
   - Go has **encapsulation** - Private/Public fields and methods? Heck yeah, Go supports that!
   - Go has **interfaces** - Go has a very different implementation of Interface, different from any other language. Interfaces in Go effectvely manages to implement **polymorphism** and **inheritance** as well, which will be explained later.  

## The boring stuff - Installation and Setup
> It is recommended to have go installed in your system, but if you are here just to try it out then you may go ahead and skip this step. Go programs can be run online [here](https://play.golang.org/), but some examples might not work due to architectural limitations.
{: class="note_yellow"}
Go Installation is as simple as any software installation can get,  
Download appropriate package from here : [https://golang.org/dl/](https://golang.org/dl/)

Follow OS Specific Instructions as below,  
- Linux? - [https://golang.org/doc/install#tarball](https://golang.org/doc/install#tarball)  
- Mac? - [https://golang.org/doc/install#macos](https://golang.org/doc/install#macos)  
- Windows? - [http://golang.org/doc/install#windows](http://golang.org/doc/install#windows)  
- Feeling adventurous? Install Go from source - [https://golang.org/doc/install/source](https://golang.org/doc/install/source)

Just to make life easier, let's setup an IDE (completely optional though),  
- Coming from Pycharm? - [https://www.jetbrains.com/go/](https://www.jetbrains.com/go/)  
- What about Visual Studio Code? - [https://code.visualstudio.com/docs/languages/go](https://code.visualstudio.com/docs/languages/go)  
- Nah, I am more of a Sublime person... - [https://packagecontrol.io/packages/GoSublime](https://packagecontrol.io/packages/GoSublime)  

> **Go 1.14** was the latest release, when this article was written.
{: class="note_red"}

## Dear, Hello World!
Let's start with an all time favorite - **writing a hello world program**.  
> For all the examples given below it is assumed that you are logged in to a terminal and have created a new directory. Also, It makes sense to create one in your home directory.  <br/>
<!-- > Ok but, Where is my home though? - [Linux](https://askubuntu.com/questions/687267/where-is-the-home-folder-located) \| [Mac](https://apple.stackexchange.com/questions/51280/where-do-i-find-my-user-folder-in-the-os-x-folder-hierarchy) \| [Windows](https://askubuntu.com/questions/1180092/where-is-home-directory-on-windows) -->
{: class="note_yellow"}

Python does it simple, too simple :

```python
# hello_world.py
print("Hello World")
```  
Go is slightly verbose, yet clear in it's approach.
```go
// hello_world.go
package main  // go programs are organised in packages, more on this later
import "fmt"  // 'fmt' is the package containing Println method
func main() { // main function is your entry point to any program
    fmt.Println("hello world")  // and that's how you print to stdout
}
```
&nbsp;  
Same is true while **executing the program**, for python :
```bash
# executing a python program
python hello_world.py
```
While, Go gives you several ways to run your program,
1. Compile to a binary and then execute
```bash
# executing a go program
# while inside your project directory
go build hello_world.go # provides a compiled binary
./hello_world # runs the compiled binary
```
2. Compile and execute with a single command
```bash
# executing a go program
go run main.py  # this is just a shortcut for above commands
```

> It is important to note that, binary created by `go build` command is platform specific. Though, go provides toolsets to build binaries for any architecture or OS, refer [this](https://www.digitalocean.com/community/tutorials/building-go-applications-for-different-operating-systems-and-architectures).
{: class="note_red"}

> `func main() {...}` acts as an entry point to your application. You must make sure that the file you are trying to build/run includes this function. 
{: class="note_yellow"}

Go also has an online playground [https://play.golang.org/](https://play.golang.org/) that allows you to run your code on browser (albeit some restrictions), without having to install go, SWEET!!!

## Store your values fresh - Variables


## Anyone asked for variety? - Types #1

## Apple or Pineapple? - Logic

## Eat. Sleep. Repeat. - Loops

## Reduce code footprint - Functions

## Wait, there's more variety! - Types #2

## Is it a class? Is it an object? - It's Struct!

## The todo list - Interface

## It wasn't me, he did it! - Pointers

## To Err is Huuan- Error Handling

## I will do it later - Defer
