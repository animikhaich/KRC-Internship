######################################################
## Internship @ KRC: DAY 4                          ##
## ANIMIKH AICH                                     ##
## RNS Institute of Technology, Bengaluru, India    ##
######################################################

## NUMPY BASICS
import numpy as np
# Declare a Numpy Array
print('Declaration of the array: ')
array = np.array ([[1,2,3,4],[5,2,2,3],[7,3,9,1]])


# Print the array
print(array)

# Finding Out the Item size of each Item of the arrary
print('Size of each item of the array: ', end='')
item_size = array.itemsize
print(item_size)

print('Shape of Array: ', array.shape)

# Resizing the Array
print('Reshaped Array: ')
array = array.reshape(6,2)
print(array)

# Using dtype argument
print('Redeclaring the same array with float64 dtype. float64 takes 8 bytes of space: ')
array = np.array ([[1,2,3,4],[5,2,2,3],[7,3,9,1]], dtype='float64')
print(array)
print('Item size: ', array.itemsize)

# An empty arrary
empty_array = np.empty((2,3))
print('Empty Array: \n', empty_array)

# Ones and Zeros
print('Ones: \n', np.ones((2,3), dtype = 'int'))
print('zeros: \n', np.zeros((2,3)))

# Transpose
print('Transpose of the arrary:\n ', array.transpose())

# Range
array = np.arange(10, 50, 3)
print('Range of array b/w 10 and 50 in steps of 3:\n',array)

# Random
array = np.random.randn(2,3)
print('Random numbers 2,3 array:\n',array)

# Array Operations
a = np.array([10,20,30,40,50])
b = np.arange(1,6)

print('Array a:', a)
print('Array b:', b)

c = a - b
print('The array subtraction is: ', c)

c = a + b
print('The array Addition is: ', c)

c = a * b
print('The array Miltiplication is: ', c)

c = a / b
print('The array Division is: ', c)

c = b**5
print('b raised to the power 5: ', c)

c = a<40
print('Array boolean comparison: ', c)

c = a.dot(b)
print('Finding the dot product: ', c)

c = np.dot(a,b)
print('Alternative method for dot product: ', c)

c = np.sqrt(a)
print('Square Root of array a:', c)
