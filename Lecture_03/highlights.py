# code written during the highlights section of class

# some basic output
print("Hello world!")
print('Hello world!')
print("A")
print(3)

# output with end
print("Hi, my name is", end=" ")
print("Marvin")

print("Hi, my name is", end="...")
print("Marvin")

# output with newlines embedded
print("A\nB\nC\nD")

# here we start doing input
#name = input()
x = 12

#print(name)
print(x)

#my_name = input("Enter your name: ")

# read a number, convert to an integer num
number = int(input("Fave number? "))
print("Your favorite number is", number)

double = number * 2
print("Double your fave is", double)

# runtime error: can't divide by 0
print(double/0)
