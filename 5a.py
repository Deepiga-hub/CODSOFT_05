'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found.")

    def search_contacts(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def user_interface():
    contact_book = ContactBook()
    print("Welcome to Contact Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contacts(keyword)
            if found_contacts:
                print("Search Results:")
                for i, contact in enumerate(found_contacts, 1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            index = int(input("Enter index of contact to update: "))
            if 1 <= index <= len(contact_book.contacts):
                name = input("Enter updated name: ")
                phone_number = input("Enter updated phone number: ")
                email = input("Enter updated email: ")
                address = input("Enter updated address: ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_book.update_contact(index, updated_contact)
            else:
                print("Invalid contact index.")
        elif choice == "5":
            index = int(input("Enter index of contact to delete: "))
            contact_book.delete_contact(index)
        elif choice == "6":
            print("Thank you for using Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    user_interface()
