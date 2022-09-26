l1=list()
n=int(input("enter a number"))
count=0
i=2
while i>=2:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    if j==i:
        l1.append(i)
        count+=1
    if count==n:
        break
    i+=1
print(l1)
