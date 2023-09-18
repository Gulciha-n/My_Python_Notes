class Person():
    def __init__(self):
        print("person created")
        
class Student(Person):
    pass 

p1 = Person()
s1 = Student()

#####

class Person():
    def __init__(self):
        print("person created")
        
class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("Student created")
        
s2 = Student()

#####

class Person():
    def __init__(self , fname , lname):
        self.firstname = fname
        self.lastname = lname
        print("person created")
        
    def who_am_i(self):
        print("I am a person")
        
    def eat(self):
        print("I am eating")
    
class Student(Person):
    def __init__(self, fname , lname, number):
        Person.__init__(self, fname , lname)
        self.student_number = number
        print("Student created")
    
    # override
    def who_am_i(self): 
        print("I am a student")
    
    def sayHello(self):
        print("Hello there I am a student")

class Teacher(Person):
    def __init__(self , fname , lname , branch):
        Person.__init__(self, fname, lname)
        self.brn = branch
    
    def who_am_i(self):
        print("I am a teacher")

t1  =Teacher('Ahmet', 'yılmaz', 'math')
print(t1.firstname + ' ' + t1.lastname + ' ' + t1.brn)        
p2 = Person('Batu', 'yılmaz')
s3 = Student('Çınar', 'turan',1256)

print(p2.firstname + " " + p2.lastname)
print(s3.firstname + " " + s3.lastname + " " + str(s3.student_number) )

p2.who_am_i()
s3.who_am_i()

p2.eat()
s3.eat()

s3.sayHello()





