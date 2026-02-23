import random

def main():
    while True:
        choice = input("Roll the dice? (y/n):").lower()
        if choice == "y":
            random_x = random.randint(1, 6)
            random_y = random.randint(1, 6)
            print(f'({random_x}, {random_y})')
        elif choice == "n":
            print(
                f"Thank you for playing the game!"
            )
            break
        else:
            print("Invalid choice!")

main()
