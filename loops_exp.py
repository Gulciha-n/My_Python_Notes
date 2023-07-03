# a = 3* "bedir" + "han"
#print (a)

#b = "bedir" "han"
#print (b)


#f = "gülcihan"
#print("hey " + f)


# print(sum(range(4)))


#print ('Put several strings within parentheses '
#       'to have them joined together.')

#text = ('Put several strings within parentheses '
#        'to have them joined together.')




'''username = "gülcihan"
passwd = "hello"

while True :
    name = input("name: ")
    pswd = input ("password:")
    if (username != name or passwd != pswd):
        print ("entered is unsuccesful")

    else :
        print ("entered is succesful")
        break '''



'''i=1
list1 = [1,2,3,4,5,6,7,8,9,10]

while i in range(1,11):
    if i in list1 and i%2==0 :
        print (i)
    i=i+1'''



#for i in reversed(range(0,11,2)):
#   print (i)


'''for i in range(1,20):
    if i%2==0:
        continue
    print (i)'''



'''for i in range(1,20):
    if i==11 :
        break
    print (i)'''




'''passNote = "70"
while True:
    note = input ("enter your note :")
    if note >= passNote :
        print ("you passed")
    else :
        print ("you failed") '''




'''name = input ("enter your name :")
if name == "" :
    print ("you did not enter your name!") 
else :
    print(f"hello {name}")'''




'''name = input ("enter your name :")

while name == "":
    print("you did not enter your name")
    name = input ("please enter your name:")
print (f"hello {name}")'''




'''user = input ("enter user name :")

while user != "gülcihan" :
    print ("your nane is wrong")
    user = input ("enter user name :")
print (f"hello {user}")'''




'''food = input ("enter a food you like :")

while not food == "q" :
    print (f"you like {food}")
    food = input ("enter an another food that you like :")
print ("byee")'''



'''num = int (input("enter a number between 1-10: "))

while num < 1 or num > 10 :
    print (f"{num} number is not valid")
    num = int (input("enter a number between 1-10 :"))
print (f"your number is {num}")'''


'''color = input ("enter a color : ")

match color :
    case "blue":
        print ("heeyy your color is blue")
    case "yellow" :
        print ("your color is yellow :( ")
    case other_color :
        print (f"your color is {other_color} byee")'''



'''def main():
    for count in range(1, 10):
        print('Z' *count)
    for count in range(8, 0, -1):
        print('Z' * count)
main()'''


def main():
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Token: {item}')
if __name__ == '__main__':
    main()




    







