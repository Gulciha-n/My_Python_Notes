def calculate_average (list1) :
    if len(list1) == 0 :
        return None
    else :
        return sum(list1) / len(list1)
    
my_list = []
average = calculate_average(my_list)

if average is None :
    print ("average is None")
else :
    print (average)







def calculate_average(numbers):
    if len(numberss)==0 :
        return None 
    else :
        return sum(numbers)/len(numbers)
    
numberss = []
average = calculate_average(numberss)

if numberss is None :
    print ("numberss is None")
else :
    print (average)







def factor(n):
    if n == 0 :
        return 1
    else :
        return n*factor(n-1)
     
a = int(input("enter a number :"))
fact = factor(a)
print (fact) 








def my_fonction (filename):
    print (filename + "this email is gülcihan's")

email = input ("enter your email :")
my_fonction(email)







def my_function ():
    first_name = input("enter your name :")
    last_name = input("enter your last name :")
    grade = input("enter your grade :")
    print(first_name,last_name,grade, end = " ")

my_function()            # NOT : kullanıcıdan değer alacaksak yerel değişken 
                         # kullanabiliriz hem yerel değişken hem de parametre 
                         # aynı anda akullanılmaz. parametre ile değer almak 
                         # için farklı bir metod kullanırız .








def my_function ():
    first_name = input ("Enter your first name: ")
    last_name = input ("Enter your last name: ")
    grade = input ("Enter your grade: ")
    print (first_name, last_name, grade, end=" ")

my_function ()






def my_function(first_name, last_name, grade):
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Grade:", grade)

a = input("Enter your first name: ")
b = input("Enter your last name: ")
c = input("Enter your grade: ")

my_function(a, b, c)





def f (*some):
    print("your parameters are : ",list(some))

num1 = input("num1:")
num2 = input("num2:")
num3 = input("num3:")
f (num1,num2,num3)





def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes",age = 30)





def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")






def funct(fruit):
    for x in fruit:
        print (x)

drinks= ["Ice tea","Coca cola","water"]
funct(drinks)





def my_funct (x):
    f = x**2 + 4*x -1
    print(f"The function resut is :{f}" )

print(my_funct(6))





def funct(x):
    return 8*x

a = funct(4)
print(a)





def sqr(x):
    return x**2

num = [4,5,6,7,8]

for a in num :
    b = sqr(a)
    print (b,end=" ")






def cube(x):
    return x**3

list1 = [2,3,4,5,6,7]

a = map(cube,list1)
print (list(a))







sum_funct = lambda a,b : a+b

result = sum_funct(3,5)
print (f"sum of numbers is : {result}")



numbers = [4,5,6,7,8,9]
sqr = map(lambda x : x**2 , numbers)
print(list(sqr))

number = 10







def change_number():
    number = 3 
    return number

x= change_number()
print(x)
print (number)






def chc_number():
    global number 
    number = 4
    return number

chc_number()
print(number)

list_of_numbers = [2,5,6,3,4,9,2]
new_list = []

for number in list_of_numbers:
    inc_num = number +1
    if inc_num < 6:
        new_list.append(number)
print(new_list)   






































    




