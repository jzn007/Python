lst = [10,20,'Juan', -10,30.5] 
print(lst)

print(lst[3])#indexing starts from zero
print(lst[3:5])#slicing
print(lst * 4) #repetition
print(len(lst)) #size of the list

#add and remove elements
lst.append(40)
lst.remove('Juan')#it's case sensitive, remove by value
del(lst[1]) #remove by index
print(lst)

#lst.clear()#remove all the elements
#print(lst)
print(max(lst))
print(min(lst))

lst.insert(3, 99) #index and value
print(lst)

#lst.sort() #ascending order
lst.sort(reverse=True) #descending order
print(lst)


