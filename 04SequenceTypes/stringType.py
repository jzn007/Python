s = "  juan zepeda nolasco  "
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
print(s[-7:-1])#-1 will not take the last element

#slicing
#third parameter is the step value --step = how many spaces will jump
print(s[0:10:2]) #take the first character and jump the step "2" to take another character
print(s[18::-1]) #it will reverse the string
print(s[::-1])

print(s.strip()) #removes all the spaces from beggining and in the end
print(s.lstrip())#removes all the spaces from the left
print(s.rstrip())#removes all the spaces from the right

print(s.find("Zep",0))#receives the value to find, the index where you want to start OPTIONAL
#it will return -1 if the value is not found

print(s.count("a"))#how many times appears
print(s.replace("Juan","Fernando"))#replace the first string with the second string

print(s.upper())
print(s.lower())
print(s.title())#the begining of every word will be with upper case