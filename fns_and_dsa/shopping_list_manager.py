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

        if choice == 1:
            item = input("Enter the item: ").lower()
            shopping_list.append(item)
            print(f"{item} successfully added!")

        elif choice == 2:
            item = input("Enter the item to be removed:").lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed successfully!")
                
            else:
               print("Error: Item not in shoping list!")
                
        elif choice == 3:
            print(f"Here is the current list: {shopping_list}")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()