import random

player_points = 0
computer_points = 0

while True:

    list = ["rock","paper","scissors"]
    computer_move = random.choice(list)

    print()
    player_move = input("Choose between [r]ock, [p]aper and [s]cissors or [l]eave game: ")

    if player_move.lower() == "r":
        player_move = list[0]
    elif player_move.lower() == "p":
        player_move = list[1]
    elif player_move.lower() == "s":
        player_move = list[2]
    elif player_move.lower() == "l":
        break
    else:
        raise SystemExit("Input is invalid! Try again...")

    print()
    print(f"You chose {player_move}")
    print(f"The computer chose {computer_move}")

    if player_move == computer_move:
        print("Game ended with a draw")

    elif player_move == "rock":
        if computer_move == "scissors":
            print("You won!")
            player_points+=1
        else:
            print("You lost! Try again...")
            computer_points+=1

    elif player_move == "paper":
        if computer_move == "rock":
            print("You won!")
            player_points+=1
        else:
            print("You lost! Try again...")
            computer_points+=1
    elif player_move == "scissors":
        if computer_move == "paper":
            print("You won!")
            player_points+=1
        else:
            print("You lost! Try again...")
            computer_points+=1


print()
print(f"Your points: {player_points}")
print(f"Computer points: {computer_points}")

if player_points>computer_points:
    print("You won! Congratulations!")
elif player_points==computer_points:
    print("Overall game ended with a draw!")
elif player_points<computer_points:
    print("You lost!")

input("Press [Enter] to exit")