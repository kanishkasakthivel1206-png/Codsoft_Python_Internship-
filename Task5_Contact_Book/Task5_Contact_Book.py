# CodeSoft Python Programming Internship
# Task 5: Contact Book

contacts = []


def add_contact():
    print("\n===== ADD CONTACT =====")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("\nContact added successfully!")


def view_contacts():
    print("\n===== CONTACT LIST =====")

    if len(contacts) == 0:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print("\nContact", i)
        print("Name    :", contact["name"])
        print("Phone   :", contact["phone"])
        print("Email   :", contact["email"])
        print("Address :", contact["address"])


def search_contact():
    print("\n===== SEARCH CONTACT =====")

    search = input("Enter name or phone number: ").strip().lower()

    found = False

    for contact in contacts:
        if (
            search in contact["name"].lower()
            or search in contact["phone"].lower()
        ):
            print("\nContact Found!")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    print("\n===== UPDATE CONTACT =====")

    phone = input("Enter the phone number of the contact: ").strip()

    for contact in contacts:

        if contact["phone"] == phone:

            print("\nContact found!")
            print("Press Enter to keep the existing value.")

            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email: ").strip()
            new_address = input("Enter new address: ").strip()

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            print("\nContact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n===== DELETE CONTACT =====")

    phone = input("Enter the phone number of the contact: ").strip()

    for contact in contacts:

        if contact["phone"] == phone:

            contacts.remove(contact)

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# Main menu
while True:

    print("\n================================")
    print("         CONTACT BOOK")
    print("================================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")
