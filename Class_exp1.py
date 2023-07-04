class Foods:
   def __init__(self,f1,f2,f3):
      self.name1=f1
      self.name2=f2
      self.name3=f3
   def show_info(self):
      print(f"Name1 : {self.name1}  name2 : {self.name2}  name3 : {self.name3}")

foods1 = Foods("soup","salad","pilav")
print(foods1.name1,foods1.name2,foods1.name3)

foods2 = Foods("kebap","köfte","döner")
print (foods2.name1,foods2.name2,foods2.name3)

foods1.show_info()