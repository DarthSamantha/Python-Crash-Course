alien_0 = {'colour': 'purple', 'points': '5'}
alien_1 = {'colour': 'black', 'points': '5'}

aliens = [alien_0, alien_1]

for alien in aliens:
    print(alien)

# Make 10 purple aliens

aliens = []
for alien_number in range(20):
    new_alien = {'colour': 'purple', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

# A list in a dictionary
# Any time you want more than one value associated to the key

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']} crust pizza " 
    "with the following toppings: ")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favourite_languages = {
    'ben': ['powershell', 'go'],
    'sam': ['bash', 'java']
}

for name, langugages in favourite_languages.items():
    print(f"\n{name.title()} favourite languages are:")
    for language in langugages:
        print(f"\t{language.title()}")

# A dictionary in a dictionary

users = {
    'sam': {
        'first': 'sam',
        'last': 'millar',
        'age': '27'
    },
    'ben': {
        'first': 'ben',
        'last': 'hollamby',
        'age': '36'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    
    print(f"\tFull name: {full_name.title()}")

