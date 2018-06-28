import re
l = input()
p = ()
p = [float(s) for s in re.findall(r'-?\d+\.?\d*', l)]
k = int(sum(p))
num_str = str(k)
sum = 0
while (sum>=0 and sum<=9):
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
print(sum)

