import re
n=bin(int(input()))
b=list(re.findall(r'(([1])+)',n))
a=str(b[b.index(max(b))][0])
print(a.count('1'))