s = {10,20,30,"xyz",10,20} #set does not allow duplicates, they are omitted
print(s)
print(type(s))

s.update([88,99]) #not garatee the order
print(s)
#print(s[0])#indexing is not supported
#print(s[0:5])#slicing is not subscriptable
#print(s*2)#repetition is not supported
s.remove(30)
print(s)


#Frozen Set
f = frozenset(s)
#f.update([20]) #not supported
#f.remove(20)#not supported

