catname=input("What is your cat's name?").capitalize()
cat_colour=input("What colour would you like your cat to be?")
intelligence=10
energy=50
weight=10

while True:
    action=input(f"What would you like to do with {catname}? (play, train, feed, sleep, view_stats,)").capitalize()
    if action == "Play":
        if energy<3:
            print(f"{catname} doesnt have enough energy right now.")
        else:
            energy-=3
    elif action == "Train":
        if energy<5:
            print(f"{catname} cannot train right now. Not enough energy.")
        else:
            energy-=5
            intelligence+=3
    elif action == "Feed":
        energy+=4
        weight+=2
    elif action == "Sleep":
        energy+=5
    elif action == "View_stats":
        print(f"{catname} is {cat_colour}\n{energy} energy left\nThey weigh {weight} kg\n{intelligence} intelligence")