import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("salaryData.csv") 
data.head()
data.info()

X = data.iloc[: , :-1].values
Y = data.iloc[:,1].values

X_train , X_test, Y_train ,Y_test = train_test_split(X,Y, test_size=1/3 , random_state = 123 ,shuffle =1 )                

model = LinearRegression()
model.fit(X_train, Y_train)

prediction = model.predict(X_test)
print(prediction)

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary Status According to Working Time ')
plt.xlabel('Salary Status')
plt.ylabel('Salary')
plt.show()


plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary Status According to Working Time')
plt.xlabel('Salary Status')
plt.ylabel('Salary')
plt.show()




