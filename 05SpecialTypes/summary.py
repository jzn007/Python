a = 20
b = 20
b = 30
print(id(a), id(b))

f = 3.14
c = 5 + 3j
print(c.real)
print(c.imag)

s = "Juan"
print(type(s))

lst = [1,2,3,4,5]
print(lst)
b = bytes(lst) #mutable
print(b)
print(type(b))

ba = bytearray(lst)
#print(ba)
print(type(ba)) #inmutable

r1 = range(20)
r2 = range(1,20)
r3 = range(1,30,3) #inmutable

t = (1,2,3,4,5)
print(type(t))

s = {1,3,5,5,7,9} #mutable
print(type(s))
print(s)

fs = frozenset(s) #inmutable
print(fs)
print(type(fs))

d = {1:100, 2:90, 3:89}
print(type(d))