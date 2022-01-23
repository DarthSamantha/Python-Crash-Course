sam = {'first_name': 'samantha', 'last_name': 'millar', 'age': '27'}
ben = {'first_name': 'ben', 'last_name': 'hollamby', 'age': '36'}
rachel = {'first_name': 'rachel', 'last_name': 'millar', 'age': '25'}

people = [sam, ben, rachel]

for name in people:
    for key, value in name.items():
        print(f"Key: {key} Value: {value}")


favourite_places = {
    'rachel': ['Wellington', 'London'],
    'sam': ['Queenstown', 'Hamilton', 'Auckland']
}

for name, places in favourite_places.items():
    print(f"{name.title()} favourite places are:")
    for favourite_place in places:
        print(favourite_place)
