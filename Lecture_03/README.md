# Lecture 03, Tuesday, January 31st, 2023

## Summary

Today's lecture was all about looking at basic output and basic input. This summary is not comprehensive of all of the topics covered in the book or lecture, but is meant to be representative of the highlights of discussions that took place.

Basic output is accompished with the `print()` function.

By default, the `print()` statement will print a newline at the end of whatever the statement is printing, which means that the next print statement would start it's content at the beginning of a new line.

This behavior can be changed by using the `end=""` parameter for the print statement which changes the last output of the print statement to whatever the `end` parameter is.

For example, the following two statements are identical:

```python
print("Hello world!")
print("Hello world!", end="\n")
```

If the `end` parameter is omitted, then it defaults to a newline escape sequence (`\n`).  Usually, at least in CS1, the `end` parameter is either an empty string or a space to keep the output on the same line:

```python
print("Hello", end=" ")
print("world!")

# identical output below; notice where the space is ... inside the string
# literal instead of in the end parameter:
print("Hello ", end="")
print("world!")
```

The `end` parameter can also be used to put *anything* at the end of a line, such as ... ellipses.

```python
print("Hello", end="...")
print("world!")

# this code would print:   Hello...world!
```

We also talked about basic input using the `input()` function.  Without a parameter (something inside the parentheses), the `input()` function just waits for the user of the program to type some input. With a parameter (a string), the string is used as a prompt to tell the user what to enter.

The results of an `input()` function call need to be stored into a variable so that the value can be used later in the program.

```python
# no prompt, store the result of the input into variable my_value
my_value = input()
print("You entered:", my_value)

# this time a prompt, store the result of the input into variable my_other
my_other = input("Please enter something:")
print("You entered:", my_other)
```

All input, by default, is textual or string data. If you need a value to be processed arithmetically later in your program as a number, you need to cast the input to the appropriate data type. To convert textual input to an integer, whole number value, use the `int()` function:

```python
my_age = int(input("Please enter your age:"))
print("You are", age, "years old.")

# because my_age is a number, you can do basic math with it, like this
print("In 10 years, you will be", age + 10, "years old.")
```

If you attempt to do arithmetic with a value read from the user that hasn't been converted to an integer or other type of number, you will receive a TypeError:

```python
# the "number" is read as a string because that's what input() does
my_number = input("Enter a number please:")

# the statement below will fail because Python doesn't know how to operate
# with a string on the lefthand side of the addition operator and an integer
# on the righthand side
print(my_number + 6)
```

## Music played at the beginning of classes so far (first three classes)

* [Almost (Sweet Music)](https://www.youtube.com/watch?v=JJ9IX4zgyLs) by Hozier
* [Hey Scenesters!](https://www.youtube.com/watch?v=0QpkuxPJ-8A) by The Cribs
* [Virtual Insanity](https://www.youtube.com/watch?v=OeTFAiYbR9o) by Jamiroquai
* [Do Your Worst](https://www.youtube.com/watch?v=Vx60Fsu-w9M) by Rival Sons
* [Fantasy](https://www.youtube.com/watch?v=DE5DXUfX0cc) by MS MR
* [Some Of Us Are Brave](https://www.youtube.com/watch?v=GC5UBAoa6nw) by Danielle Ponder
* [Main Title/Rebel Blockade Runner](https://www.youtube.com/watch?v=v3_Dopwe1Ls) by John Williams
* [Virginia (Wind in the Night)](https://www.youtube.com/watch?v=6LS4oKobHp0) by The Head and the Heart
* [I Dare You](https://www.youtube.com/watch?v=WOgQpjARYyc) by The Regrettes
* [FREEDOM](https://www.youtube.com/watch?v=3YHVC1DcHmo) by Jon Batiste
* [Sleep to Dream](https://www.youtube.com/watch?v=L9Wnh0V4HMM) by Fiona Apple

## The topics for this lecture:

* Basic Output
  - `print()`
  - Basic outputting options
* Basic Input
  - `input()`
  - Input types and prompts
* Errors
  - 3 main types of errors
  - Detecting Errors practice

## The highlighted topics for this lecture:

* `print()`
* String literal
* `print("A",2)`
* `print("Hello", end=" ")`
* Newline character `\n`
* whitespace
* `input()`
* `input("prompt")`
* String input
* Data type
* `int()`
* Syntax error
* Runtime error
* Logic error
* Bug
* Crash
z