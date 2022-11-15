def recursiv_putere(a,putere):
    if(putere==1):
        return a
    else:
        return a*recursiv_putere(a,putere-1)
nr1=int(input("Baza= "))
nr2=int(input("Puterea= "))
print(recursiv_putere(nr1,nr2))
def putere_it(a,putere):
    produs=1
    for i in range(putere):
        produs*=a
    return produs
print(putere_it(nr1,nr2))