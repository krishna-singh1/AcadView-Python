import re
file =open("test1.txt", "w")
file.write("Hello Vishwa pratap singh")
file.close()
file = open("test1.txt", "r")
text = file.read()
n = re.match(r'', text, re.M | re.I)
