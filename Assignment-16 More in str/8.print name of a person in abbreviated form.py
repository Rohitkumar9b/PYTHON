s=input()
l1=s.split()
i=0
while i<(len(l1)-1):
    print((l1[i][0]).upper(),'.',sep='',end=' ')
    i+=1
l2=[]
for r in l1[-1]:
    l2.append(r)
#print(l2)
s1=l2[0].upper()
del l2[0]
l2.insert(0,s1)
s2=''.join(l2)
print(s2)
