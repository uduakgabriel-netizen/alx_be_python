def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        
        choice = input("Enter your choice: ")

        if not choice.isdigit():
          print("Invalid input. Please enter a number between 1 and 4.")
          continue

        choice = int(choice)

        if choice == 1:
            # Prompt for and add an item
            item_name = input("Enter the item to add: ")

            if item_name:
                if item_name in shopping_list:
                    print(f"The {item_name} is already on the list")
                else:
                    shopping_list.append(item_name)
                    print(f"{item_name} added succesfully!")
            else: 
                print("You must enter an item!")
            pass
        
        elif choice == 2:
            # Prompt for and remove an item
            item_name = input("Enter the item to remove: ")

            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print(f"{item_name} removed successfully!")
            else:
                print(f"{item_name} not found in shopping list.")
            pass
        
        elif choice == 3:
            # Display the shopping list
            if shopping_list != []:
              print("Shopping list item(s):")
              for item in shopping_list:
                print(f"- {item}")
            else:
                print("They are no items on the shopping list. Enter 1 to add an item.")
            pass
        
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
      
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":

    main()