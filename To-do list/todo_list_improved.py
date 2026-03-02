def main():
    groceries = []

    while True:
        print("""To-do list Menu:
              1. View Tasks
              2. Add a Task
              3. Remove a Task
              4. Exit
              """)
        try: 
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Invalid, Enter (1-4)")
            continue

        if choice ==1:
            if groceries:
                for i, task in enumerate(groceries, start=1):
                    print(f'{i}.{task}')
            else:
                print("No tasks yet")
        elif choice == 2:
            num = input("Enter a task you want to enter:")
            groceries.append(num)
            print(f"{num} has been added")
        elif choice == 3:
            if groceries:
                for i, task in enumerate(groceries, start=1):
                    print(f'{i}.{task}')
                try:
                    num = int(input("Enter the number which you want to remove:"))
                    if 1 <= num <= len(groceries):
                            removed = groceries.pop(num - 1)
                            print(f'{num}.{removed} has been removed')
                    else:
                        print("enter a valid number")
                except ValueError:
                    print("invalid")
                    continue
            else:
                print("No tasks to remove")
        elif choice == 4:
            print("exiting......")
            break
        else:
            print("Invalid choice. Try again.")

main()