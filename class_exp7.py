class Worker:
    def __init__(self,name,age): 
        self.name=name 
        self.age=age

    def __str__(self):
       return self.name + " has a job who age is " + str(self.age)

worker1 = Worker("pelin",19)
print(worker1)






