def save_names(names, filename):
    with open(filename, "w") as file:
        for name in names:
            file.write(name + "\n")


def load_names(filename):
    names = []
    try:
        with open(filename, "r") as file:
            for line in file:
                names.append(line.strip())
    except FileNotFoundError:
        pass
    return names


def print_items(items):
    count = 1
    for item in items:
        if item:
            print(f"{count}. {item}")
            count += 1
#add a loop for entering number even when wrong entry
def delete_name(filename, names):
    if not names: 
        print("No names to delete"); 
        return
    while True:
        print_items(names)
        number = input("enter number (or q to cancel): ")
        if number == "" or number.lower() == "q":
            break
        if number.isdigit():
            index = int(number) - 1
            if 0 <= index < len(names):
                removed = names.pop(index)
                print(f"{removed} Deleted")
                save_names(names, filename)
                break
            else:
                print("Number not on list")
        else: 
            print("enter a number")

    

filename = "names.txt"
names = load_names(filename)

while True:
    print("\nMenu:")
    print("1. View names")
    print("2. Add a name")
    print("3. Delete a name")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nCurrent names:")
        print_items(names)

    elif choice == "2":
        new_name = input("Enter a name: ")
        if new_name:
            names.append(new_name)
            save_names(names, filename)
            print("Name added.")

    elif choice == "3":
        delete_name(filename, names)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

