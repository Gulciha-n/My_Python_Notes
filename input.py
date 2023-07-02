import module 

result = module.area_round(7)
print(result)

rslt= module.area_round(5)
print(rslt)

import random

for i in range(10):
    print (random.randint(1,20))

list1= ["blue","gray","yellow","pink","orange"]

print(random.choice(list1))

print(random.sample(list1,3))

random.shuffle(list1)
print(list1)


