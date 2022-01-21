cars = ['audi', 'bmw', 'mazda', 'toyota']
for car in cars:
    if car == 'audi':
        print(f"This car is an {car.title()}")
    else:
        print("This car is not an Audi")

suv = 'Range Rover'
print(suv.lower() == 'range rover')
print(suv.lower() != 'range rover')

age = 27
print(age > 30)
print(age < 30 and age > 5)
print(age < 30 or age > 5)
 
food = ['pasta', 'chocole', 'ice cream', 'pizza']
print('pasta' in food)
print('pasta' not in food)

if 'apple pie' not in food:
    print("Apple pie should be in the list")

game_active = True

age = 12
if age > 20:
    print("Age is greater than 20")
elif age < 15:
    print("Age is less than 15")
else:
    print("Age is between 15 and 20")

age = 12
if age < 5:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission price is ${price}.")
#Else is option, it's a catch all

#To test multiple conditions use if statements
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding Mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding Pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("Finished making you pizza")

requested_toppings = ['mushrooms', 'extra cheese', 'mushrooms', 'green peppers']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making you pizza.")

#Checking that a list is not empty
requested_toppings = []
if requested_toppings:
#^ Python will return true if the list is not empty 
    for requested_topping in requested_toppings:
        print(f"Adding {requested_toppings}.")
    print("Finished making you pizza")
else:
    print("Are you sure you want a plan pizza?")

available_toppings = ['mushrooms', 'olives', 'extra cheese', 'pineapple']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to pizza.")
    else:
         print(f"Sorry that is not an available topping.")
print("Finished making pizza.")

