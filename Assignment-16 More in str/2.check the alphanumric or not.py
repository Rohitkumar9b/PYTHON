s=input()
alpha=False
numeric=False
specialchar=False
for a in s:
    if ord(a)>=97 and ord(a)<=122:
        alpha=True
    elif ord(a)>=65 and ord(a)<=90:
        alpha=True
    elif ord(a)>=48 and ord(a)<=57:
        numeric=True
    else:
        specialchar=True
if alpha==True and numeric==True:
    print("Yes")
else:
    print("No")
