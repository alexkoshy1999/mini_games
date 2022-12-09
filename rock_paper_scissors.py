import random

def get_choices():
    player_choice = input("Enter a Choice (rock, paper, scissors, exit):")
    if player_choice in ("rock","paper","scissors","exit"):
        options = ["rock","paper","scissors"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer":computer_choice,"game":player_choice}
        return choices
    else:
        choices = {"player": 0,"game":0}
        print("Enter a valid choice!!!!!")
        return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return 0,"It's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return 'p',"Rock smashes Scissors! You win"
        else:
            return 'c',"Paper covers rock! You lose."
    elif player=="paper":
        if computer=="rock":
            return 'p',"Paper covers rock! You win!"
        else:
            return 'c',"Scissors cut paper! You lose."
    elif player=="scissors":
        if computer=="rock":
            return 'c',"Rock smashes Scissors! You lose!"
        else:
            return 'p',"Scissors cut paper! You win."
p,c,g=0,0,0
game = input("Enter \"play\" or \"exit\":")
while game == "play":
    choices = get_choices()
    if choices["game"]=="exit":
        break
    if  choices["game"]!=0:
        point,result = check_win(choices["player"],choices["computer"])
        print(result)
        if result!="None":
            g+=1
        if point=='p':
            p+=1
        if point=='c':
            c+=1
        print(f"Total game played {g}")
        print(f"Player Score: {p}")
        print(f"Computer Score: {c}")

