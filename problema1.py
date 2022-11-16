n = int(input("Dat n: "))
def suma1rec(n):
    if(n<=1):
        return 0
    return n*2*(n-1)+suma1(n-1)
def suma1(n):
    suma=0
    for i in range(1,n+1):
        suma+=i*2*(i-1)
    return suma
def suma2rec(n):
    if(n<=0):
        return 0
    return n/((2*n-1)*(2*n+1))+suma2rec(n-1)
def suma2(i):
    suma=0
    for n in range(0,i+1):
        suma+=n/((2*n-1)*(2*n+1))
    return suma      
print(suma1rec(n))
print(suma1(n))
print(suma2rec(n))
print(suma2(n))
