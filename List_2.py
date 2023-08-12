names = ["Ali","Yagmur","Hakan","Deniz"]
years = [1997,1989,1999,2000]

names.append("Cenk")
print(names)

names.insert(0, "Sena")
print(names)

names.remove("Deniz")
print(names)

names.pop(1)
print(names)

index = names.index("Sena")
print(index)

result = "Ali" in names
print(result)
result1 = names.index("Hakan")
print(result1)


names.reverse()
print(names)

names.sort()
print(names)

years.sort()
print(years)

####

string = "Chevrolet,Dacia"

result2 = string.split()
print(result2)
 
print(min(years))
print(max(years))

print(years.count(1999))

years.clear()
print(years)

####

brands = []
b1 = input("brand1 :")
b2 = input("brand2 :")
b3 = input("brand3 :")

brands.append(b1)
brands.append(b2)
brands.append(b3)
print(brands)



