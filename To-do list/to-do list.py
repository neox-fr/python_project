def main():
    groceries = []
    print(
        """To-do List Menu:
        1. View Tasks
        2. Add a Task
        3. Remove a Task
        4. Exit"""
    )
    def choice():
        
        while True:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print(groceries)
            elif choice == 2:
                item = input("Enter a item:")
                groceries.append(item)
            elif choice == 3:
                item = input("enter the item You want to remove:")
                if item in groceries:
                    groceries.remove(item)
            elif choice == 4:
                break
            else:
                print("invalid input")
    choice()

main()