'''
def CountDown(n):       #generator oluşturulmamiş kod bellekte yer kaplar.
    while n>0:
        print(n) 
        n -= 1

CountDown(5)

 ''' 



def CountDown (n):      
    while n > 0:
        yield n
        n -= 1

mygenerator = CountDown(5)  

for i in mygenerator:     
    print(i)              


''' 
yield ifadesi ile n değeri döndürülür

mygenerator ifadesini döngüye alarak hep bir önceki değeri unutup
yenisini üretmesini sağladik.

Her döngü adiminda n değeri, generator tarafindan üretilir 
ve döngü bu değerleri tüketerek çalişir.

 for i in mygenerator: döngüsüyle generatorun değerleri sırayla alınır ve i değişkenine atanır. 
 Bu şekilde,her adımda bir önceki değer unutulur ve jeneratör bir sonraki değeri üretir.

''' 