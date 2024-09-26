#collection = single "varible" used to store multiple values
# List = [] ordered and changeable. Duplicates Ok
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Table = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "strawberries", ""]
# print(dir(fruits)) # prints 
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[1] = "pineapple" #I can use vuales to redesign them
# fruits.append("pineapple") # adds
# fruits.remove("apple") # remove
fruits.insert(0, "pineapple")
# fruits.sort() # this sorts the list
# fruits.reverse() # reverse
# fruits.clear() # Just clears the list

# # print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)