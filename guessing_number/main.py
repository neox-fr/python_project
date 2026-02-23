import random
def main():
    number = random.randint(1,100)
    while True:
        player_choice = int(input("Guess the number between (1 to 100):"))
        if player_choice == number:
            print("congrats you guessed the number!")
            break
        elif player_choice > number:
            print("the number is high, go lower!")
        elif player_choice < number:
            print("the number is low, go higher!")
        else:
            print("invalid input!, choice must be a integer between (1 to 100)")
main()
