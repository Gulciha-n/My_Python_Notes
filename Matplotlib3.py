import matplotlib.pyplot as plt
import numpy as np

#generate an image of random numbers

plt.figure()
img = np.random.random((50,50))

plt.imshow(img, cmap="gray")
plt.axis()
plt.show()


'''
1-Create a new empty figure by calling plt.figure().
2-Generate a 2D NumPy array of random numbers using np.random.random((50,50)).
This creates a 50x50 array filled with random values between 0 and 1.
3-Use plt.imshow() to display the generated image. 
4-Pass the image array as the first argument and set the cmap(color map) 
parameter to "gray" to display the image in grayscale.
5-Use plt.axis() to adjust the axis limits of the plot.
6-Finally, call plt.show() to display the figure with the generated image.

'''
