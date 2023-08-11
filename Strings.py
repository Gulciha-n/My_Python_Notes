print("""strings in 
python

!!""")

print("strings\npython")
print("strings\tpython")

a = "strings"
b = "python"
print(a + " " + b)
print(a[1])
print(a[1:4])
print(a[::2])
print(a[::-1])



num1= input("number 1 : ")
num2= input("number 2 : ")

sum = int(num1)+ int(num2)
print(sum)
print(type(num1))

isonline = True
print(int(isonline)) 



pi= 3.14
r = float(input("enter radius : "))
a = circle_area = pi*r**2
b = circle_perimeter = 2*pi*r
#print ("area :{} perimeter : {}".format(a,b))
print("area :" + str(a) + "perimeter : " + str(b))



name = input("enter your name : ")
surname = input("enter your surname : ")
age = input("enter your age : ")

print("name : " + name + "\nsurname : " + surname + "\nage : " + age)



result = 200 / 700
print("result : {r:.3}".format(r=result))
print("result : {r:10.3}".format(r=result))



message = " hello there. my name is gulcihan"
print(message)
print(message.upper())
print(message.lower())
print(message.capitalize())
s = message.split()
print(message.split())
print(s[5])

message = " ".join(message)
print(message)

index = message.find('gulcihan')
print(index)

isfound = message.startswith(' ')
isfoundd = message.endswith('n')
print(isfound)
print(isfoundd)

message = message.replace("gulcihan", "cansu")
message = message.replace(" ", "_")
print(message)

message = message.center(50,"*")
print(message)



import string
from weakref import ProxyType


string1 = " Hello World I am Gulcihan "
n=string1.strip()
print(n)
c=string1.lstrip()  #lstrip
d=string1.rstrip()  #rstrip
print(c)
print(d)

#rslt = string1.index('World')
rslt = string1.rindex('Gulci')

#print(rslt)
print(rslt)
print(string1.isalpha())
print(string1.isdigit())
print(string1.center(50,"*"))

result = "contents".center(30)
result1 = "contents".ljust(20,"*")
result2 = "contents".rjust(20,"-")
print(result)
print(result1)
print(result2)

result3 = string1.replace(" ", "_")
result4 = string1.replace(" ", "_",2)
result5 = string1.replace(" ", "")
print(result3)
print(result4)
print(result5)

result6 = string1.replace("World" , "There")
print(result6)

result7 = string1.split(" ")
print(result7)
print(result7[5])





























