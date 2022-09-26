print("Enter a list")
t1=tuple(eval(input()))
print(type(t1))
print(t1)
t2=tuple(sorted(t1))
print(t2)
i=-1
while i>(-len(t2)):
    if max(t2)!=t2[i]:
        print('second largest is ',t2[i])
        break
    i-=1
