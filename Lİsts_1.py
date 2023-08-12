
numbers = [1, 10, 5 , 16, 4 ,9 ,10]
letters = ['a', 'g', 's','b','y','a','s']

value = min(numbers)
value = max(numbers)
value = max(letters)
value = min(letters)

value = numbers[3:6]
value = numbers[:3]
value = numbers[4:]

numbers[4] = 40

numbers.append(49)      #adds item we want
numbers.append(59)

numbers.insert(3,78)    #adds item in index we want 
numbers.insert(-1 ,20)

numbers.pop()           #delete the last one
numbers.pop(0)
numbers.pop(-1)

numbers.remove(49)      #delete we want
numbers.remove(40)

numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(letters)
print(numbers)

print(len(numbers))
print(len(letters))

numbers.clear()

print(numbers.count(10))
print(letters.count('a'))


message = 'Hello There . My name is Gülcihan'.split()
print(message)
print(message[0])


my_list = [1,2,3]
my_list= ['one' , 2, True]
print(my_list)


list1= ['one', 'two', 'there']
list2 = ['four', 'five', 'six']

number = list1+ list2
print(number)
print(len(number))



usersA = ['Derya', 20]
usersB = ['Pelin', 19]

users = [usersA, usersB]  #

print(usersA)
print(usersB)
print(users)

print(users[0][0])



list1 = ['Bmw', ' Mercedes', 'Opel', 'Mazda'] 
 
result = (len(list1)) 

result = list1[0]
result = list1[3]
result = list1[-1]

list1[-1] = 'Toyota'
result = list1

result  = 'Mercedes' in list1

result = list1[-2]

result = list1[0:3]
result = list1[:3]
result = list1[-2:]

result[-2] = ['Toyota', 'Renault']
result = list1

result = list1 + ['Audi', 'Nissan']

del list1[-1] 
result = list1

result = list1[::-1]


studentA = ['Yiğit', 'Bilgi', 2010,[70,60,70]]
studentB = ['Ahmet', 'Sevim',1999,[80,80,70]]
studentC = ['Ahmet', 'Turan',1998,[80,70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} age and grade point average {(studentA[3][0]) +(studentA[3][1]) + (studentA[3][2])} "

print(result)



