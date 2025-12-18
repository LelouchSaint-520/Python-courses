a = {1,2,3,4,5,6,7,8}
b = {2,3,4,5,6,7,8,9}
c = {3,4,5,6,7,8,9,0}

f = a ^ b ^ c
d = a ^ b
e = d ^ c
g = a.symmetric_difference(b)
print(e)
print(f)
