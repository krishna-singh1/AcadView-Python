p=list()
n=int(input("number of user"))
for i in range(n):
    name=input("name")
    grade=int(input("number"))
    if grade>80:
        c="A+"
    else:
        c="A"
    p.append([name,c])
print(p)
