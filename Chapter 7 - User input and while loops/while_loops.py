from turtle import title


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something and I will repeat it back to you:  "
prompt += "\nEnter 'quit to end the program "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#Flag

active = True
while active:
    message = input(prompt) 

    if message == 'quit':
        active = False
    else:
        print(message)



 #Break

prompt = "\nWhat cities have you visited:"
prompt += "\nEnter quit to end "
while True:
     city = input(prompt)

     if city == 'quit':
        break
     else:
         print(f"I'd love to go to {city.title()}!")

#Continue - goes back to the beginning

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

prompt = "\nPlease enter pizza toppings"
prompt +="\nEnter quit when you have finished\n"

while True:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break
    else:
        print(f"Adding {pizza_topping.title()} to Pizza")
