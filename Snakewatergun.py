import random
print("Hello welcome to the game")
lst=["snake", "water", "gun"]

chances=10
no_of_chances=0
player =0
computer=0

while no_of_chances<chances:
    print("enter a choice: snake, water, gun")
    ch = input()
    print(f"you selected {ch}")
    comp = random.choice(lst)
    print(f"Computer selected {comp}")

    if ch==comp:
        print(f"your guess is {ch} and computers:{comp}")
        print("it is a tie-no points")
    if ch=="gun" and comp=="snake":
        player=player+1
        print(f"your guess is {ch} and computers:{comp}")
        print(f"Player gets a point . Total points are:{player}")
    elif ch=="snake" and comp=="gun":
        computer=computer+1
        print(f"your guess is {ch} and computers:{comp}")
        print(f"Computer gets a point . Total points are:{computer}")
    elif ch=="water" and comp=="gun":
        player = player + 1
        print(f"your guess is {ch} and computers:{comp}")
        print(f"Player gets a point . Total points are:{player}")
    elif ch=="gun" and comp=="water":
        computer = computer + 1
        print(f"your guess is {ch} and computers:{comp}")
        print(f"Computer gets a point . Total points are:{computer}")
    elif ch=="snake" and comp=="water":
        player = player + 1
        print(f"your guess is {ch} and computers:{comp}")
        print(f"Player gets a point . Total points are:{player}")
    elif ch=="water" and comp=="snake":
        computer = computer + 1
        print(f"your guess is {ch} and computers:{comp}")
        print(f"Computer gets a point . Total points are:{computer}")
    else:
        print("enter a valid choice")

    no_of_chances=no_of_chances+1
    print(f"{chances-no_of_chances} chances are left out of {chances}")

print("game over")
if player==computer:
    print("it is a tie")
elif player> computer:
    print("player wins")
else:
    print("computer wins")