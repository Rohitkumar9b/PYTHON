print("Enter a list")
t1=tuple(eval(input()))
print("Enter another list")
t2=tuple(eval(input()))
t3=tuple(sorted(t1))
t4=tuple(sorted(t2))
if t3==t4:
    print("Both tuple contains same elements")
else:
    print("NOt same elements in both tuple")
