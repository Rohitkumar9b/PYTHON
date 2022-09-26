d1={1:'Rohit',2:'Gautam',3:'Abhinav',5:'Amit'}
c1= sorted(d1, key=lambda x:d1[x])
print(type(c1))
for i in c1:
    print(i," - ",d1[i])

l1 = [1,2,3,4,5,6,7,8,9]
c1= sorted(l1, key=lambda x:x%2)
print(c1)


