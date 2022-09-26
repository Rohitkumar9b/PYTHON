print("Enter list of numbers:")
l1=eval(input())
l1.sort()
print(l1)
i=0
while i<len(l1):
    print(l1[i]," - ",l1.count(l1[i]))
    i=i+l1.count(l1[i])
