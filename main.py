cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
}

print("Welcome to my cat game!")

name = input("Enter name:").capitalize()
colour=input("Enter colour:")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats")

    if option == '1':
        # change the cat's attributes here
        pass
    elif option == '2':
        pass
    # elif ...
    else:
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        pass
    # elif ...
    