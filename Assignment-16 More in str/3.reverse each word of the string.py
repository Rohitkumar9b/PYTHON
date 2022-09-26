s1=input()
l1=s1.split()
l2=[]
for i in l1:
    l2.append(i[::-1])
print(l2)
print(' '.join(l2))
#print("print in s2")
#s2=' '.join(l2)
#print(s2)
