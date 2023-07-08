
import numpy as np

array1 = np.array([1,2,3],dtype=int)
print(array1,",",array1.dtype)


#astype = change data (array) type

array2 = array1.astype(np.float64)
print(array2,",",array2.dtype)


array3 = array2.astype(np.int64)
print(array3,",",array3.dtype)






