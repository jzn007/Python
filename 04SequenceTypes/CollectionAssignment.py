#List countries
print("----------------- Using a List ----------------- ")
countriesList = ["Mexico", "Canada", "USA"] #Add 3 countries to a List
print(countriesList)
countriesList.append("UK") #Add an country at the end
print(countriesList)
del(countriesList[3]) #remove by index
print(countriesList)
countriesList.insert(2, "UK") #add a country in the middle
print(countriesList)


#set countries
print("----------------- Using a SET ----------------- ")
countriesSet = {"Mexico", "Canada", "USA"} #Create a set with 3 countries
print(countriesSet)
countriesSet.add("UK") ##Add an country at the end, Add doesn't guarantee the order
print(countriesSet)
countriesSet.remove("UK") #remove by index, indexing is not supported
print(countriesSet)
countriesSet.update(["UK"]) #add a country in the middle of the set, Update does not guarantee the order
print(countriesSet)
