######################################################
## Internship @ KRC: DAY 5                          ##
## ANIMIKH AICH                                     ##
## RNS Institute of Technology, Bengaluru, India    ##
######################################################

## NUMPY BASICS
import numpy as np
# Declare a Numpy Array
print('Declaration of the array: ')
array = np.arange(10)**3


# Print the array
print(array)

# Indexing, Slicing an array
print('3rd element in the array: ', array[2])

print('A part of the array: ',array[1:5] )

print('A part of the array with a gap of 2 elements: ',array[1:6:2] )

print('A part of the array in reverse: ',array[6:1:-1] )

print('The entre array in reverse: ', array[::-1])

print('The entre array in reverse with gap of 3 elements: ', array[::-3])

print('Each element of the array: ')
for i in array:
    print(i**(1/3))


def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)

print('New array declared from function: ',b)

print('Element 2,3 of b: ', b[2,3])

print('Each row in the second column of b: ', b[0:5,1])

print('Equivalent to the previous example: ',b[:,1] )

print('Each column in the second and third row of b: ', b[1:3,:])

print('Last row from bottom: ',b[-1])


c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])

print('New 3D array c: ', c)

print('Find the shape of C: ', c.shape)

print('Same as c[1,:,:] or c[1]: ', c[1,...])

print('Same as c[:,:,2]: ', c[...,2])

print('Printing rows in B')
for row in b:
    print(row)

print('Printing elements in B in a new line each')
for element in b.flat:
    print(element)

print('Return a Flattened array: ', c.ravel())


a = np.floor(10*np.random.random((2,2)))
print('New Array:\n ', a)

b = np.floor(10*np.random.random((2,2)))
print('New Array:\n ', b)

c = np.vstack((a,b))
d = np.hstack((a,b))

print('Horizontal stacking of a & b: \n', d)
print('Vertical stacking of a & b: \n', c)

from numpy import newaxis
print('Using NewAxis')
print('Similar to Previous one, Stacking coumn wise:\n',np.column_stack((a,b)))   # With 2D arrays

a = np.array([4.,2.])
b = np.array([2.,8.])
print('Make a as a 2D column Vector:\n',a[:,newaxis])  # This allows to have a 2D columns vector

print('2D Column vector for both a and b:\n',np.column_stack((a[:,newaxis],b[:,newaxis])))
print('2D Column vector for both a and b but vertical stack:\n',np.vstack((a[:,newaxis],b[:,newaxis])))


# Splitting Arrays
print('Splitting Arrays:')
a = np.floor(10*np.random.random((2,12)))

print('New Array:\n', a)

print('Split into 3 seperate arrays: \n',np.hsplit(a,3))   # Split a into 3

print('Split from 3rd and 4th Column:\n',np.hsplit(a,(3,4)))


