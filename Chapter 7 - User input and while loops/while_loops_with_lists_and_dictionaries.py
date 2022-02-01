#You shouldn't modify items inside a for loop
#because its hard to keep track of the items in the list

unconfirmed_users = ['sam', 'ben', 'rachel']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['cat', 'dog', 'cat', 'pig']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
