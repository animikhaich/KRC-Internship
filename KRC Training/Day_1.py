#Transpose a matrix in a Single line in Python

##Using Numpy
import numpy
matrix=[[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))

#Partial Functions

##Example 1
from functools import partial

def f(a, b, c, x):  # A normal function
    return 1000 * a + 100 * b + 10 * c + x

# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
print(g(5))

##Example 2
from functools import *


# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c


# A partial function with b = 1 and c = 2
add_part = partial(add, c=2, b=1)

# Calling partial function
print(add_part(3))

#Packing and Unpacking

##Unpacking
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)
# Driver Code
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)

##Packing
def myFunc(*someargs):
    sum = 0
    for i in someargs:
        sum = sum + i
    return sum

print(myFunc(2,3,4,5,4,3,2))

#Ternary Operator
a = 10
b = 20
print( (b, a) [a < b] )

#Loops
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print (d)

# Python code to demonstrate working of
# center(), ljust() and rjust()
str = "geeksforgeeks"

# Printing the string after centering with '-'
print(str.center(20, '-'))

# Printing the string after ljust()
print(str.ljust(20, '-'))

# Printing the string after rjust()
print(str.rjust(20, '-'))

