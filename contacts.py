def add_contact(contacts):
    name=input("enter name:")
    phone=input("Enter phone number:")
    email=input("Enter email:")
    address=input("Enter address:")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully.")
def view_contacts(contacts):
    if contacts:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}). Name:{contact['name']}, phone:{contact['phone']}")
    else:
        print("No contacts found.")
def search_contacts(contacts):
    search_term=input("Enter name or phone number to search:")
    results=[contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if results:
        for contact in results:
            print(f"Name:{contact['name']}, phone:{contact['phone']},Email:{contact['email']}, Address:{contact['address']}")
    else:
        print("No contacts found.")
def update_contact(contacts):
    name=input("Enter the name of the contact to update:")
    for contact in contacts:
        if contact in contacts:
            if contact['name'].lower()==name.lower():
                contact['name']=input(f"Enter new name ({contact['name']}):")
                contact['phone']=input(f"Enter new phone number ({contact['phone']}):")
                contact['email']=input(f"Enter new email ({contact['email']}):")
                contact['address']=input(f"Enter new address ({contact['address']}):")
                print("Contact updated successfully.")
                return
    print("Contact not found.")
def delete_contact(contacts):
    name=input("Enter the name of the contact to delete:")
    for contact in contacts:
        if contact['name'].lower()==name.lower():
            contacts.remove(contact)
            print("contact deleted successfully.")
            return
    print("contact not found.")
def main():
    contacts=[]
    while True:
        print("\n Contacts management system")
        print("1.Add contact")
        print("2.view contact list")
        print("3.search contact")
        print("4.Update contact")
        print("5.Delete contact")
        print("6.Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            add_contact(contacts)
        elif choice=='2':
            view_contacts(contacts)
        elif choice=='3':
            search_contacts(contacts)
        elif choice=='4':
            update_contact(contacts)
        elif choice=='5':
            delete_contact(contacts)
        elif choice=='6':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()