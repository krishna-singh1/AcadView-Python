import re

phone = "2004-959-559 # This is Phone Number"


num = re.match(r'(.*)#(.*)',  phone, re.M | re.I)
print("Phone Number : ", num.group(2))

pp = "121267891212"
num1 = re.match(r'[6789]', pp, re.M | re.I)
print(num1.group(1))