import argparse
import sys
import os
import json

CONTACTS_FILE = "contacts.json"

def load_contacts ():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contacts (contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, nargs="?", help="Name of the contact")
parser.add_argument("email", type=str, nargs="?", help="Email of the contact")
parser.add_argument("-l", "--list", action="store_true", help="List all contacts")
parser.add_argument("-r", "--remove", type=str, help="Remove a contact by their name")
args= parser.parse_args()

if len(sys.argv) ==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.list:
    contacts = load_contacts()
    for contact in contacts:
        print(f"{contact['name']}: {contact['email']}")

elif args.remove:
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"] != args.remove]
    save_contacts(new_contacts)
    print(f"Removed {args.remove}")

elif args.name and args.email