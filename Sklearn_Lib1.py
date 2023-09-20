import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("salaryData.csv") 
data.head()
data.info()

input1 = data.iloc[: , :-1].values
output1 = data.iloc[:,1].values

input1_train , input1_test, output1_train ,output1_test = train_test_split(input1,output1, test_size=1/3 , random_state = 123 ,shuffle =1 )                

model = LinearRegression()
model.fit(input1_train, output1_train)

prediction = model.predict(input1_test)
print(prediction)

plt.scatter(input1_train, output1_train, color = 'red')
plt.plot(input1_train, model.predict(input1_train), color = 'blue')
plt.title('Çalışma Süresine göre Maaş Durumu')
plt.xlabel('Çalışma Süresi')
plt.ylabel('Maaş')
plt.show()


plt.scatter(input1_test, output1_test, color = 'red')
plt.plot(input1_train, model.predict(input1_train), color = 'blue')
plt.title('Çalışma Süresine göre Maaş Durumu')
plt.xlabel('Çalışma Süresi')
plt.ylabel('Maaş')
plt.show()