
name = ""   #False , not name = True

while not name:
    name = input("enter your name :")

print(f"your name is : {name}")


#####

numbers = [1,3,5,7,9,12,19,21]

i = 0
while (i < len(numbers)):
    print(i)
    i+=1
    
    
####


beginning = int(input("beginning :"))
finish = int(input("finish : "))
    
while beginning<finish:
    beginning += 1 
    print(beginning)
    

####≡


beginning = int(input("beginning :"))
finish = int(input("finish : "))
    
while beginning<finish:
    if beginning %2 == 1:
        print(beginning)
    beginning += 1 
    
    
####


i = 100
while i > 0:
    print(i)
    i-= 1
   
    
####


i = 1
numbers = []
while i<=5 :
    a = int(input("enter a number :"))
    numbers.append(a)
    i+=1
numbers.sort()    
print(numbers)       
  
  
####


products = []
piece = int(input("how many product do you want :"))

i= 0
while i<piece :
    name = input("name of product :")
    price = int(input("price of product :"))
    products.append({
        'name':name,
        'price':price
           })
    i += 1
    
for product in products:
    print(f"name : {product['name']}, price : {product['price']}")



####


students = []
num = int(input("How many student there are in the class : "))

i=0
while i<num :
    name = input("name :")
    surname = input("surname :")
    age = int(input("age :"))
    grade = int(input("grade :"))
    students.append({
        'name' : name,
        'surname' : surname,
        'age' : age,
        'grade' : grade
        
        })
    i += 1

for student in students :
    print(f"Name : {student['name']}, Surname : {student['surname']}, Age : {student['age']}, Grade : {student['grade']}")
    



    
    
    
