# Lecture 11, February 28th, 2023

## In-class Errata / Additional Discussion


We started off class talking about ChatGPT and how using services and tools like this can be extremely useful but that we need to be able to be critical about the results that come back from a generative AI service like ChatGPT.  We need to learn how to ask questions that don't give us too much information, for example, to ask a question like "Can you give me an outline of the steps needed to accomplish task X **without providing any code solutions**?"  That is an acceptable use of the technnology in a classroom and academic learning situation. Asing ChatGPT or another generative AI platform to _solve_ your problems is not. 

---

We then had some good discussions about our Poll Everywhere questions.  [Q1.py](Q1.py) asked about how many times a loop would execute. Everyone answered either 11 or 12 based on the code, which was expected. When trying to determine how many times a counter-controlled loop will execute, just make sure to look at the initial value, the final value for testing, and the operator being used to test fo the final value.  In the Q1 example, the initial value was 0, the test was `x <= 11` and the modifcation was `x += 1`.  So it runs from 0 through 11, inclusive, which is 12 times.

----

Regarding [Q2.py](Q2.py), we talked about how this loop would be an infinite loop.  Theoretically, this is true, as integers don't really have an upper or lower limit.  Utilizing ChatGPT, it came back with this response about integer values:

> In Python, integer values do not overflow or underflow because they are implemented as "unlimited precision" integers, which means they can represent integers of arbitrary size. This is in contrast to many other programming languages, where integers have a fixed size and can overflow or underflow if the result of an arithmetic operation exceeds the maximum or minimum representable value.

> Python's implementation of integers is achieved using a technique called "bignum arithmetic," which allows the program to dynamically allocate memory as needed to represent integers of arbitrary size. This means that you can perform arithmetic operations on very large integers without worrying about overflow or underflow errors.

That's great, but there *is* a practical limit to how big an integer can be, however, and that is limited by the amount of memory the system has. So eventually, our code in [Q2.py](Q2.py) would encounter what is known as "underflow", which means that it would reach the smallest number it could possibly store on the system it's running on and then the  number would either roll around mathematically to the largest number the system could store (thus making the loop fail) or it would become a NaN (Not a Number) value, which would likely also cause the loop to exit.

Underflow/overflow _does_ occur with floating point numbers in Python.  Run this code in Thonny to test it that I culled from [https://stackoverflow.com/questions/52151647/integer-overflow-in-python3](https://stackoverflow.com/questions/52151647/integer-overflow-in-python3) and [this brief explanation at python.org](https://docs.python.org/3/library/exceptions.html#OverflowError):

```python
import sys

i = sys.maxsize
print(i)
# 9223372036854775807
print(i == i + 1)
# False
i += 1
print(i)
# 9223372036854775808

f = sys.float_info.max
print(f)
# 1.7976931348623157e+308
print(f == f + 1)
# True
f += 1
print(f)
# 1.7976931348623157e+308
```

----

We discussed what good sentinel values are for [Q3.py](Q3.py). Because the question asked about numeric input for quilt squares, the best option is an impossible integer value size for quilt squares:

```python
size = int(input("enter quilt square size: "))

while size >= 0:
    total += size
    size = int(input("enter quilt square size: "))
```

But arguments _could_ be made for the word `done` or `q` if you did the numeric casting inside the loop:

```python
size = input("enter quilt square size: ")

while size != "done":
    total += int(size)
    size = int(input("enter quilt square size: "))
```

The only problem with this is if you allow textual input and you try to cast it as an integer inside the loop, without proper precautions (which we don't have yet) the code will crash.  So if someone entered `seventeen`, the code would crash trying to cast it with `int()`.

-----

Then in [Q4.py](Q4.py) and [Q5.py](Q5.py) we looked at sentinel-controlled loops that had the same input but produced different results. Q4.py had the correct code, which has the structure of:

* prime the loop with initial value for loop control variable
* while the loop control value hasn't been entered:
	* process the value in whatever fashion makes sense
	* read another value for the loop control variable and then end the loop, to go back to test again.

In Q5, the order of statements inside the loop were reversed, which means that if you enter the loop with a valid value, you immediately throw it away because you read a new value. Then you process that value without testing it for validity and _then_ end the loop and test again.

Sentinel-controlled loops, in general, operate on the principle of entering good data and then processing it and continuing to enter data until a bad value is entered:

```python
total = 0
grade = int(input("Enter a grade to process: "))

while grade >= 0:
    total += grade
    grade = int(input("Enter a grade to process: "))

print("The total of all grades is:", total)
```

Data validation loops, a subset of sentinel-controlled loops, work on the opposite premise: the loop continues while you keep entering bad values. The value that allows you to exit the data validation loop will be a _good_ value.

```python
weight = float(input("Enter a weight greater than 0: "))

while weight <= 0:
    weight = float(input("Enter a weight greater than 0: "))

print("The weight you entered, which is definitely bigger than 0, is:", weight) 
```

----

## Music played at the beginning of class

* [Midnight on the Interstate](https://www.youtube.com/watch?v=6_6M_6KStEw) by Trampled by Turtles
* [Song Up In Her Head](https://www.youtube.com/watch?v=kdM89_88cdM) by Sarah Jarosz
* [Something in the Orange](https://www.youtube.com/watch?v=lA8F9sIhGdg) by Zach Bryan
* [The Lion The Beast The Beat](https://www.youtube.com/watch?v=Ov8uT8DTvlw) by Grace Potter & The Nocturnals

## The topics for this lecture were:

* Loop body
* Iteration
* while condition: 
	- statement1
	- statement2

## The highlighted topics for this lecture were

* while loop
* Loop body
* Iteration

* Counter-controlled loop
* Sentinel-controlled loop
* Sentinel value

* Infinite loop
* Pre-test loop

* Requirements for looping:

	1. Loop Control Variable (LCV)
	2. Initial value for the LCV
	3. Modification of the LCV
	4. Test for the final value of the LCV
