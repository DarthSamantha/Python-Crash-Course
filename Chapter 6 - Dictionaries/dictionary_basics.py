alien_0 = {'colour': 'purple', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_postion'] = 25

for key, value in alien_0.items():
    print(f"Key: {key} Value: {value}")

new_points = alien_0['points']
print(f"Congrats you just earned {new_points} points!")

alien_0['colour'] = 'black'
print(f"The alien is now the colour {alien_0['colour']}")

del alien_0['points']
print(alien_0)

# get() method requires a key as a first argument
# 2nd optional argument is if value doesn't exist

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

rachels_dictionary = {
    'first_name': 'Rachel',
    'last_name': 'Millar',
    'age': '25',
    'city': 'Auckland'
}

print(rachels_dictionary['age'])
print(f"{rachels_dictionary['first_name']} lives in {rachels_dictionary['city']}")

for key, value in rachels_dictionary.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print(f"\n{rachels_dictionary.items()}")
print("\n")

for key in rachels_dictionary.keys():
    print(key)

for key in rachels_dictionary:
    print(key)

favourite_foods = {
    'Rachel': 'chips',
    'Debbie': 'chocolate',
    'David': 'chips',
    'Random': 'carrots'}

family = ['Rachel', 'Debbie', 'David']

for name in favourite_foods:
    print(f"Hi, {name}.")
    
    if name in family:
        food = favourite_foods[name].title()
        print(f"\t{name}, I see you love {food}")

for name in sorted(family):
    print(f"{name} thank you for taking the poll")

for food in favourite_foods.values():
    print(f"Top food condendant is: {food}")

# set() method will remove duplicate values, so only print unique
# build a set directly using braces (without key value pairs)

food = {'chips', 'chocolate', 'carrots', 'chips'}
print(food)

beaches = {'Raglan': 'Waikato', 'Waihi': 'Bay of Plenty', 'Mission Bay': 'Auckland'}
for key, value in beaches.items():
    print(f"{key} is located in {value}.")

for key in beaches:
    print(key)

favourite_languages = {
    'sam': 'java',
    'ben': 'go',
    'rachel': 'c'
}

names_for_poll = ['sam', 'ben', 'debbie']

for name in favourite_languages:
    if name in names_for_poll:
        print(f"Thank you {name.title()} for taking the poll!")
    else:
        print(f"Hi {name.title()}, please take the poll")

for name in names_for_poll:
    if name in favourite_languages:
        print(f"Thank you {name.title()} for taking the poll!")
    else:
        print(f"Hi {name.title()}, please take the poll") 















