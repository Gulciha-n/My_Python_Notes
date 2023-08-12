
dict1 = {"Ankara":6 , "istanbul" : 34}

print(dict1["Ankara"])
print(dict1["istanbul"])

dict1["kocaeli"] = 6
print(dict1)

####

users = {
    "gulcihan" : {"age":20, "job": "engineer"},
    "cansu" : {"age":24,"job":"dietation"}     
     }

print(users["gulcihan"])
print(users["cansu"])

print(users["gulcihan"]["age"])

####

students = {
    
    '120' : {"name":"Ali","surname":"Yılmaz","phone":"532 000 00 01"},
    '125' : {"name":"Can","surname":"korkmaz","phone":"532 000 00 02"},
    '128' : {"name":"Volkan","surname":"Yükselen","phone":"532 000 00 01"}
    }

number = input("enter your number :")
name = input("enter your name : ")
surname = input("enter your surname : ")
phone = input("enter your phone :")

#students[number] = {"name":name,"surname":surname,"phone":phone}
#print(students)

students.update({
    number : {
        "name":name,
        "surname":surname,
        "phone":phone}
    })
print(students)
#you can add a new attribute with using "update"

stdNo = input("no :")
student = students[number]
print(student)

####
# Value types => string , number
x = 10 
y = 20

x = y

y= 90

print(x,y)  # x=20 , y=90


####

# Reference types

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"
# a also changes when we change b because adress of a equal b
print(a,b)




