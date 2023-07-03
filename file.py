
#exp1
'''f = open ("files.txt","r")
content = f.read()
print(content)
f.close()'''



#exp2

'''with open("files.txt","r") as f:
    content = f.readlines()
    print (content)
    for line in content:
        print(line,end=" ")'''


#exp3

'''with open ("files.txt","r") as f:
    for line in f:
        print(line,end=" ")'''


#exp4

'''with open("files.txt","r") as f:
    line = f.readline()
    print(line,end="")'''



#exp5
'''with open("files.txt","r") as f:
    line = f.read(1000)
    print(line)'''




#exp6
'''with open("file2.txt","w") as f:
    f.write("I am gulcihan I want to be a coder\n")
    f.write("hello")'''




#exp7

'''import random

#with open("number_history.txt","w") as number_files
number_files = open("number_history.txt","w")

while True:
    number = random.randrange(1000)
    print(number)
    number_files.write(str(number))
    #number_files.close()

    if number == 77:
        print("number founded")
        break'''







    











 

  


        






