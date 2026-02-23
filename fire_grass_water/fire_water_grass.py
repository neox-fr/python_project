
import random

option= ["fire", "water", "grass"]

def function_choices(option):
    player_choice=input("enter fire water or grass:")
    
    computer_choice=random.choice(option)
    choices={"player":player_choice, "computer":computer_choice}
    return choices

def check(player, computer, option):
    print(f"player chose {player} and computer chose {computer}")
    if player not in option:
        return "invalid choice"
    elif player == computer:
        return "draw"
    elif player == "fire":
        if computer == "grass":
            return "fire burns grass so you win"
        else:
            return "water stops fire so you lose"
    elif player == "water":
        if computer == "fire":
            return "water stops fire so you win"
        else:
            return "water has no effect on grass so you lose"
    elif player == "grass":
        if computer == "fire":
            return "fire burns grass so you lose"
        else:
            return "water has no effect on grass so you win"

choices=function_choices(option)
result=check(choices["player"], choices["computer"],option)
print(result)