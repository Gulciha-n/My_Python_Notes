import random
while True:
    random_number = random.randrange(1000)
    print(random_number)

    if random_number == 222:
        print("found !")
        break
    
