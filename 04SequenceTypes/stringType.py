s = "  Juan Zepeda Nolasco  "
print(s)

s1 = """You are 
the creator
of your destinity"""
print(s1)

print(s1[0])
print(s[2]) #index of s at index 2
print(s * 2 ) #string repetition

print(len(s))
print(len(s1))

print(s[0:4]) #slicing
print(s[0:]) #if you not provided the end, it will take all the string till the end
print(s[:11]) #if you not provided the start, it will take all the string from the start

#negative numbers -1 represents the last index in the string
#-1 will not take the last element
print(s[-7:-1])

#slicing
#third parameter is the step value --step = how many spaces will jump
print(s[0:10:2]) #take the first character and jump the step "2" to take another character
print(s[18::-1]) #it will reverse the string

print(s[::-1])

print(s.strip()) #removes all the spaces from beggining and end
print(s.lstrip())#removes all the spaces from the left
