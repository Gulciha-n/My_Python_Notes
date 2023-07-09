import pandas as pd

dict1 = {"name": ["murat","ayse","hilal"],
              "age" : [33,45,66],
              "city": ["Ankara","Ankara","Antalya"]} 

data1 = pd.DataFrame(dict1)
print(data1)

dict2 = {"name": ["ali","veli","kenan","murat","ayse","hilal"],
              "age" : [15,16,17,33,45,66],
              "city": ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]} 
data2 = pd.DataFrame(dict2)


#merge vertical (vertical=0 , horizontal=1)
data_vertical = pd.concat([data1,data2],axis=0)
print(data_vertical)

#merge horizontal
data_horizontal = pd.concat([data1,data2],axis=1)
print(data_horizontal)

