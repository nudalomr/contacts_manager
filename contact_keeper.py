import os
import csv
import argparse
import random #used to generate ID randomly
import re

from datetime import datetime


contact_file = "my_contacts.csv"

if not os.path.exists(contact_file):
    with open(contact_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Phone", "Email", "Note"])


def generate_id(): #give each new user a unique ID
    ids = set()
    with open(contact_file, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            ids.add(int(row[0]))

    while True:
        new_id = random.randint(1, 1000)
        if new_id not in ids:
            return new_id

def is_valid_email(email): #email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" or "N/A"
    return re.match(email_pattern, email) is not None

def add_contact():
    print("")
    print("Please fill in all the information...")
    print("")
    print("Use N/A if data is not available.")
    print("")

    name = input("Enter Full Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    note = input("Enter Note: ")
    print("")

    unique_id = generate_id()

    if email.lower() == "n/a" or is_valid_email(email):
        try:
            with open(contact_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([unique_id, name, phone, email, note])
            print(f"Contact added: ID-{unique_id} | {name} | {phone} | {email} | {note}")
        except PermissionError:
            print("Error: The file 'my_contacts.csv' is open. Close it and try again.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
    else:
        print("")
        print("Please use valid email format or 'N/A' or 'n/a'. Please try again.")
        print("")


def delete_contact():
    delete_id = input("Please Enter the ID of the contact to delete: ")
    try:
        with open(contact_file, "r", newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    
        deleted_contact = None
        updated_contacts = []
        for contact in contacts:
            if contact[0] == delete_id:
                deleted_contact = contact
            else:
                updated_contacts.append(contact)

        if deleted_contact:
            with open(contact_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_contacts)
            print("")
            print(f"Contact with ID {delete_id} deleted.")
            print(f"Details: {', '.join(deleted_contact)}")
        else:
            print(f"Contact with ID {delete_id} not found.")
            print("")

    except PermissionError:
            print("Error: The file 'my_contacts.csv' is open. Close it and try again.")
    except Exception as e:
            print(f"An unexpected error occured: {e}")        
    

def list_contacts():
    with open(contact_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def find_contact():

    #find contact using any keyword
    keyword = input("Enter Keyword to search: ").strip().lower()

    matches = []
    
    with open(contact_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if any(keyword in field.lower() for field in row):
                matches.append(row)

    if matches:
        print("\nMatching contacts:")
        for match in matches:
            print(f"ID: {match[0]} | Name: {match[1]} | Phone: {match[2]} | Email: {match[3]} | Note: {match[4]}")
    else:
        print("No match found.")



def edit_contact(): #using an ID number; edit name, email, Phone, note
    target_id= input("Please enter the ID of the contact to edit: ")
    try:
        with open(contact_file, "r", newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        for i, contact in enumerate(contacts):
            if contact[0] == target_id:
                print(f"found contact: {contact}")
                print("")
                print("Put nothing or Press Enter if data doesnt change.")
                print("")

                name = input(f"Enter new name (current: {contact[1]}): ") or contact[1]
                phone = input(f"Enter new phone (current: {contact[2]}): ") or contact[2]
                email = input(f"Enter new email (current: {contact[3]}): ") or contact[3]
                note = input(f"Enter new note (current: {contact[4]}): ") or contact[4]

                contacts[i] = [target_id, name, phone, email, note]

                with open(contact_file, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(contacts)

                print(f"Contact with ID {target_id} updated: {contacts[i]}")
                return
            
        print(f"No contact found with ID {target_id}.")
        
    except PermissionError:
            print("Error: The file 'my_contacts.csv' is open. Close it and try again.")
    except Exception as e:
            print(f"An unexpected error occured: {e}")    



def csv_to_text(contact_file, output_text_file):
    
    with open (contact_file, 'r') as csvfile, open(output_text_file, 'w') as textfile:
        for line in csvfile:
            textfile.write(line)
    print(f"Contacts saved as a plain text file: {output_text_file}")




# Arguments

parser = argparse.ArgumentParser(
    description=(
        "This is a Python script that can help you manage your contacts (like the old Rolodex).\n"
        "You can use this script to manipulate a CSV file full of contacts.\n"
        "This script is for personal use only. Be careful not to delete important data.\n\n"
        "NOTE: THIS SCRIPT ONLY WORKS IF THE FILE IS NOT OPEN."
    ),
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument("-a", "--add", action="store_true", help="Prompt to add a new contact.")
parser.add_argument("-d", "--delete", action="store_true", help="Delete a contact. Use -l to know the unique ID.")
parser.add_argument("-t", "--text", action="store_true", help ="Turns CSV file into a Text file." )
parser.add_argument("-l", "--list", action="store_true", help ="List the Contents of the CSV file." )
parser.add_argument("-f", "--find", action="store_true", help ="Find contacts using keywords." )
parser.add_argument("-e", "--edit", action="store_true", help ="Edit contacts using ID." )

args = parser.parse_args()


if args.add:
    add_contact()
    print("")
elif args.delete:
    delete_contact()
    print("")
elif args.list:
    list_contacts()
elif args.find:
    find_contact()
elif args.edit:
    edit_contact()
elif args.text:
    current_date = datetime.now().strftime("%m-%d-%Y")
    output_text_file = f"contacts_{current_date}.txt"
    csv_to_text(contact_file, output_text_file)
else:
     parser.print_help()


