dict1 = { 1: "John", 2: "Bob", 3:"Bill"} #value-key
print(dict1)
print(dict1.items())
k = dict1.keys()
print(k)
for i in k:
    print(i)

v = dict1.values()
print(v)
for i in v:
    print(i)

print(dict1[3])
del(dict1[3])
print(dict1)
