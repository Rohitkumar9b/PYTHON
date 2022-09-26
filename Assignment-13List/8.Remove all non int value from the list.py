# l1=eval(input())
# print(l1)
# l2=[a for a in l1 if type(a)==int]
# print(l2)


def square(arg):
    return (int(arg)**2)

print(list(map(square, [5])))