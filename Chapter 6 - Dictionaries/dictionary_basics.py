alien_0 = {'colour': 'purple', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"Congrats you just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_postion'] = 25
print(alien_0) 

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
    print(f"Hi, {name}")
    
    if name in family:
        food = favourite_foods[name].title()
        print(f"\t{name}, I see you love {food}")











