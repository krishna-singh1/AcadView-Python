Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py", line 2, in <module>
    l=int(input().split())
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12 23 43
>>> l
<map object at 0x055799F0>
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12 32
>>> l
[12, 32]
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
1 2 33 44
80
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12 23 43 43
4
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12 23 43
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py", line 8, in <module>
    b=a/len(l)
NameError: name 'l' is not defined
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12
12
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
>>> 

===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12 23
35
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
12 23 23
19.333333333333332
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
10 10 10
10.0
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
10 10 10
10.0
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py", line 9, in <module>
    print(mean(a))
NameError: name 'mean' is not defined
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
10 10 10
10.0
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py", line 9, in <module>
    print(statistics.mean(a))
NameError: name 'statistics' is not defined
>>> 
===== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py =====
10 01 01
4.0
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/list.py", line 10, in <module>
    print(statistics.mean(a))
NameError: name 'statistics' is not defined
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
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
hello
12
adad
name  is  hello
age is    12
4
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
TypeError: cc() missing 1 required positional argument: 'info'
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
name  is  vishwa
age is    12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 4, in cc
    print(len(name+age))
TypeError: must be str, not int
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
name  is  vishwa
age is    12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 4, in cc
    print(len(name)+len(age))
TypeError: object of type 'int' has no len()
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
21
name  is  vishwa
age is    21
6
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
name  is  vishwa
age is    12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 4, in cc
    print(int(len(name))+int(len(age)))
TypeError: object of type 'int' has no len()
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
print(int(len(name))+int(len(age)))

Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
ValueError: invalid literal for int() with base 10: ''
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
name  is  vishwa
age is    12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 4, in cc
    print(int(len(age)))
TypeError: object of type 'int' has no len()
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
name  is  vishwa
age is    12
Traceback (most recent call last):
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 5, in <module>
    cc(input(),int(input()))
  File "C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py", line 4, in cc
    print(len(age))
TypeError: object of type 'int' has no len()
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
12
name  is  vishwa
age is    12
6
>>> 
=== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/function.py ===
vishwa
23333333
dhfvbhvfhv
name  is  vishwa
age is    23333333
10
>>> l=[1,2,3,4,5,6]
>>> l[-1::-1]
[6, 5, 4, 3, 2, 1]
>>> l[-5:-1]
[2, 3, 4, 5]
>>> l[-5:1]
[]
>>> l[-5:0]
[]
>>> l[0:-1]
[1, 2, 3, 4, 5]
>>> l[0:-2]
[1, 2, 3, 4]
>>> l=[1,2,3,4,5,6,7,8,9]
>>> l[1::2]
[2, 4, 6, 8]
>>> l[-1::2]
[9]
>>> l[-1::-2]
[9, 7, 5, 3, 1]
>>> p=[10]
>>> l+p
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
====== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/dic.py ======
1
2
3
4
5
6
>>> 
====== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/dic.py ======
1  2  3  4  5  6  
>>> 
====== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/dic.py ======
1
2
3
4
5
6
>>> 
====== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/dic.py ======
1
 2
 3
 4
 5
 6
 
>>> 
====== RESTART: C:/Users/vishw/OneDrive/Desktop/Py pepinput/day3/dic.py ======
1
2
3
4
5
6
>>> range(l)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    range(l)
NameError: name 'l' is not defined
>>> range(6)
range(0, 6)
>>> l=12
>>> range(l)
range(0, 12)
>>> b=4
>>> range(b,l)
range(4, 12)
>>> 
