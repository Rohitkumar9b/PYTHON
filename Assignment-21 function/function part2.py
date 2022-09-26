def evenOrOdd(n):
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")

def checkleap(yr):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                print("Leap year")
            else:
                print("NOt leap year")
        else:
            print("leap year")
    else:
        print("Not leap Year")

def isPalindrome(s):
    s1=s[::-1]
    if s1==s:
        return True
    else:
        return False

def isPrime(n):
    i=2
    while i<n:
        if n%i==0:
            break
        i+=1
    if i==n:
        return True
        #print("Prime number")
    else:
        return False
        #print("NOt")

def checkFibonacci(n):
    a=-1
    b=1
    s=0
    while s<=n:
        s=a+b
        a=b
        b=s
        print(s,end=' ')
        if s==n:
            return True
    return False
#print(checkFibonacci(8))
def nextPrime(n):
    i=n
    while i>=n:
        if isPrime(i):
            return i
            break
        i+=1
#print(nextPrime(10))

def NthFibonacci(n):
    a=-1
    b=1
    s=0
    count=0
    while count!=n:
        s=a+b
        a=b
        b=s
        count+=1
    return s
#print(NthFibonacci(10))
def fibonacci(n):
    a=-1
    b=1
    s=0
    count=0
    while count!=n:
        s=a+b
        a=b
        b=s
        count+=1
        print(s)
#fibonacci(10)
def countDigits(n):
    s=0
    while n:
        s=s+n%10
        n//=10
    return s
#print(countDigits(1234))
def countWords(s):
    l1=s.split()
    print(l1)
    print("total words is ",len(l1))
countWords('rohit kumar   singh')

def countVowels(s):
    v="AEIOUaeiou"
    print(s)
    count=0
    for i in s:
        for x in v:
            if x==i:
                count+=1
    return count
print(countVowels('aerioordiiou'))
