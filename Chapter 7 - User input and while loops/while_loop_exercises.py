prompt = "\nPlease enter pizza toppings"
prompt +="\nEnter quit when you have finished\n"


while True:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break
    else:
        print(f"Adding {pizza_topping.title()} to Pizza")

active = True
while active:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        active = False
    else:
        print(f"Adding {pizza_topping.title()} to Pizza")


age = input("\nWhat is your age? ")
age = int(age)

if age < 3:
    print("\nYour movie ticket is free")
elif age >= 3 & age < 12:
    print("\nYour movie ticket is $10")
else:
    print("\nYour movie ticket is $15")

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

