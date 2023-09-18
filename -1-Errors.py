#Errors

# print(a) #NameError
# int('1a2') #ValueError
# print(10/0) #ZeroDivisionError
# print('tex't) #SyntaxError



#Error Handling (hata yönetimi)

#ZeroDivisionError => try - except
try:
    x = int(input('x :'))
    y = int(input('y :'))
    print(x/y)
except ZeroDivisionError:
    print("you can not use zero for y")
except ValueError:
    print('enter numbers for x and y')

#####

try:
    x = int(input('x :'))
    y = int(input('y :'))
    print(x/y)
except (ZeroDivisionError,ValueError) as e :
    print("you entered a wrong information")
    print(e)
    
####

    
try:
    x = int(input('x :'))
    y = int(input('y :'))
    print(x/y)
except :
    print("you entered a wrong information")

#####

while True:
    try:
        x = int(input('x :'))
        y = int(input('y :'))
        print(x/y)
    except :
        print("you entered a wrong information")
    else:
        break
    
#####


while True:
    try:
        x = int(input('x :'))
        y = int(input('y :'))
        print(x/y)
    except Exception as ex:
        print("you entered a wrong information",ex)
    else:
        break
    finally:  #closes files
        print('try - except ended')

#####




 