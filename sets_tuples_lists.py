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

cars=["Ford", "Volvo", "BMW", "Cadillac", "Chevrolet", "Porsche", "Jaguar" ]
# add 4 new cars in the list
cars.append("Honda")
#print out the list of cars in an f-string
print(f"The acrs in the list are{cars}")
# replace the last element in the list
cars[-1]="Austin Martin"
#print out the list of cars in an f-string
print(f"The acrs in the list are{cars}")
#replace 3rd element in the list with another car
cars[2]="Genesis"
#print out the list of cars in a f-string
print(f"The acrs in the list are{cars}")
#remove 3rd element in the list
cars.remove("Cadillac")
#print out the list of cars in an f-string
print(f"The acrs in the list are{cars}")
#check if the list contains the car "Ford"
print("Ford" in cars)
#print out the results of cars in an f-string
print(f"The acrs in the list are{cars}")

for car in cars:
    requestCar= input("Enter a car: ")
    cars.append(requestCar)
    print(f'The cars in the list are: {cars}')
    if len(cars) == 10:
        print("You have reached the maximum nummbers of cars")
        break