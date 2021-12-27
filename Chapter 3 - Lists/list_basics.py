food = ['chocolate', 'apple pie', 'cheese', 'pasta']
print(food)

print(food[0])
print(food[-1])

message = f"My favourie from this list is {food[1].title()}"
print(message)

food[0] = 'twirl'
print(food)



food.append('banana')
print(food)

food.insert(1, 'cookie')
print(food)

del food[4]
print(food)

popped_food = food.pop()
print(food)
print(popped_food)

food.remove('cheese')
print(food) 
# remove only deletes the first value of the word in the list

cars =['bmw', 'mazda', 'audi', 'tesla']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#sort a list temporarily with sorted()

cars =['bmw', 'mazda', 'audi', 'tesla'] 
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print(len(cars))