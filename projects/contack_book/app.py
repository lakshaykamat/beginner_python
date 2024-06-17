import csv
import os

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Contact:
    file_path = 'contacts.csv'

    def __init__(self, name, contact_no):
        if Contact.is_valid_contact_no(contact_no) and Contact.is_exist(name) == False:
            self.__name = name
            self.__contact_no = contact_no
            self.save()
        else:
            print("Invalid Contact number or contact is already saved")
            return

    def get_name(self):
        return self.__name

    def get_contact_no(self):
        return self.__contact_no

    @staticmethod
    def total_contacts():
        if not os.path.exists(Contact.file_path):
            return 0

        with open(Contact.file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            count = sum(1 for row in csvreader)
        return count - 1

    @staticmethod
    def is_exist(name):
        if not os.path.exists(Contact.file_path):
            return False

        with open(Contact.file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if row[1] == name:
                    return True
        return False

    @staticmethod
    def read_contacts():
        if not os.path.exists(Contact.file_path):
            print("No contacts found.")
            return

        with open(Contact.file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            print("ID | Name | Contact No.")
            for row in csvreader:
                print(f"{row[0]} | {row[1]} | {row[2]}")

    @staticmethod
    def is_valid_contact_no(contact_no):
        return len(contact_no) == 10 and is_integer(contact_no)

    @staticmethod
    def remove(name):
        if not Contact.is_exist(name):
            print(f"No contact found with name: {name}")
            return

        contacts = []
        with open(Contact.file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if row[1] != name:
                    contacts.append(row)

        with open(Contact.file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(contacts)

        print(f"Contact {name} removed successfully.")

    def save(self):
        if not os.path.exists(Contact.file_path):
            with open(Contact.file_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(["ID", "Name", "Contact No"])

        with open(Contact.file_path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([Contact.total_contacts() + 1, self.get_name(), self.get_contact_no()])

        print(f"{self.get_name()} saved to contact list!")

if __name__ == "__main__":
    while True:
        print("""
1. Add a new contact
2. Remove a contact
3. Show all contacts
4. Exit
        """)
        operation = input("Enter number: ")

        if operation == "1":
            name = input("Enter name: ")
            contact_no = input("Enter contact number: ")
            if Contact.is_valid_contact_no(contact_no):
                contact = Contact(name=name, contact_no=contact_no)
        elif operation == "2":
            name = input("Enter the name of the contact to remove: ")
            Contact.remove(name)
        elif operation == "3":
            Contact.read_contacts()
        elif operation == "4":
            break
        else:
            print("Invalid option, please try again.")
