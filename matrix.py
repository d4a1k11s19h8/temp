import numpy
x=numpy.array([[2,1,1],
               [3,2,1],
               [2,1,2]])
print(dir(numpy))

'''to copy a matrix'''
y=x.copy()

'''for taking the traspose'''
y=x.transpose()

'''for multiplying corresponding elements of an array'''
print(numpy.multiply(x,y))

'''for matrix multiplication can use any of 2'''
print(numpy.matmul(x,y),x.dot(y))

#x.reshape(9,1)
y=numpy.linalg.inv(x)
print(numpy.matmul(x,y),numpy.__version__)
print(type(y))
'''<array>.ndim for knowing the dimension of array'''
x=numpy.array(42);print(x.ndim) # 0dimension
x=numpy.array([1,2,3,4,5,6]);print(x.ndim)# 1dimension
x=numpy.array([[1,2,3],[4,5,6]]);print(x.ndim)# 2dimension(matrix)
x=numpy.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]);print(x.ndim)# 3dimension

x=numpy.array([1,2,3],ndmin=3) # to create an array of required dimension
print(x);print(x.ndim)

'''
numpy.mat.  is for matrix application'''


x=numpy.array([[2,1,1],
               [3,2,1],
               [2,1,2]])
'''indexing in array
to add element of row-2,col-3 and row-1,col-3'''
print(x[1][2]+x[0][2]) #or
print(x[1,2]+x[0,2])
# -ve indexing print the last element from the 2nd dim:
# x[1, -1]
'''
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
from the second element,slice elements from index 1
to index 4 (not included)
print(arr[1, 1:4])

From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
'''
print(x.dtype)
'''data types in numpy
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
NumPy array object has a property called dtype that
returns the data type of the array

arr = np.array([1, 2, 3, 4], dtype='i4')
arr = np.array([1, 2, 3, 4], dtype='S')
newarr = arr.astype('i')
to change the data type of an existing array,
is to make a copy of the array with the astype() method.'''

'''to delete an element from array when index is given'''
print(numpy.delete(x,5 #<index>
                   ),x)

# dtype is not required argument
print(numpy.zeros((3,3))) # this gives 0. as all the elements
print(numpy.zeros((3,3),dtype='i'))# this gives 0 as all the elements

'''to create a void matrix it takes binary object
encode() func makes an object in binary lang'''
x1=numpy.void((str(3).encode(),str(3).encode()))

'''to print average of all the numbers'''
print(numpy.average(x))

'''to know the size of an array'''
print(numpy.size(x))

'''to split the array in no of divisions'''
print(numpy.split(x,3))

'''to add two arrays can use any of 2'''
print(numpy.add(x,y),x+y)

'''to add two arrays and change the datatype''' 
print(numpy.array(numpy.add(x,y),dtype='i'))
print(numpy.array(numpy.add(x,y),dtype=numpy.int32))


print(numpy.append(x,[1,2,3]))

'''to change the size of an array'''
x.resize(9,1)
print(x)


'''using numpy.arange(a,b,c) for creating an array
where a,b,c has usual meaning as in range() func

reshape changes the size of an array
'''
print(numpy.arange(1,25,2))
print(numpy.arange(12).reshape(3,4))

print(numpy.conjugate(y),y)

