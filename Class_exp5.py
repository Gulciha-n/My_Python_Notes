class worker:
   num_worker=0
   def __init__(self,name,salary):
        self.name=name
        self.salary = salary
        worker.num_worker+=1
        
   def info(self):
       return f"Name :{self.name}   salary :{self.salary}"
   @classmethod
   def number(cls):
       return cls.num_worker
       
worker1=worker("Batu",9000)
worker2=worker("Derya",10000)

print (worker1.info())
print (worker2.info())
print(worker.num_worker)

