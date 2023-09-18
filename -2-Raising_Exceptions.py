class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
def check_age(age):
    if age < 18:
        raise MyCustomError("Your age should be at least 18")        
    
try :
    user_age = int(input("Enter your age :"))
    check_age(user_age)
    print("Welcome.")
except MyCustomError as e:
    print(f"Error : {e}")
except ValueError:
    print("Error : You entered an invalid number!")
    
####

class Person:
    def __init__(self,name,age):
        if len(name) > 10:
            raise Exception("more charachter!")
            
        else :
            self.name = name
            self.age = age
 
try:
    p1 = Person("Ali",1989)
    print(f"Name : {p1.name} , Age :{p1.age}")
except Exception as e:
    print(f"Error : {e}")

#####

list1 = ["1","2","5a","10b","abc","10","50"]

for x in list1:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
    
#####

while True :
    num = input("number :")
    if num == 'q':
        break
    
    try:
        rslt = float(num)
        print(rslt)
    except ValueError:
        print("invalid number!")
        continue
    
#####

turkish_character = 'şçğüöıİ'

def Check_psw(psw):
    for i in psw:
        if i in turkish_character:
            raise TypeError("psw includes turkish characters!")
        else:
            pass
    print("valid password.")

psw = input("password :")
      
try:
    Check_psw(psw)
except TypeError as er:
    print(f"invalid password! Error : {er}")    
    
#####

def factorial(x):
    x = int(x)
    
    if x < 0 :
        raise ValueError("Negative value!")
    
    result = 1
    for i in range(1,x+1):
        result *= i
                
    return result


for i in [5,10,20,-3,"10a"]:
    try:
        y = factorial(i)
    except ValueError as err:
        print(err)
        continue
    print(y)
    
    
#####
        


