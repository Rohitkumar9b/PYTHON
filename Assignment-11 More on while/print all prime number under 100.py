k=0
for a in range(2,101):
    for i in range(2,a):
        if a%i==0:
            k=1
            break
        else:
            k=0
    if k==0:
        print(a,end=" ")