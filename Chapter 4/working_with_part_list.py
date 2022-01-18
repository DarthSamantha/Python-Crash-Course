players = ['Sam', 'Ben', 'Rachel', 'Debbie', 'David']
print(players[0:3])
print(players[:3])
print(players[2:])
print(players[-3:])

#Including a third value tells Python how many to skip between items
print(players[0:4:2])

#Looping through a slice
for player in players[0:3]:
    print(player)

#Copying a list
my_foods = ['Pizza', 'Rice', 'Chocolate', 'Apple Pie']
copy_of_my_foods = my_foods[:]
print(copy_of_my_foods)

copy_of_my_foods.append('Ice Cream')
print(copy_of_my_foods)
print(f"{my_foods}\n")

#Sometimes you'll want to modify a list that can't be changed.  
#Values that cannot change are immutable 
#An immutable list is called a tuple
#A tuble uses parentheses instead of square brakets

dimensions = (200, 50)

buffet_menu = ('toast', 'cereal', 'pancakes', 'eggs', 'fruit')
print("The foods served at our buffet are:")
for food in buffet_menu:
    print(food)

# buffet_menu[1] = 'porridge'

buffet_menu = ('muffins', 'cereal', 'pancakes', 'porridge', 'fruit')
print("\nThe foods served at our buffet are:")
for food in buffet_menu:
    print(food)

