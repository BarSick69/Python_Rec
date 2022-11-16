import random
random.seed(2139)
tablou=[]
for i in range(0,10):
    tablou.append(random.randint(0,10))
print(tablou)
new=tablou
new.reverse()
print(new)
lungime=len(tablou)-1

def suma(tabloul,lungime):
    if(lungime==0):
        return tabloul[0]
    return tabloul[lungime]+suma(tabloul,lungime-1)

def sumapare(tabloul,lungime):
    if(tabloul[lungime]%2==0):
        if(lungime<=0):
            return tabloul[0]
        return tabloul[lungime]+sumapare(tabloul,lungime-1)
    else:
        if(lungime<=0):
            return 0
        return sumapare(tabloul,lungime-1)

def sumaimpare(tabloul,lungime):
    if(tabloul[lungime]%2!=0):
        if(lungime<=0):
            return tabloul[0]
        return tabloul[lungime]+sumaimpare(tabloul,lungime-1)
    else:
        if(lungime<=0):
            return 0
        return sumaimpare(tabloul,lungime-1)
        
print(suma(tablou,lungime))
print(sumapare(tablou,lungime))
print(sumaimpare(tablou,lungime))

