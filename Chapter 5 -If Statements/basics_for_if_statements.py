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