import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = np.array([7,6,4,3])

plt.figure()   #open an empty screen

plt.plot(x,y , color="blue" ,alpha =0.8 , label ="line")

##add scatter
plt.scatter(x,y ,color ="orange",alpha =0.7 ,label="scatter")

plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")

#enables gridlines
plt.grid(True)

#add labels or descriptions for lines, points
plt.legend()

plt.xticks([0,1,2,3,4,5])

#close figure
plt.show()







