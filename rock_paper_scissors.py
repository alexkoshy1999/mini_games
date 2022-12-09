import random

def get_choices():
    player_choice = input("Enter a Choice (rock, paper, scissors, exit):")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer":computer_choice,"game":player_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "Rock smashes Scissors! You win"
        else:
            return "Paper covers rock! You lose."
    elif player=="paper":
        if computer=="rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
    elif player=="scissors":
        if computer=="rock":
            return "Rock smashes Scissors! You lose!"
        else:
            return "Scissors cut paper! You win."

game = input("Enter \"play\" or \"exit\":")
while game == "play":
    choices = get_choices()
    if choices["game"]=="exit":
        break
    result = check_win(choices["player"],choices["computer"])
    print(result)
    


