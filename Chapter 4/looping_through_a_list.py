Cities = ['auckland', 'wellington', 'queenstown', 'taupo']
for x in Cities:
    print(f"{x.title()}, next place to visit")
    print(f"I can't wait to visit {x.title()}.\n")

print("for loop ended\n")

Pizza = ['Hawaiian', 'Meatlovers', 'Pepperoni']
for pizza in Pizza:
    print(f"I like {pizza} Pizza")

print("\nPizza is amazing\n")

Animals = ['Dog', 'Cat', 'Pig', 'Goat']
for Animal in Animals:
    print(f"A {Animal} would make a great pet")

print("\nAny of these would make a great pet\n")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

squares = []
for value in range(0,10):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(0, 10):
    squares.append(value ** 2)

print(squares)

digits =[1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value **2 for value in range(1,11)]
print(squares)

