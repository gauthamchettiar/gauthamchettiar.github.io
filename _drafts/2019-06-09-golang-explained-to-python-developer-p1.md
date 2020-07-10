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
  - [Bonus - Golang Tools](#bonus---golang-toolchain)
  - [Bonus - Golang vs Java](#bonus---golang-vs-java)
  - [Exercise](#exercise)
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
1. Do I always have to pass variable type, is **type inferrence** not a thing in Go?
```go
// If you are assigning a variable during declaration
// below syntax works fine, due to type inferrence
var fruit = "apple"
var fruitCount = 2
var fruitCost = 199.99
```
2. What if I want to declare **multiple variables in a single line**, is there a shortcut?
```go
// both must be of same type, since type is explicitly passed
var fruitExpensive, fruitCheap string = "apple", "banana"
// if no type is passed, different types of variable can be assigned
// in a single line, due to type inferrence
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

> Also, you might not even require to use all of them in your day-to-day programming so feel free to skim by the material. There's a [tldr](#types-tldr) at the end that summarises the same.
{: class="note-yellow"}

### bool - boolean value
```go
// explicit type assignment
var isAppleCheap bool = false
// with type inferrence
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
// above expression can be written with type inferrence as below
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
// above expression can be written with type inferrence as below
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
A byte (1 byte = 8 bits) in Go is nothing but an alias of uint8 (8 bit). Then you might think what's the use of byte? Well, with respect to Go there's no real difference between the two. Both can be interchanged and used without any issues. It's just a convention that tells a programmer that a particular value is not an `uint8` but a `byte`. 

> Complete ASCII character code list that can be stored in 1 byte is available [here](https://theasciicode.com.ar/)
{: class="note-yellow"}

### rune, an alias of int32
All the characters cannot be assigned within the 256 character codes that `byte` provides, there are values that will occupy more than this space. A 2 byte character example is `ã` and a 3 byte example is `अ`. In Go they can be stored as `rune`.  Again `rune` is nothing but an alias to int32. They are just used to represent a character that is more than a byte long. Similar to a byte, `rune` and `int32` can be interchanged and used.

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
So here's the major out takes of the types in go,
1. For all integer type values use `int` and let Go take care of the storage size. Use storage size specific `int8`, `int16`, `int32`, `int64` only when you are keen on saving memory.
2. If you are sure that a value can never become negative, like `appleCount` you may use `uint` instead of `int`. And again, use storage size specific `uint8`, `uint16`, `uint32`, `uint64` only when you are keen on saving memory.
3. If you have a floating point value, you can use `float32` to store the same. `float64` is generally an overkill for most of the tasks, but if you are processing something that require extreme precision it's better to use `float64`.
4. `complex64` and `complex128` are useful in scientific queries where you have to process values in real and imaginary parts. `complex64` is just 2 different `float32` values, each for real and imaginary parts. Similar is the case for `complex128` which is `float64` + `float64`i.
5. `byte` and `rune` are just an alias for `uint8` and `int32` respectively. They are used as a convention to denote characters, since there is no char type in Go.
6. `string` is a just collection of `byte`. 
7. Type conversions in Go has to be done explicitly. So when a character is retrieved from a string as `fruit[0]` it is returned as a byte instead of character. It has to be explicitly converted to string to get back that character - `string(fruit[0])`  
8. With an effort to reduce unwanted code, Go throws an error if an import is not used or a variable is declared and not used. So if your code has unused imports or variables, it will never compile.

## Stubborn variables - Constants
Constants are variables that cannot be changed once assigned. Constants in Go is slightly different other languages. `const` is used instead of `var` for creating a constant.   
In case of variables, when we do this:
```go
var fruitCount = 2      // fruitCount is of type int
var fruitCost = 199.99  // fruitCost is of type float32/float64
```
type inferrence kicks in and variable type is assigned based on the value assigned.  

While in the case of constants, when we do this:
```go
const fruitCountConst = 2      // fruitCount is untyped
const fruitCostConst = 199.99  // fruitCost is untyped
```
every value is **untyped**, meaning `fruitCountConst` and `fruitCostConst` is just a value like `2` or `199.99`.  

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
even though `2` was assigned to each variable, the actual variable declared was specific to the variable type and not the value assigned. Same rule applies for any constants.

Consider below example,
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

## Eat. Sleep. Repeat. - Loops

## Reduce code footprint - Functions

&nbsp;  
That's a lot to learn in a stretch! Go take a coffee break or something,
<div class="tenor-gif-embed" data-postid="10692456" data-share-method="host" data-width="100%" data-aspect-ratio="2.5025125628140703"><a href="https://tenor.com/view/you-deserve-iit-worth-win-thanks-welcome-gif-10692456">You Deserve IIt Worth GIF</a> from <a href="https://tenor.com/search/youdeserveiit-gifs">Youdeserveiit GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>

## BONUS - Golang Toolset

## BONUS - Golang vs Java | Part 1

## EXERCISE

## Wait, there's more variety! - Types #2

## Is it a class? Is it an object? - It's Struct!

## The todo list - Interface

## It wasn't me, he did it! - Pointers

## To Err is Huuan- Error Handling

## I will do it later - Defer
