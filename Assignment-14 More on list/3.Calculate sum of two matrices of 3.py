A=[]
for i in range(3):
    A.append([int(e) for e in input("Enter three numbers with comma").split(',')])
B=[]
for i in range(3):
    B.append([int(e) for e in input("Enter three numbers with comma").split(',')])
C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j]+=A[i][k]*B[k][j]
for i in range(3):
    for j in range(3):
        print(C[i][j],end=' ')
    print()
    





#string = "abhinavagarwalsps@gmail.com"
#dct = dict()
#for ch in string:
#    if ch in dct:
#        dct[ch] += 1
#    else:
#        dct[ch] = 1
#print(dct)
