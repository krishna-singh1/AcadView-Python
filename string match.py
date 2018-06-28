import re
num = input()
n = re.match(r'[+][9][1][-][6789]([0-9]{9})', num, re.M | re.I)
if n:
    print("valid")
else:
    print("not valid")


#r'^(\+91-)[6789](\d){9}$'