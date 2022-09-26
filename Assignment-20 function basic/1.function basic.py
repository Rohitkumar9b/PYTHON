def printN_natural(n):
    for i in range(1,n+1):
        print(i,end=' ')
def printN_naturalRev(n):
    for i in range(n,0,-1):
        print(i,end=" ")
def printN_square(n):
    for i in range(1,n+1):
        print(i*i,end=" ")
def printNOdd(n):
    for i in range(1,n+1):
        print(2*i-1,end=" ")
def printNEven(n):
    for i in range(1,n+1):
        print(2*i,end=' ')

def Sum(n):
    l1=[i for i in range(1,n+1)]
    return sum(l1)

def areaofCircle(r):
    return(3.14*r**2)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def simpleInterest(p,t,r):
    return (p*t*r)/100

def avg(a,b,c):
    return (a+b+c)/3
    
printN_natural(10)
print()
printN_naturalRev(10)
print()
printN_square(10)
print()
printNOdd(10)
print()
printNEven(10)
print()
s=Sum(10)
print(s)
a=areaofCircle(7)
print(a)
f=fact(5)
print(f)
s=simpleInterest(100,1,1)
print(s)
a=avg(1,2,3)
print(a)
