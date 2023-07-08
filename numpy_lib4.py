import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10])

print(array1)
print(array1.shape)  #dimension of array
print(array1.ndim)   #number of dimension
print(array1.dtype)  #data type of array
print(array1.size)   #size of array

#reshape : change number of dimension
array2 = array1.reshape(5,2)
print(array2)
print(array2[0])
print(array2[0][1])



array3 = np.array([[1,2,3]])
print(array3)
print(array3.shape)  #dimension of array
print(array3.ndim)   #number of dimension
print(array3.dtype)  #data type of array
print(array3.size)   #size of array





