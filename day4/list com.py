cc=[]
p=[1,2,3]
l=['a','b','c']
for i in range (len(p)):
    for j in range (len(l)):
        cc.append([p[i],l[j]])
print(cc)

l=[x for x in range(10) if x%2==0]
print(l)
