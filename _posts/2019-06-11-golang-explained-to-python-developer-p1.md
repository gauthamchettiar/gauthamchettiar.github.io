---
layout: post
title:  "Golang Explained to a Python Developer | Part 1"
# date:   2020-07-09 14:00:00 +0530
categories: technical golang
permalink: /golang-explained-to-python-developer-p1
---

This is Part 1 of "Golang Explained to Python Developer" Series.

[Let's skip formality and just dive in >](#thinking-in-go)  
[Jump to Index >](#index)  

![GOPHER_LEARN](https://github.com/ashleymcnamara/gophers/blob/master/GOPHER_LEARN.png?raw=true)
Photo Credit : [https://github.com/ashleymcnamara/gophers](https://github.com/ashleymcnamara/gophers)

> I wish there was just one universal programming language to learn!

In theory such a language is possible but it has to be extremely well designed to cater every programmer's need. Each language was incepted out of frustration or limitation of some other language. For Example, out of an extremely verbose java was born some of the beloved languages - Kotlin and Scala.

Likewise, Go and Python are designed for two very distinct usecases - former being adopted as more of a networking and microservices language and later as a backend web and data analytics language. Though, both are general purpose laguage and can be used to implement any variety of applications. 

This article should act as a goto reference for developers used to python or any programming language and looking to add another language under their belt. Most of the formal introduction to programming concepts has been skipped to make it as concise as possible. Links have been provided, wherever necessary in case you are new to any of the concepts. 

So, here we go...

<div class="tenor-gif-embed" data-postid="6905306" data-share-method="host" data-width="100%" data-aspect-ratio="1.7913669064748199"><a href="https://tenor.com/view/tim-gunn-come-on-everyone-waving-lets-go-gif-6905306">Let's Go GIF</a> from <a href="https://tenor.com/search/timgunn-gifs">Timgunn GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>

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
  - [Bonus](#bonus)
  - [Exercise](#exercise)
- Part 2 (Yet to be uploaded)

## Thinking in Go
> Go picked some concepts from procedural programming, functional programming and object oriented programming, and put them together, and left out other concepts to create its own unique flavour of idiomatic programming style. [[source]](https://flaviocopes.com/golang-is-go-object-oriented/)

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
{: class="note-yellow"}
Go Installation is as simple as any software installation can get,  
Download appropriate package from here : [https://golang.org/dl/](https://golang.org/dl/)

Follow OS Specific Instructions as below,  
- Linux? - [https://golang.org/doc/install#tarball](https://golang.org/doc/install#tarball)  
- Mac? - [https://golang.org/doc/install#macos](https://golang.org/doc/install#macos)  
- Windows? - [http://golang.org/doc/install#windows](http://golang.org/doc/install#windows)  
- Feeling adventurous? Install Go from source - [https://golang.org/doc/install/source](https://golang.org/doc/install/source)

Just to make life easier, let's setup an IDE (completely optional),  
- Coming from Pycharm? - [https://www.jetbrains.com/go/](https://www.jetbrains.com/go/)  
- What about Visual Studio Code? - [https://code.visualstudio.com/docs/languages/go](https://code.visualstudio.com/docs/languages/go)  
- Nah, I am more of a Sublime person... - [https://packagecontrol.io/packages/GoSublime](https://packagecontrol.io/packages/GoSublime)  

> **Go 1.14** was the latest release, when this article was written.
{: class="note-yellow"}

## Dear, Hello World!
Let's start with an all time favorite - **writing a hello world program**.  
<div class="tenor-gif-embed" data-postid="4903969" data-share-method="host" data-width="100%" data-aspect-ratio="1.6666666666666667"><a href="https://tenor.com/view/typing-jim-carrey-fast-busy-gif-4903969">Typing Jim Carrey GIF</a> from <a href="https://tenor.com/search/typing-gifs">Typing GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>
&nbsp;  
> For all the examples given below it is assumed that you are logged in to a terminal and have created a new directory. Also, It makes sense to create one in your home directory.  <br/>
<!-- > Ok but, Where is my home though? - [Linux](https://askubuntu.com/questions/687267/where-is-the-home-folder-located) \| [Mac](https://apple.stackexchange.com/questions/51280/where-do-i-find-my-user-folder-in-the-os-x-folder-hierarchy) \| [Windows](https://askubuntu.com/questions/1180092/where-is-home-directory-on-windows) -->
{: class="note-yellow"}

Python does it simple, too simple :

```python
# writing a hello_world python program saved as,
# hello_world.py
print("Hello World")
```  
Go is slightly verbose, yet clear in it's approach.
```go
// writing a hello_world fo program saved as,
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
go build hello_world.go # provides a compiled binary
./hello_world # runs the compiled binary
```
2. Compile and execute with a single command
```bash
# executing a go program
go run main.py  # this is just a shortcut for above commands
```

> Binary created by `go build` command is platform specific. Though, go provides toolsets to build binaries for any architecture or OS, refer [this](https://www.digitalocean.com/community/tutorials/building-go-applications-for-different-operating-systems-and-architectures).
{: class="note-red"}

> `package main` is required for a file to be recognised as a runnable. `func main() {...}` acts as an entry point to your application. You must make sure that the file you are trying to build/run includes both of them.  
{: class="note-yellow"}

Go also has an online playground [https://play.golang.org/](https://play.golang.org/) that allows you to run your code on browser (albeit some restrictions), without having to install go, SWEET!!!

## Keep your values fresh - Variables
Variables in python are a no brainer,
```python
fruit = "apple"
fruit_count = 2
fruit_cost = 199.99
```
In Go, variable declaration is in the format `var <name> <type>`,
```go
var fruit string = "apple"
var fruitCount int = 2
var fruitCost float32 = 199.99 // more about float32 later
```
> Notice how **variable type** comes after **variable name**? That's how it's done in Go. This would take time to get used to, even if you are not from a python background.
{: class="note-yellow"}
&nbsp;  
In python it's not possible to just declare a value and not assign to it (being a dynamic language, that's not even required), Go being a statically typed language alows to do so,
```go
var fruit string  // Initialized with empty string
var fruitCount int // Initialized with 0 
var fruitCost float32 // Initialized with 0
```
&nbsp;  
There's more to variable declaration in Go, each of them listed below -
1. Do I always have to pass variable type, is **type inference** not a thing in Go?
```go
// If you are assigning a variable during declaration
// below syntax works fine, due to type inference
var fruit = "apple"
var fruitCount = 2
var fruitCost = 199.99
```
2. What if I want to declare **multiple variables in a single line**, is there a shortcut?
```go
// both must be of same type, since type is explicitly passed
var fruitExpensive, fruitCheap string = "apple", "banana"
// if no type is passed, different types of variable can be assigned
// in a single line, due to type inference
var fruitExpensiveCount, fruitExpensiveCost = 2, 199.99
var (
  fruitCheapCount, fruitCheapCost = 12, 9.99
  // Adding more variable declarations here works fine in go
)
```
3. Python is still simpler, I don't have to write `var` or `<type>` for every variable declaration...
```go
// you can drop all the keywords and use
// := notation
// this is a shorthand for above declarations
fruitExpensive := "apple"
fruitCheap := "banana"
fruitExpensiveCount, fruit_expensiveCost := 2,199.99
fruitCheapCount, fruitCheapCost := 12, 9.99
```
4. That shorthand makes it feel dynamic, can I **overwrite a variable with a different type**?  
```go
fruitNameOrCount := "apple"
fruitNameOrCount = "banana"
// this is REASSIGNMENT, thus works
// value of variable fruitNameOrCount is now banana
fruitNameOrCount := "banana"
// this is REDECLARATION, thus doesn't work, throws
// ERROR: no new variables on left side of :=
fruitNameOrCount := 2
// same goes in this case, throws
// ERROR: no new variables on left side of :=
```

> Golang tries to keep the code as minimal as required, thus **most of the warnings in other languages are errors in golang**. For Example, If you declare a variable and not use it anywhere, your code would never compile. You will instead get `ERROR: <var_name> declared but not used`
{: class="note-red"}
> All the above code examples would fail to compile if you try to run it as it is. You need to enclose them in `main` code block from [Dear, Hello World](#dear-hello-world) example above. Also, print each variable declared using `fmt.Println(fruit, fruitCount, fruitCost)` so that go can understand that your variable is being used somewhere and not throw any compilation errors.
{: class="note-yellow"}
> You might have noticed the camel casing in golang variable names e.g: `fruitExpensiveCount`, that's the convention followed by go.
{: class="note-yellow"}
## Anyone asked for variety? - Types #1
Even if types are never explicitly declared in python, python do dynamically assign a type to any variable.
```python
# types example in python
type('apple') # <class 'str'>
type(1)       # <class 'int'>
type(1.1)     # <class 'float'>
type(False)   # <class 'bool'>
```

In Golang, there's an array of data types that can be explicitly assigned or a bunch of types that are inferred by the compiler.  
Since there's a lot... here's a handy list,
- [bool - boolean value, e.g: true, false](#bool---boolean-value)
- [int8, int16, int32, int64, int - signed integer types, e.g: -2, -1, 0, 1, 2](#int8-int16-int32-int64-int---signed-integer-types)
- [uint8, uint16, uint32, uint64, uint - unsigned integer types, e.g: 0, 1, 2, 3, 4](#uint8-uint16-uint32-uint64-uint---unsigned-integer-types)
- [float32, float64 - floating point numbers, e.g: 123.456, 1e+8, -2.98e-2](#float32-float64---floating-point-numbers)
- [complex64, complex128 - complex numbers, e.g: 1 + 2i, 1e+8 + -2.98e-2i](#complex64-complex128---complex-numbers)
- [byte, an alias of uint8](#byte-an-alias-of-uint8)
- [rune, an alias of int32](#rune-an-alias-of-int32)
- [string, a collection of bytes](#string-a-collection-of-bytes)

> Also, you might not even require to use all of them in your day-to-day programming so feel free to skim by the material. There's a [tldr](#types-tldr) at the end of this section that summarises the same.
{: class="note-yellow"}

### bool - boolean value
```go
// explicit type assignment
var isAppleCheap bool = false
// with type inference
isBananaCheap := true
```
AND/OR operations can be performed on boolean using `&&` and `||` operators respectively,
```go
// AND operator
fmt.Println(true && true) // returns true
fmt.Println(false && false) // returns false
fmt.Println(true && false) // returns false
// OR operator
fmt.Println(true || true) // returns true
fmt.Println(false || false) // returns false
fmt.Println(true || false) // returns true
```
### int8, int16, int32, int64, int - signed integer types
```go
// explicit type assinment
var minInt8Bit, maxInt8Bit int8 = -128, 127
var minInt16Bit, maxInt16Bit int16 = -32768, 32767
var minInt32Bit, maxInt32Bit int32 = -2147483648, 2147483647
var minInt64Bit, maxInt64Bit int64 = -9223372036854775808, 9223372036854775807
```
`int` is an alias to either `int32` or `int64`, this bit count depends on system type e,g: `int32` on 32bit system and `int64` on 64bit system.
```go
var int32BitOr64Bit int = 12345 // can be either int32 or int64
// above expression can be written with type inference as below
int32BitOr64Bit := 12345
```
This kind of type system might raise some questions. I have few listed below,  
1. Okay, so what would happen if I use any **64 bit variable on a 32 bit system**? Will I lose data?  
ANSWER: **No you don't**, your system would assign two 32 bit registers for a single 64 bit variable. Thus providing support for 64 bits.
2. Can I assign a certain **lower bit variable to higher bit variable**, like `int16` to `int32`?  
ANSWER: **Yes, but it has to be explicitly converted.**
```go
var maxInt16Bit int16 = 32767
var int32Bit int32 = int32(maxInt16Bit)
// since 32767 is within int32 range, conversion works fine 
int32Bit = maxInt16Bit
// golang does not implicitly convert, throws
// ERROR: cannot use maxInt16Bit (type int16) as type int32 in assignment
```
1. So, what would happen if I try to convert **higher bit variable to lower bit variable**, like `int32` to `int16`?  
ANSWER: These type of conversions **can corrupt your data** so try to avoid them.
```go
var int32BitWithMax16Bit int32 = 32767
var int16Bit int16 = int16(int32BitWithMax16Bit)
// since 32767 is within 16 bit range, conversion works fine
var int32BitWithInvalidMax16Bit int32 = 32768
var int16BitInvalid int16 = int16(int32BitWithInvalidMax16Bit)
// 32768 is converted to -32768 and stored in int16BitInvalid
// thus it won't throw an error but will corrupt your data
```  

> Even though a type can be cast to other type using `<type>(<variable_name>)` OR `<type>(<value>)` expression. All conversions don't work, as a thumb rule never try to convert higher bit variable to a lower bit variable. 
{: class="note-yellow"}

### uint8, uint16, uint32, uint64, uint - unsigned integer types
Being unsigned these type values can assign more positive numbers than signed integers
```go
// explicit type assignment
var minUint8Bit, maxUint8Bit uint8 = 0, 255
var minUint16Bit, maxUint16Bit uint16 = 0, 65535
var minUint32Bit, maxUint32Bit uint32 = 0, 4294967295
var minUint64Bit, maxUint64Bit uint64 = 0, 18446744073709551615
```
`uint` is an alias to either `uint32` or `uint64`, this bit count depends on system type e,g: `uint32` on 32bit system and `uint64` on 64bit system.
```go
var uint32BitOr64Bit uint = 12345 // can be either uint32 or uint64
// above expression can be written with type inference as below
uint32BitOr64Bit := 12345
```

### float32, float64 - floating point numbers
There is no `float` type in Go. You have to either use `float32` or `float64`.  

```go
var float32BitPositive, float32BitNegative float32 = 1.233, -2.903
var maxFloat32Bit float32 = 3e+38               // 3(0 times 38).0
var smallestNonzeroFloat32Bit float32 = 1e-45   // 0.(0 times 45)1

var float64BitPositive, float64BitNegative float64 = 1.233, -2.903
var maxFloat64Bit float64 = 1e+308              // 1(0 times 308).0
var smallestNonzeroFloat64Bit float64 = 5e-324  // 0.(0 times 324)5
```  

> Float 'min' and 'max' value given above is not precise to last digit, if you really want to know the value; refer [here](https://stackoverflow.com/questions/45105177/the-maximum-value-for-float64-and-complex128-type-in-go)
{: class="note-yellow"}

> Interested in knowing how floating point values are stored in memory? Refer [here](https://softwareengineering.stackexchange.com/questions/215065/can-anyone-explain-representation-of-float-in-memory).
{:class="note-yellow"}

### complex64, complex128 - complex numbers
Complex values are denoted by real and imaginary parts, explained [here](https://www.mathsisfun.com/numbers/complex-numbers.html).  
In Golang there are 2 versions of complex type, 
1. `complex64` (which has `float32` real part and `float32` imaginary part) and 
2. `complex128` (which has `float64` real part and `float64` imaginary part)

They can be stored in Go as follows,
```go
var complex64BitPositive, complex64BitNegative complex64 = 1.2 + 33i, -2.9 + 0.03i
var maxComplex64Bit complex64 = 3e+38 + 3e+38i               
var smallestNonzeroComplex64Bit complex64 = 1e-45 + 1e-45i   

var complex128BitPositive, complex128BitNegative complex128 = 1.2 + 33i, -2.9 + 0.03i
var maxComplex128Bit complex128 = 1e+308 + 1e+308i           
var smallestNonzeroComplex128Bit complex128 = 5e-324 + 5e-324i
```

### byte, an alias of uint8
In computers, characters like `a` or `@` are converted to byte and stored in memory. A byte is 8 bits long which can store a total of 256 characters (0 to 255). All the characters that fall under this range are called ASCII characters.  
A `byte` (1 byte = 8 bits) in Go is nothing but an alias of `uint8` (8 bit). Then you might think what's the use of `byte`? Well, with respect to Go there's no real difference between the two. Both can be interchangeably used without any issues. It's just a convention that tells a programmer that a particular value is not an `uint8` but a `byte`. 

> Complete ASCII character code list that can be stored in 1 byte is available [here](https://theasciicode.com.ar/)
{: class="note-yellow"}

### rune, an alias of int32
All the characters cannot be assigned within the 256 character codes that `byte` provides, there are values that will occupy more than this space. A 2 byte character example is `ã` and a 3 byte example is `अ`. In Go they can be stored as `rune`.  Again `rune` is nothing but an alias to int32. They are just used to represent a character that is more than a byte long. Similar to a `byte`, `rune` and `int32` can be interchangeably used.

> Complete character code list with [1 byte and 2 byte](https://design215.com/toolbox/ascii-utf8.php) along with [3 byte](https://design215.com/toolbox/utf8-3byte-characters.php) and [4 byte](https://design215.com/toolbox/utf8-4byte-characters.php) are there in the respective list.
{: class="note-yellow"}

### string, a collection of bytes
A `string` is a collection of `byte`. Does that make sense, okay how about this a `string` is a collection of characters... In terms of Go, strings are internally stored as an array of `byte`s we can ponder over it more details once we get to collections.

Meanwhile in python, characters in string can be iterated over as follows,
```python
fruit = "apple"
print(fruit[0]) # will print 'a'
```

This type of operation is possible in Go aswell,  
```go
fruit := "apple"
fmt.Println(fruit[0]) // instead of 'a' it will return 97.
// 97 being the character code of 'a'
fmt.Println(string(fruit[0])) // this will return 'a'
```

> In python, conversions are implicit. Thus when character code `97` is retrieved using `fruit[0]` it is implicitly converted to character `a`. This is not true in Go. **Every conversion in Go has to be done explicitly** (except aliases like `byte` to `uint8` conversion). Thus if you want to get a character you must convert that character code (byte value) to string using `string(fruit[0])`. This might seem verbose, but that's just a practice imposed by Go to maintain code clarity.
{: class="note-red"}

> Also, There is no concept of char data type in Go. A character is always represented by either `byte` or `rune` data type.
{: class="note-yellow"}

### types; tldr
So here's the major takeaway from this section,
1. For all integer type values use `int` and let Go take care of the storage size. Use storage size specific `int8`, `int16`, `int32`, `int64` only when you are keen on saving memory.
2. If you are sure that a value can never become negative, like `appleCount` you may use `uint` instead of `int`. And again, use storage size specific `uint8`, `uint16`, `uint32`, `uint64` only when you are keen on saving memory.
3. If you have a floating point value, you can use `float32` to store the same. `float64` is generally an overkill for most of the tasks, but if you are processing something that require extreme precision it's better to use `float64`.
4. `complex64` and `complex128` are useful in scientific queries where you have to process values in real and imaginary parts. `complex64` is just 2 different `float32` values, each for real and imaginary parts. Similar is the case for `complex128` which is `float64` + `float64`i.
5. `byte` and `rune` are just an alias for `uint8` and `int32` respectively. They are used as a convention to denote characters, since there is no char type in Go.
6. `string` is a just collection of `byte`. 
7. Type conversions in Go has to be done explicitly. So when a character is retrieved from a string as `fruit[0]` it is returned as a byte instead of character. It has to be explicitly converted to string to get back that character - `string(fruit[0])`  
8. With an effort to reduce unwanted code, Go throws an error if an import is not used or a variable is declared and not used. So if your code has unused imports or variables, it will never compile.

## Stubborn variables - Constants
Constants are variables that cannot be changed once assigned. `const` is used instead of `var` for creating a constant.   
In case of variables, when we do this:
```go
var fruitCount = 2      // fruitCount is of type int
var fruitCost = 199.99  // fruitCost is of type float32/float64
```
type inference kicks in and variable type is assigned based on the value to the right side of `=`.  

While in the case of constants, when we do this:
```go
const fruitCountConst = 2      // fruitCount is untyped
const fruitCostConst = 199.99  // fruitCost is untyped
```
every value is **untyped**, meaning `fruitCountConst` and `fruitCostConst` is just a value like `2` or `199.99`.  

<div class="tenor-gif-embed" data-postid="4383019" data-share-method="host" data-width="100%" data-aspect-ratio="1.7777777777777777"><a href="https://tenor.com/view/huh-hu-gif-4383019">Excuse Me? GIF</a> from <a href="https://tenor.com/search/hu-gifs">Hu GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>
That doesn't make sense, does that?  

Let me give a different example,
```go
var intVariable int = 2 
var floatVariable float32 = 2 
var complexVariable complex64 = 2 

fmt.Println(intVariable)      // prints 2 
fmt.Println(floatVariable)    // prints 2.0
fmt.Println(complexVariable)  // prints 2+0i
```
even though `2` was assigned to each variable, the actual variable declared was specific to the variable type and not the value assigned. Same rule applies for any constants. For example,
```go
const untypedConst = 2
var intVariable int = untypedConst
var floatVariable float32 = untypedConst
var complexVariable complex64 = untypedConst

fmt.Println(intVariable)      // prints 2 
fmt.Println(floatVariable)    // prints 2.0
fmt.Println(complexVariable)  // prints 2+0i
```

So just keep in mind **any constant when assigned is untyped during compile time**.

There are other properties of constants in Go as follows,
1. A variable cannot be assigned to a constant,  
```go
intVariable := 2
const intConst = intVariable
// ERROR: const initializer intVariable is not a constant
```
2. Values that are calculated during runtime cannot be assigned to `const` variable,  
```go
package main
import "math"
func main(){
  const squaredValue float32 = math.Sqrt(2)
}
// ERROR: const initializer math.Sqrt(2) is not a constant
```
`math.Sqrt(2)` is a function defined in `math` package and it returns a value that is calculated during runtime, thus cannot be assigned to a constant.
3. Apart from Numeric Constants shown above, **String Constants** and **Boolean Constants** can also be declared that has all the properties of Numeric Constants.
4. It is also possible to declare **typed constants** as shown below,  
```go
const intConst int32 = 32
const floatConst float64 = 64
const stringConst string = "APPLE"
const boolConst bool = false
// below declaration would fail, as it's not possible to 
// declare a const without assignment
const intConstWithoutValue int32
// ERROR: const declaration cannot have type without expression
```
5. `:=` only declares a variable and thus cannot be used to declare constants.

## Apple or Pineapple? - Logic
Finally let's discuss logic.
<div class="tenor-gif-embed" data-postid="10734645" data-share-method="host" data-width="100%" data-aspect-ratio="1.7913669064748199"><a href="https://tenor.com/view/real-housewives-of-new-york-thats-all-iwanted-lying-down-on-the-floor-satisfied-gif-10734645">Finally At Peace GIF</a> from <a href="https://tenor.com/search/realhousewivesofnewyork-gifs">Realhousewivesofnewyork GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>

I know it's been a long article. But we are almost 75% done... bear with me for a few more sections... and Part 2... and 3. 😜 

### if {...} else if {...} else {...}
Python has following construct for defining logic,
```python
# logic in python
if boolean_value == True:
  print("YES, This article is Fun!")
else:
  print("NO, This article is not boring!")
```

Go does it in a similar way but with curly braces,
```go
if booleanValue == true{
  fmt.Println("YES, This article is fun!")
} else {
  fmt.Println("NO, This article is not boring!")
}
```

`else if{...}` block can also be used which is similar to `elif:` in python.
```go
if age < 10 {
  fmt.Println("Hello, Kid!")
} else if age > 60 {
  fmt.Println("Hello, Sir/Madam!")
} else {
  fmt.Println("Hello, Stranger!")
}
```
> `else{...}` and `else if{...}` block must be started on the same line where `if {...}` or `else if{...}`block ends. Other wise Go would automatically insert a `;` and end the previous block, and throw `ERROR: unexpected else, expecting }`
{: class="note-red"}
&nbsp;  
It's also possible to **initialize a variable along with condition**, that is only accessible in the `if{...}`, `else if{...}` and `else{...}` block.  
```go
someInt := 32
if variableDeclaredInIf := 2; someInt > 40{
  privateVariable := 0
  fmt.Println(someInt + variableDeclaredInIf)
} else if variableDeclaredInIf = 1; someInt < 30 {
  // instead of re-assigning a variable a new variable can also be declared
  fmt.Println(someInt + variableDeclaredInIf)
} else {
  fmt.Println(variableDeclaredInIf)
  fmt.Println(privateVariable)  // this will fail
  // ERROR: undefined: privateVariable
}
fmt.Println(variableDefinedInIf)  // this will fail
// ERROR: undefined: variableDefinedInIf
```

### switch{...} 
Python lacks switches which might have forced you to use multiple `if`, `elif` statements in conjunction. Go does include a `switch {...}` that behaves differently than most of the languages.
```go
numericValue := 2
// numericValue is your variable that would be
// evaluated in each case statement
switch numericValue {
  case 1:
      fmt.Println("One")
  case 2:
      fmt.Println("Two")
  case 3:
      fmt.Println("Three")
  default:
      fmt.Println("No Match")
  }
// above code prints Two
```

Above statment is your generic switch statement with `switch <variable> {...}`. If value from the `<variable>` equals any value from the enclosing case statement, in this case `1`, `2` or `3`, it would execute the statement within that matching block. Variable provided to `switch <variable>` could be of any type not just a numeric value. And finally, `default` is similar to your `else` block, if none of the condition matches `default` block will be executed - it is an optional statement.

> In Java and C, a `break` has to be added after every case statement. Otherwise, along with the matching `case` block all the blocks under that is also executed. This is not required in Go, it would exit the case by itself on match.
{: class="note-yellow"}

Switches in Go has a bunch of behaviour that's unique to the language. I have listed them below,
1. Just like `if <declaration>; <condition>` **a switch block can also include a declaration** as,
```go
switch variableOnlyAccessibleInsideSwitch := 0 ; variableToEvaluate { ... }
```
2. **Instead of passing a variable to switch, it can also be empty**. If no variable is provided then all the `case` statements must include a condition (just like an `if` statement). As shown below,
```go
age := 23
switch {
  case age < 10:
        fmt.Println("Hello, Kid!")
  case age > 60:
        fmt.Println("Hello, Sir/Madam!")
  default:
        fmt.Println("Hello, Stranger!")
}
// In above case it's a replacement to a
// long if{...} else if{...} block
```
3. So what if I need to **execute same `case` block for multiple matches**?
```go
letter = "z"
switch letter {
  case "a", "b", "c":
        fmt.Println("You are just starting")
  case "x", "y", "z":
        fmt.Println("You have finished")
  default:
        fmt.Println("You are somewhere in the middle")
}
// will print, You have finished
```
4. What if I want the behaviour back from Java / C, **not break out of case but continue execution**?
```go
numericValue := 1   // should match the first case block
switch numericValue {
  case 1:
        fmt.Println("One")
        fallthrough
  case 2:
        fmt.Println("Two")
  case 3:
        fmt.Println("Three")
  default:
        fmt.Println("No Match")
  }
// One
// Two
```
`fallthrough` is a special keyword that allows a case statement to go ahead and executes the immediate next case block and not break on match.

## Eat. Sleep. Repeat. - Loops
<div class="tenor-gif-embed" data-postid="5894655" data-share-method="host" data-width="100%" data-aspect-ratio="1.7777777777777777"><a href="https://tenor.com/view/rollercoaster-infinite-loop-loop-looping-amusement-gif-5894655">Infinite Loop - Rollercoaster GIF</a> from <a href="https://tenor.com/search/rollercoaster-gifs">Rollercoaster GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>
&nbsp;  
Loops in python are one of the best thing that language offers. With simple yet effective syntax, it eliminates most of the bloated code from other languages. With Go you are in the control of code complexity. You can write your for loops as verbose as Java or as straightforward as Python.
```go
for i := 1; i <= 10; i++ {
    fmt.Println(i)
} // prints 1 to 10
```
Above is the verbose version, where all three parts of `for` - `<declaration>; <condition>; <post-statement>` has been defined. Here, `<declaration>` declares and initializes any new variale that's only accessible within the `for` block. `<condition>` is evaluated at the end of every loop, if it is evaluated to be `false` loop exits. `<post-statement>` is executed at the end of every loop, just before `<condition>` is evaluated. 

What if you want to initialize multiple variables or say execute multiple post-statement?  
```go
// multi varable declaration & multi post-statements
for i, j := 1, 10; i <= 10; i,j = i+1, j-1 {
     fmt.Println(i+j)
} // prints 11, ten times
```

Yes, that did complicate the statement. Now let's cut things out.
1. Without `<post-statement>`
```go
// leave a ; at the end
for i, j := 1, 10; i <= 10; {
     fmt.Println(i+j)
     i,j = i+1, j-1
} // prints 11, ten times
``` 
2. Without `<declaration>`
```go
// leave a ; at the start
i, j := 1, 10
for ; i <= 10; i,j = i+1, j-1 {
     fmt.Println(i+j)
} // prints 11, ten times
```
3. With `<condition>` only, i.e: without `<declaration>` and `<post-statement>`
```go
i, j := 1, 10
// no ; required
for i <= 10 {
    fmt.Println(i+j)
    i,j = i+1, j-1
} // prints 11, ten times
```
4. Infinite loop?
```go
i, j := 1, 10
for {
  fmt.Println(i+j)
  i,j = i+1, j-1
  if i > 10 {
        break
  }
}
```

> There are no `while` loops in Go. Since it's possible to use `for` with just a `<condition>`, this effectively replaces `while` loop in Go.
{: class="note-yellow"}


### Range
Go does have a `range` keyword which is helpful in iterating over collections. This is different from the `range()` function that you might be used to with python. We will get back to this keyword once we learn more advanced types like maps and slices. For now here's a simple implementation to iterate over any string,
```go
alphabets := "abcdefg"
// range keyword returns 2 values, which is assigned to
// i = iteration count
// character = each character in string
for i, character := range name {
  fmt.Println(i, string(character))
}
// 0 a to 6 g will be printed in new line
```

## Reduce code footprint - Functions
Functions in Go has certain distinct features. 
```go
// here's a function we have been using since the start
func main() {...}
```
From the syntax it should be evident that `func` keyword creates a function followed by `<function-name>` and curly braces `{...}` that encloses the code block.  

Some variations and possibilities with respect to functions in Go,
1. Functions **with arguments** (input to any function),
```go
// function declaration
func printSum(a int, b int) {
    fmt.Println(a + b)
}
func main(){
    // function call
    printSum(1,2)
}
```
Yes, even for function arguments, `<type>` comes after `<name>`.  
Since **both arguments are of same `<type>`,** that is `int`, we can shorthand it to,  
```go
func printSum(a, b int) {...}
```
2. Functions with **return values** (output from a function)
```go
func getSum(a, b int) int {
    return (a + b)
}
func main(){
    // function call
    sumVal := getSum(1,2)
}
```  
3. Function with **multiple return values**. YES, that's a thing in Go!
```go
func getSumAndDifference(a, b int) (int, int) {
    return (a + b), (a - b)
}
func main(){
    // function call
    sumVal, diffVal := getSumAndDifference(1,2)
}
```

4. Named return values
```go
// sumVal and diffVal will be returned automatically
func getSumAndDifference(a, b int) (sumVal int, diffVal int) {
    sumVal, diffVal = a + b, a - b
    return
    // empty return statement must be used with named returns
}
func main(){
    // function call
    sumVal, diffVal := getSumAndDifference(1,2)
    fmt.Println(sumVal, diffVal)
}
```
Since both named returns are of type int, we can shorthand it
```go
func getSumAndDifference(a, b int) (sumVal, diffVal int) {...}
```

> Multi return statements are useful in situations where more than one value might be required. But, often in some usecases we might just need a single return value out of many that a function returns. Like suppose in the above example we just needed difference and and not the sum. In such cases, you can use blank identifiers - `_, diffVal := getSumAndDifference(1,2)`. Thus even if sumVal is returned it will thrown out and not saved in memory.
{: class="note-red"}  
&nbsp;  
**Aaaand, that concludes this part!**

That's a lot to learn in a stretch! Go take a coffee break or something.
<div class="tenor-gif-embed" data-postid="10692456" data-share-method="host" data-width="100%" data-aspect-ratio="2.5025125628140703"><a href="https://tenor.com/view/you-deserve-iit-worth-win-thanks-welcome-gif-10692456">You Deserve IIt Worth GIF</a> from <a href="https://tenor.com/search/youdeserveiit-gifs">Youdeserveiit GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>
&nbsp;  
Back already?

Now you have got options...  
1. Read the [BONUS](#bonus) material.
2. Solve [EXERCISE](#exercise) and become a Golang NERD!
<!-- 3. Move ahead with Second Part (or if you are early and it's not published yet, revise this one again) -->

## BONUS
This section includes topics that has been categorized as *good to know*. You may go ahead and read this if you want to know like what functionalities does `go` command provide or who is the mascot of Golang!
### Golang Toolset
Go along with compiling your code provides and array of different features that are quite useful in day-to-day programming scenarios. Complete featureset of go command can be found [here](https://golang.org/cmd/go/) I have listed some useful ones below for easy reference,
1. `go help <command>` -  return details of any specific subcommand
2. `go build` - will provide a compiled binary and place it in the directory this command was triggered in. Refer ["Dear, Hello World"](#dear-hello-world)
3. `go run` - will compile to a binary, save it in a temporary location and run the application
4. `go env` - will list all the environment variables that is used by Go.  
```bash
go env # will display all environmet variables
# set GOARCH=amd64
# set GOBIN=C:\Users\gauthamchettiar\go\bin
# set GOENV=C:\Users\gauthamchettiar\AppData\Roaming\go\env     
# set GOPATH=C:\Users\gauthamchettiar\go
# set GOROOT=c:\go
# ... has been truncated to save space
go env GOBIN # will display only the passed env variable
go env -u GOBIN # will unset that env variable
go env -W GOBIN=C:\Users\gauthamchettiar\go\bin # will set the env variable
```
4. `go install` - apart from generating your build in you current directory, it's also possible to generate it in a designated folder where all binaries should go. As name suggests, this can be used to install any application, if you set your path in your system's executables - you should pretty much have a running command. You can refer [this](https://www.digitalocean.com/community/tutorials/how-to-build-and-install-go-programs#installing-go-programs-with-go-install) article make `go install` to work correctly.
5. `go fmt` - this command will automaticall format your code to make it more legible - super useful!
6. `go vet` - without compiling your code, will printout any errors in your code that can lead to compilation errors.

### Gopher
We have a derpy little mascot for Golang,  
![GOPHER](https://blog.golang.org/gopher/header.jpg)  

He is called **Gopher** and was originally drawn by [Renee French](http://reneefrench.blogspot.com/).  
Since then it has seen several redraws like these:  
[https://github.com/ashleymcnamara/gophers](https://github.com/ashleymcnamara/gophers)  
[https://github.com/egonelbre/gophers](https://github.com/egonelbre/gophers)  
[https://github.com/MariaLetta/free-gophers-pack](https://github.com/MariaLetta/free-gophers-pack)


## EXERCISE
Before we start with the exercise there's one more thing that I would like to provide for reference, i.e: **how to take user input?**
```go
package main
// multiple imports can be clubbed together as below
import (
    "fmt"
    "bufio"
    "os"
)
func main(){
    // io reader has to be created 
    reader := bufio.NewReader(os.Stdin)
    // here's your prompt
    fmt.Print("Enter your name : ")
    // below statement would return user entered text
    // this would wait for '\n' to exit - newline OR enter
    text, _ := reader.ReadString('\n')
    // print your returned text
    fmt.Println("Hello",text)
}
```
Do mind that, there's more than one way to accept input but this one's the most efficient.

**Some Instructions / Good practices to follow:**
1. Comment the heck out of it! (at this point it's okay to comment as much as possible to make it easier for your future self to understand).
2. Give meaningful names to functions and variables that you would be creating, let it be as long as needed.
3. Exercise will have a skeleton code attached that can be used to get started with.
4. Don't be too harsh on yourself. If something doesn't seem to work, GOOGLE! Still puzzled? You can always contact me!

**And finally, here is your exercise,**  
Create a calculator program that, (a) asks for [operation type] and [operand count]. (b) Then depending on [operand count] asks for [actual operands]. (c) Performs the user requested [operation type] on the [actual operands] and returns the [result]. *Operations can be (+, -, * and /)*
```go
// Sample output below,
// What operation would you like to perform? +
// How many number of operands do you have? 3
// Input operand 1 : 1
// Input operand 2 : 2
// Input operand 3 : 3
// Result : 6
```
```go
// calculator app: code skeleton
package main

import (
  "bufio"
  "fmt"
  "os"
  "strconv"
)

func takeIntegerInput(displayString string) int {
  text := takeStringInput(displayString)
  // below function converts string to integer
  intVal, _ := strconv.Atoi(text)
  return intVal
}

func takeStringInput(displayString string) string {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print(displayString)
  text, _ := reader.ReadString('\n')
  return text
}

func main(){

}
```

That truely concludes Part 1 of the series.

I would love your feedback, find my details at the bottom of this page and feel free to contact me anytime!

And, Thank you for reading through so patiently. ❤️