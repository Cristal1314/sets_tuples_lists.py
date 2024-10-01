#collection = single "varible" used to store multiple values
# List = [] ordered and changeable. Duplicates Ok
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Table = () ordered and unchangeable. Duplicates OK. FASTER


#LISTS
#---------------------------------------------------------------------------------------------------------------------------
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
print(fruits.index("apple"))

print(fruits)
# # print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)



 #Challenge
#----------------------------------------------------------------------------------------------------------------------------
# cars = ["bmw", "maserati","audi","mercedes", "ferrari"]
# print(f"these are lists of {cars}")
# print(f"the first car is {cars[0]}")


# #changing the value of the lists
# cars [0] = "toyota"
# print(f"the first cars is {cars[0]}")


# print(f"the last car is {cars[-1]}")
# cars[-1] = "Lamborghini"
# print(f"the lst car is {cars[-1]}")


# #adding a new value to the list
# cars.append("bugatti")
# print(cars)
# cars.remove("maserati")
# print(cars)


# #looping through the list
# #otherwise called iterating through the list
# for car in cars:
#    #print(len(car))
#    #print(car)
# #    carRequest = input("add a new car please: ")
# #    cars.append(carRequest)
#    print(len(car))
#    print(cars.uppercase())
#    print(cars)
   # if len(cars) > 10:
   #    break


# #challenge
# #create a list of friends
# # Make sure the initals list is none
# friends = ["Jazmin", "Lesly","Melissa","Flor", "Aleidy"]
#  # add a new friends to the list, add at least 5 friends
# print(friends)
#  # remove a friend
# friends.remove("Aleidy")
# # insert a friends at specific index mabybe 2
# print(friends.append("Junior"))
# # print the list of friends 
# print(friends)
# # loop through the list and print the friends name
# print(friends.sort)
# # see if a particular friend is in the list (Boolean values)
# print(friends)
# # if the list is greater then 10 break the loop
# for friend in friends:
#    print(friends)
#    if len(friends) > 10:
#       break


# SETS
#--------------------------------------------------------------------------------------------------------------
fruits ={"apple", "orange", "banana", "coconut", "strawberries", ""}
# print(dir(fruits)) # prints 
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple", "Mango","Kiwi","Leche") #This adds the fruits that are wanted to hbe added
#fruits.remove("apple") # This will remove the object inside of the perentraces
fruits.pop() # This will make one of the inputs inside be removed random


# # fruits[1] = "pineapple" #I can use vuales to redesign them
# # fruits.append("pineapple") # adds
# # fruits.remove("apple") # remove
# fruits.insert(0, "pineapple")
# # fruits.sort() # this sorts the list
# # fruits.reverse() # reverse
# # fruits.clear() # Just clears the list
# print(fruits.index("apple"))

print(fruits)
# print(fruits[0])
# # print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)




#TUPLE
#--------------------------------------------------------------------------------------------------------------
fruits =("apple", "orange", "banana", "coconut", "strawberries", "")
# print(dir(fruits)) # prints 
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

print(fruits)
for fruit in fruits:
    print(fruits)

#--------------------------------------------------------------------------------------------------------------
# DICITIONERIES


# dictionary = a collection oif {key:value} pairs
#             ordered and changeable. No duplicate\
    


capitals = {"USA" : "Washington",
            "Indian" : "New Delhi" ,
            "Chine" : "Beijing",
            "Russia" : "Moscow",}


# print(dir(capitals))
# print(help(capitals))
#print(capitals.get("USA"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")


capitals.updata("Germeny" ; "Berlin",
                "Meixco": "Cuidad de Meico",
                "Chile": "Santigo")
capitals.updata({"USA": "Detriit"})
capitals.pop("China")
capitals.popitem()

keys = capitals.keys()
print(keys)
for key in capitals.keys():
     print(keys)

values = capitals.values
for value in capitals.value():
    print(value)



items = capitals.items
for key , value in capitals.value:
    print(f"{key}: {value}")



print(capitals)