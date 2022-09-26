def printNnatural(n):
    if n:
        printNnatural(n-1)
    print(n)
#printNnatural(10)

def NnaturalReverse(n):
    print(n,end=' ')
    if n:
        NnaturalReverse(n-1)
#NnaturalReverse(10)
def Nodd(n):
    if n!=1:
        Nodd(n-1)
    print(2*n-1,end=' ')
#Nodd(10)
def NoddRev(n):
    print(2*n-1,end=' ')
    if n!=1:
        NoddRev(n-1)
#NoddRev(10)

def Neven(n):
    if n!=1:
        Neven(n-1)
    print(2*n,end=' ')
#Neven(10)
def NevenRev(n):
    print(2*n,end=' ')
    if n!=1:
        NevenRev(n-1)
#NevenRev(10)
def sumN(n):
    if n==1:
        s=1
    else:
        s=n+sumN(n-1)
    return s
#print(sumN(10))

def sumEvenN(n):
    if n==1:
        s=2
    else:
        s=2*n+sumEvenN(n-1)
    return s
#print(sumEvenN(3))

def sumOddN(n):
    if n==1:
        s=1
    else:
        s=(2*n-1)+sumOddN(n-1)
    return s
#print(sumOddN(3))
f=lambda n: 1 if n==0 else n*f(n-1)
print(f(5))
