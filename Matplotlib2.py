import matplotlib.pyplot as plt
import numpy as np

fig , axes = plt.subplots(2,1, figsize=(9, 7))

#add space between graphs
fig.subplots_adjust(hspace = 0.5)

x = [1,3,5,7,9,11,13]
y = [13,11,9,7,5,3,1]

axes[0].scatter(x,y ,color="red")
axes[0].set_title("sub_1")
axes[0].set_xlabel("sub_1 x ")
axes[0].set_ylabel("sub_1 y ")


axes[1].scatter(x,y , color="blue")
axes[1].set_title("sub_2")
axes[1].set_xlabel("sub_2 x ")
axes[1].set_ylabel("sub_2 y ")


