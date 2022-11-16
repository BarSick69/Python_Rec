def cmmdc(n,m):
    if(n>m):
        return cmmdc(m,n-m)
    elif(n<m):
        return cmmdc(m-n,n)
    else:
        return n
m=int(input("Dati m: "))
n=int(input("Dati n: "))
print(cmmdc(m,n))