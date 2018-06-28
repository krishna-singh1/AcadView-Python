#l=list(map(int,input().split()))
#l=map(int,input().split())
#print(sum(list(map(int,input().split()))))
#print(len(list(map(int,input().split()))))


#a=list(map(int,input().split()))

#print(sum(a)/len(a))
#print(statistics.mean(a))
>>> l=[1,2,"dsdsd",[1,2,4,5,6]]
>>> l[3]
[1, 2, 4, 5, 6]
>>> l[3][3]
5
>>> dic={'hello':[123],'lol':[1,2,3]}
>>> dic
{'hello': [123], 'lol': [1, 2, 3]}
>>> dic["hola"]=1233
>>> dic
{'hello': [123], 'lol': [1, 2, 3], 'hola': 1233}
>>> hola in dic
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    hola in dic
NameError: name 'hola' is not defined
>>> "hola" in dic
True
>>> del dic["hola"]
>>> dic
{'hello': [123], 'lol': [1, 2, 3]}
>>> 
