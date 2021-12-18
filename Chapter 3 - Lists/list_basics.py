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