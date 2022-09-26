def binary(n):
    if n==1:
        s='1'
    else:
        s=binary(n//2)+str(n%2)
    return s
#print(binary(25))

def octal(n):
    if n==1:
        s='1'
    else:
        s=octal(n//8)+str(n%8)
    return s
#print(octal(10))
def sumSquares(n):
    if n==1:
        s=1
    else:
        s=n*n+sumSquares(n-1)
    return s

#print(sumSquares(4))
def fibonacci(n):
    if n!=2:
        a=1
        b=0
        s=a+b
        fibonacci(n-1)
    return s
#print(fibonacci(5))

def f():
    a=1
    if a:=2:
        print(a)
        print('HI')

f()











class Item:
    x=5
    def __init__(self):
        print("Welcome")
    def f1():
        print("Hello")

i1=Item()  #Item(i1,a,b)

