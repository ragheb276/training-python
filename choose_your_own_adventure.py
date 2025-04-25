name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the Choose Your Own Adventure game.")

print("You find yourself in a dark forest. There are two paths ahead of you.")
print("Do you want to go left or right?")

choice1 = input("Type 'left' or 'right': ").lower()
if choice1 != "left" and choice1 != "right":
    print("please type 'left' or 'right' next time.")
    quit()
if choice1 == "left":
    print("You encounter a wild beast!")
    print("Do you want to fight it or run away?")
    
    choice2 = input("Type 'fight' or 'run': ").lower()
    
    if choice2 == "fight":
        print("You bravely fight the beast and win! You are a hero!")
    elif choice2 == "run":
        print("You run away safely, but you missed the treasure!")
    else:
        print("please type 'fight' or 'run' next time.")
        quit()
elif choice1 == "right":
    print("You find a treasure chest!")
    print("Do you want to open it or leave it?")
    
    choice2 = input("Type 'open' or 'leave': ").lower()
    
    if choice2 == "open":
        print("You found gold and jewels! You are rich!")
    elif choice2 == "leave":
        print("You walk away, but you missed the treasure!")
    else:
        print("please type 'open' or 'leave' next time.")
        quit()
        
        