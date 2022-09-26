v="AEIOUaeiou"
s=input("Enter a string")
count=0
for i in s:
    if i in v:
        count+=1
print(count)
