# # collections = single "variable"used to store multiple values
# # Lists = [] ordered and changeable. Duplicates OK
# # Set = {} unordered and unmutable, but Add/Remove OK. NO duplicates
# # Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits=["apple", "orange","banana", "coconut","strawberries", "kiwi", "papaya", "watermelon"]
# print(fruits[0])   # 0 = apple
# print(fruits[0:3]) # numbers 0-3
# print(fruits[::2]) # gives every second element
# print(fruits[::-1]) # makes it backwords

# for fruit in fruits:
#     print(fruit)
# #interation
# #DONT HAVE A ONE LETTER VARIABLE (name it after the variable but singular)
# #loops through the whole thing

# print(dir(fruits)) # DIR lists all the attributes for the list

# # print(help(fruits)) #gives you help with documentation

# print(len(fruits)) # gives the length of the variable

# print("apple" in fruits)
# print("pineapple" in fruits)
# # Tells us if its in there

# fruits[0]="pineapple" # changes the value of 0 in the list

# fruits.append("pineapple") # adds element to the end of the list


# fruits.remove("apple") # removes element

# fruits.instert(0, "pineapple") # inserts the variable in the spot and pushes the other variables

# fruits.sort() # in alphabetical order
# fruits.reverse() # reverse
# fruits.clear # all the elements are gone/cleared
# print(fruits.index("apple"))

# cars=["Ford", "Volvo", "BMW", "Cadillac", "Chevrolet", "Porsche", "Jaguar" ]
# # add 4 new cars in the list
# cars.append("Honda")
# #print out the list of cars in an f-string
# print(f"The acrs in the list are{cars}")
# # replace the last element in the list
# cars[-1]="Austin Martin"
# #print out the list of cars in an f-string
# print(f"The acrs in the list are{cars}")
# #replace 3rd element in the list with another car
# cars[2]="Genesis"
# #print out the list of cars in a f-string
# print(f"The acrs in the list are{cars}")
# #remove 3rd element in the list
# cars.remove("Cadillac")
# #print out the list of cars in an f-string
# print(f"The acrs in the list are{cars}")
# #check if the list contains the car "Ford"
# print("Ford" in cars)
# #print out the results of cars in an f-string
# print(f"The acrs in the list are{cars}")

# for car in cars:
#     requestCar= input("Enter a car: ")
#     cars.append(requestCar)
#     print(f'The cars in the list are: {cars}')
#     if len(cars) == 10:
#         print("You have reached the maximum nummbers of cars")
#         break

    ###### CHALLENGE #####
# create a list of friends
# friends=["Emily W"]
# # add 4 new friends to the list by requesting the user to enter names
# for friend in friends:
#          requestfriends= input("Enter a friends name : ")
#          friends.append(requestfriends)
#          print(f'The list of friends are: {friends}')
#          if len(friends) == 5:
#              print("You have reached the maximum nummbers of friends")
#              break
    
   
    
# print out the list of friends in a f_string
# replace the last element in the list with another friends
# print out the list of friends in a f_string
# replace the 3rd element in the list with another string
# print out the list of friends in a f_string
# insert a new friends in the 2nd position
# print out the list of friends in a f_string
         
###############sets###############
#sets are unordered and unindexed
#they ar defined using curly brackets
#they do not allow duplicates
         
fruits={"apple", "banana", "mango", "cherry", "watermelon"}
print(fruits)
# print(dir(fruits)) #method used with sets
# print(help(fruits)) #documentation/method used with sets
# print(len(fruits)) #number of elements in the set
# print("volvo" in fruits) #check if elemets are in the set
print(fruits.add("orange"))
print(fruits)
print(fruits.add("kiwi"))
print(fruits)
#add multiple elements to the set
print(fruits.update(["orange", "kiwi", "pineapple"]))
print(fruits)
#remove an element from the set
print(fruits.remove("banana"))
print(fruits)
print(fruits.pop()) #removes last element
print(fruits)
print(fruits.clear()) #clears the set
print(fruits)
#sets are used to store elements that shouldnt be changed
#doesnt matter the order of the elements
#example : a collection of unique items
social_security_numbers= {123456789, 987654321, 1234567890}
#remove the last element in this set
print(social_security_numbers.pop())
#add another ss number
print(social_security_numbers.add(777777777))
print(social_security_numbers)
print(social_security_numbers.add(666666666))
print(social_security_numbers)

##########tuples#############
#tumples are immutable and are defined using parenthesis
#create a tuple called my_tuple with the following values
example_tuple= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(example_tuple)
print(example_tuple.count(2)) #counts the number of times 2 appears
print(dir(example_tuple)) #attributes used with tuples
print(help(example_tuple)) #documentation methods that can be used
print(len(example_tuple)) #number of elements in the tuple
print(2 in example_tuple) #check if an elements is in a tuple
#tuples are useful when you want to store a collection of items that wont be changed
#likes weeks or months
#finding index in the value of tuples
# print(example_tuple.index(2))
# lymeric="peter pipe picked a peck of pickled peppers"
# #convert the string to a tuple
# #split it first
# lymeric_tuple=tuple(lymeric.split())
# print(lymeric_tuple)
# #find how many times the letter "peppers" is in the tuple
# print(lymeric_tuple.count("peppers"))

#loops with tuples
for item in example_tuple:
    print(item)

################dictionary#############
#dictionaries are unordered, changable, and indexed
#they are defined using curly brackets
#they have keys and values
#a collection of {key:value} pairs, no duplicates
#keys are unique
#values can be of any data type
capitals={"Kenya":"Nairobi",
          "Uganda":"Kampala",
          "Tanzania":"Dodoma",
          "Rwanda":"Kingali",
          "China":"Beijing",
          "USA" :"Washignton DC"}
print(capitals)
print(dir(capitals)) #attributes that are used in dictionaries
print(help(capitals)) #documentation methods used with dictionaries
print(len(capitals)) #number of items in a dictionary
#if you want to check the value of a key in the dictionary
print(capitals["Kenya"])
print(capitals.get("Kenya"))
#add an item to the dictionary #Two ways
capitals["South Africa"]="Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
#add 3 more countries and theire capitals to the dictionary
capitals.update({"France":"Paris", "Germany":"Berlin", "Italy":"Berlin"})
print(capitals)

capitals.pop("China") #remove an item from the dictionary
print(capitals)
#clears dictionary
#capitals.clear() # do not run this
#loop through the dictionary to get the keys
for key in capitals :
    print(f"these are the {key}")

#print the values in the dictionary
for value in capitals.values():
    print(value)

#print the key value pairs in the dictionary
items=capitals.items() #key value pairs
for key, value in items :
    print(f"{key} is the capitol of {value}")
    

