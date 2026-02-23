import random
number_guess = random.randint(1,100)
while True:
    try:
        guessing = int(input('Guess the number (1 - 100):'))
        if guessing < number_guess:
            print("number is low, go higher!")
        elif guessing > number_guess:
            print("number is high, go lower!")
        else: 
            print("Congrats!, You guessed correct")
            break

    except ValueError:
        print("Enter a valid number")
