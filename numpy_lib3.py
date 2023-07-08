import numpy as np

array1 = np.arange(10)
print(array1)

print(array1[3])     #index
print(array1[3:7])


array1[1:3]=12     # data assignment 
print(array1)


array2 = np.array([[1,3,5],[2,4,6],[7,8,9]])

print(array2[1])

print(array2[1][0])

print(array2[0][2])

print((array2[0:2]))

print(array2[0,:2])  

print(array2[:2,1:]) #x axis , y axis

print(array2[:,:1])  #only the first indexes of each 



