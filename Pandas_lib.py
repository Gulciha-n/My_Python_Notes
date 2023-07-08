import pandas as pd

dictionary = {"names":["Gülcihan","Cansu","Suna"],
              "ages" :[23,25,24],
              "department" :["engineer","dietitian","engineer"]}

data = pd.DataFrame(dictionary)
print(data)

data.head(2) #first two lines
data.tail(2) #last two lines

#writed columns
print(data.columns)  

#data information
print(data.info())   

#statistics attributes
print(data.describe()) 


print(data["names"])
print(data["ages"])
print(data["department"])


#add column
data["cities"] = ["istanbul","Ankara","İzmir"]
print(data)

# only "ages" variable in all columns
print(data.loc[: ,"ages"])

# only "ages" variable and first two columns
print(data.loc[:1,"ages"])
# 1, inclusive 

# from names to cities in first two columns
print(data.loc[:1,"names":"cities"])

#only names and cities are included
print(data.loc[:2,["names","cities"]])

#print lines in reverse 
print(data.loc[::-1 , :])


# iloc = index location
print(data.iloc[:,1])
# :,1 = all columns and 1.index (ages)
print(data.iloc[:,2])
# :,2 = all columns and 2.index (department)


# :3 = first three columns , [0,1] = first and second indexes
print(data.iloc[:3,[0,1]])


































