class worker:
   def __init__(self,name,salary):
        self.name=name
        self.salary = salary
     
        
   def info(self):
       return f"Name :{self.name}   salary :{self.salary}"
   
worker1=worker("Batu",9000)
worker2=worker("Derya",10000)

print (worker1.info())
print (worker2.info())




