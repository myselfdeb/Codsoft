import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")

def view_contact_list(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts saved yet.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print("---" * 10)

def search_contact(contacts):
    print("\n--- Search Contact ---")
    search_term = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details['phone']:
            print(f"\nName: {name}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print(f"  Address: {details['address']}")
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact(contacts):
    print("\n--- Update Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").strip()
    if name_to_update in contacts:
        print(f"\n--- Current details for '{name_to_update}' ---")
        print(f"Phone: {contacts[name_to_update]['phone']}")
        print(f"Email: {contacts[name_to_update]['email']}")
        print(f"Address: {contacts[name_to_update]['address']}")

        print("\n--- Enter new details (leave blank to keep current) ---")
        new_phone = input(f"New Phone ({contacts[name_to_update]['phone']}): ").strip()
        new_email = input(f"New Email ({contacts[name_to_update]['email']}): ").strip()
        new_address = input(f"New Address ({contacts[name_to_update]['address']}): ").strip()

        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email
        if new_address:
            contacts[name_to_update]['address'] = new_address

        save_contacts(contacts)
        print(f"\nContact '{name_to_update}' updated successfully!")
    else:
        print(f"Contact '{name_to_update}' not found.")

def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        save_contacts(contacts)
        print(f"\nContact '{name_to_delete}' deleted successfully!")
    else:
        print(f"Contact '{name_to_delete}' not found.")

def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("---" * 10)

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()