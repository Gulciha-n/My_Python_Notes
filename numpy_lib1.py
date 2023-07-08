
import numpy as np

list1 = [1,2,3,4,5,6]

array1 = np.array(list1)

print(array1)




list2 =[[1,2,3],[4,5,6]]

array2 = np.array(list2)

print(list2)

print(array2.dtype)




array3 = np.zeros(6)
array4 = np.ones(6)
array5 = np.ones((3,2))
array6 = np.ones((2,2,3))
print(array3)
print(array4)
print(array5)
print(array6)

