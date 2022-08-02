#it's inmutable
#regular parentesis are optional but prefereably use it
#if only contains one elemente add a comma at the end

tpl = (20,30,40,20,50,'xyz')
#tpl = (20,)#if you don't put the semicolon it will be treated as integer
#tpl[2] = 123 #not supported
print(type(tpl))
print(tpl * 3)
print(tpl.count(20))
print(tpl.index('xyz'))

lst = [67,34,'xyz']
print(type(lst))
tpl1 = tuple(lst)
print(type(tpl1))