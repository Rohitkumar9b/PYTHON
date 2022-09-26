s=input()
d=dict()
d1={}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
for k,v in d.items():
    print(k,' - ',v)
