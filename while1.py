import time
temp = 10

while temp <= 50:
    
    if temp < 20:
        print("Cold !") 
    elif temp >= 20 and temp < 30:
        print ("Good :)")  
    else:
        print("Hot!")      

    print("the current temperature is ",temp)
    temp += 5
    time.sleep(2)




