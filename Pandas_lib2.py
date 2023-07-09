import pandas as pd

#filters

dictionary = {"name": ["ali","veli","kenan","murat","ayse","hilal"],
              "age" : [15,16,17,33,45,66],
              "city": ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]} 
data = pd.DataFrame(dictionary)
print(data)


filter1 = data.age > 22
print(filter1)


#print filtred datas
#The expression data[filter1] applies the condition filter1 to all rows 
#of the data DataFrame and selects the rows that satisfy the condition. 
#It creates a subset DataFrame consisting of the selected rows and returns it.
filters_data = data[filter1]
print(filters_data)



#average age
average_age = data.age.mean()

#add a new column
data["group_age"] = ["young" if average_age>i else "old" for i in data.age]
print(data)























