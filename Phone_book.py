import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = {}
    
while True:
    print("\n--- Phone Book ---")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    print("6. Edit contact")
    print("7. Count contacts")
    print("8. Delete all contacts")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name (or type stop):")
        if name.lower() == "stop":
            break
        if name in contacts:
            print("contact already exists!")
            continue

        while True:
            phone = input("Enter 10-digit phone num:")
            if phone.isdigit() and len(phone) == 10:
                contacts[name] = phone
                print("contact added.")
                break 
            else:
                print("Invalid num!")

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name} - {phone}")

    elif choice == "3":
        search_name = input("Enter name to search:")

        found = False
        for name in contacts:
            if name.lower() == search_name.lower():
                print("phone", contacts[name])
                found = True
                break
        if not found:
            print("contact not found!")

    elif choice == "4":
        name = input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("deleted successfully!")
        else:
            print("contact not found ")

    elif choice == "5":
        print("goodbuy!")
        break

    elif choice == "6":
        name = input("Enter name to edit:")
        if name in contacts:
            while True:
                new_phone = input("Enter new 10-digit num:")
                if new_phone.isdigit() and len(new_phone) == 10:
                    contacts[name] = new_phone
                    print("number updated.")
                else:
                    print("Invalid num!")

    elif choice == "7":
        print("Total contacts", len(contacts))

    elif choice == "8":
        contacts.clear()
        print("All contacts deleted")

    else:
        print("Invalid choice!")