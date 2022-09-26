print("Enter numbers with space")
s1={int(x) for x in input().split()}
print("Enter again numbers with space")
s2={int(x) for x in input().split()}
s3=s1.union(s2)
print(s3)
