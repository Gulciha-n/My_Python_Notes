import numpy as np

array2D = np.array([[2,4,6,8,0],[1,3,5,7,9]])

#slicing
print(array2D[0][2])
print(array2D[1][3])

print(array2D[0,1],array2D[0,2])
print(array2D[1,0],array2D[1,4])

print(array2D[0,1:5])
print(array2D[1,1:4])


# : all of the rows , columns
print(array2D[:,:])
print(array2D[:,1])
print(array2D[0,:])


#the last row and all columns
print(array2D[-1,:])


#creating a vector
vector = array2D.ravel()
print(vector)

vector[0]=10
print(vector)


#concatenating of arrays
#axis=1 => concatenating of columns
#axis=0 => concatenating of rows

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)



#array split 
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

















