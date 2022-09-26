l1=list()
k=int(input())
n=2
while n<k:
    i=2
    while i<n:
        if n%i==0:
            break
        i+=1
    if i==n:
        l1.append(n)
    n+=1
print(l1)
