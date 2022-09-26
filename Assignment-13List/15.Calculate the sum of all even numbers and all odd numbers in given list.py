l1=[1,2,3,1,4,5,6,7,8]
l2=[a for a in l1 if a%2==0]
print("Sum of even numbers is ",sum(l2))
l2=[a for a in l1 if a%2!=0]
print("Sum of odd numbers is ",sum(l2))
