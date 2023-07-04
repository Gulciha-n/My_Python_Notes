class worker:
    raise_rate=1.3
    number_worker=1
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        worker.number_worker+= 1

print(worker.number_worker,end=" ")
worker1 = worker("batu",9000)
print(worker1.name,worker1.salary)
print(worker.number_worker,end=" ")
worker2 = worker("pelin",10000)
print(worker2.name,worker2.salary)




