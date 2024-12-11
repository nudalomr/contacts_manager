# contacts_manager
Contact Management script

This repo contains a script for Scripting Class Mark Nudalo

Description:

My inspiration for this script was my former Manager and his brimming rolodex. As a Store Manager of a retail store, he had way too many people and contact information to save. It has gotten to the point that some contacts are lost or is outdated. I wanted to create a script that can be use by anyone anywhere for solving that unique problem.The main job of this script, contacts_manager, is to help INDIVIDUALS
managed their contacts.

Here are some of the features of this script:

> Give the user the abilityto add, delete or edit contacts by only using unique ID system (1-1000). 
> Give the user the ability to store information in a simple manner and wide compatability by using the CSV format.
> Give the user the ability to transform the CSV format into regular text document for accessibility reasons.

Future work that could be added:

	1. Validate Phone number.
	2. Give the user the ability to transform CSV to PDF format.
	3. Have the script run anywhere in the directory. (See REQUIREMENTS)
	4. Give the ability to use an existing CSV file with a different file name.

REQUIREMENTS:

	1. This script was writtent with Python 3.11.5
	2. This script requires that the csv file must be in the same directory as the script file.
	3. The script CAN create a csv file called "my_contacts.csv" if none exist.

TEST:

	1. Use -a or --add to add contacts
	2. Use -d or --delete to delete contact.
	3. Use -l or --list to list current contacts.
	4. Use -e or --edit to edit a specific contact.
	5. Use -f or --find to find a contact(s) using any keyword.
	6. Use -h or --help to show Man pages.
	7. Verify Email is in correct format or using 'N/A' or 'n/a'.
	8. Edit only specific information without changing the other data.
	9. Check if ID is unique.
	10. Check if human readable error message exist IF using -a, -d, or -e AND the file is open.

NOTE: Before doing any testing, please use the list feature (-l) to save time.

