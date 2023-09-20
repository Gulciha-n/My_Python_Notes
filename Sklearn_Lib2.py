from sklearn import datasets
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# print(iris)

# print(type(iris))

# print(iris.data)

data = pd.DataFrame(iris.data)
print(data)

data.head()

# write columns from feature_names in the iris features
data.columns = iris.feature_names 
print (data.head())

# add the target column that in the iris feature

data["target"] = iris.target
print(data)

#what is the target value? = is a number representing the dataset value

print(iris.target_names[0])
print(iris.target_names[1])
print(iris.target_names[2])

# split the datasets as x and y 
# X = attributes(inputs) , Y = outputs

# drop the target columns because it's outputs not inputs
X = data.drop("target",axis=1)
print(X)

Y = data["target"]
print(Y)




