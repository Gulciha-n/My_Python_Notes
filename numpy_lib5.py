import numpy as np

array2D = np.array([[2,4,6,8],[1,3,5,7],[2,3,4,5]])
print(array2D)


array1 = np.zeros((3,4))
print((array1))


array2 = np.ones((3,4))
print(array2)


array3= np.empty((3,4))
print(array3)


array4 = np.arange(10,20,2)
print(array4)


#linspace = np.linspace(start, stop, num)
array5 = np.linspace(10,30,5)
print(array5)


#float array
array6 = np.float32([[1,2,3],[5,6,7]])
print(array6)



#mathemathical operations
a = np.array([1,2,3])
b = np.array([3,5,7])

print(a+b)
print(a-b)
print(a**2)
print(b**2)

print(np.sum(a))
print(np.sum(b))

print(np.max(a))
print(np.max(b))

print(np.min(a))
print(np.min(b))


#average = using "mean"
print(np.mean(a))
print(np.mean(b))

#median = in the middle
print(np.median(a))
print(np.median(b))


#generating random numbers in range [0,1]
random_array = np.random.random((3,3))
print(random_array)
































