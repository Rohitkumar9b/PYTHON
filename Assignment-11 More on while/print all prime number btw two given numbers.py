k=1
for a in range(int(input("Enter first number")),int(input("Enter second number"))+1):
    for i in range(2,a):
        if a%i==0:
            k=0
            break
        else:
            k=1
    if k==1 and a!=1:
        print(a,end=" ")