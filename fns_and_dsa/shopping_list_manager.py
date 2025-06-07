def display_menu():
    """Displays the main menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    """Prompts the user for an item and adds it to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    else:
        print("Item cannot be empty. Please enter a valid item.")

def remove_item(shopping_list):
    """Prompts the user for an item and removes it from the shopping list."""
    if not shopping_list:
        print("The shopping list is currently empty. Nothing to remove.")
        return

    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the list.")

def view_list(shopping_list):
    """Displays the current items in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []  # Initialize an empty shopping_list as required

    while True:
        display_menu()  # Call the display_menu function
        try:
            choice = int(input("Enter your choice: "))  # Read choice as an integer
            if choice == 1:
                add_item(shopping_list)
            elif choice == 2:
                remove_item(shopping_list)
            elif choice == 3:
                view_list(shopping_list)
            elif choice == 4:
                print("Exiting Shopping List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()