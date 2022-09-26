n=int(input("Enter a number"))
i=2
while i<n:
    if n%i==0:
        break
    i=i+1
if i==n:
    print("Prime number")
else:
    print("Not Prime number")