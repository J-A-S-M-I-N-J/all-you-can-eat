import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_fastfood_survey')

nata = SHEET.worksheet('Nata')
paradis = SHEET.worksheet('Paradis')
frikkos = SHEET.worksheet('Frikkos')
babylon = SHEET.worksheet('Babylon')
yazhou = SHEET.worksheet('Yazhou')
mommes = SHEET.worksheet('Mommes')
libanesiska = SHEET.worksheet('Libanesiska')
inputValues = SHEET.worksheet('inputValues')

nata_score = nata.get_all_values()
paradis_score = paradis.get_all_values()
frikkos_score = frikkos.get_all_values()
babylon_score = babylon.get_all_values()
yazhou_score = yazhou.get_all_values()
mommes_score = mommes.get_all_values()
libanesiska_score = libanesiska.get_all_values()

def get_name():
    while True:
        print("Are you hungry? Let us help you with that.\n")
        name_str = input("But first, enter your name:\n ")
        if  name_str.isalpha():
            inputValues.append_row([name_str])
            print(f"Okay then, {name_str}! Let's get started.\n")
            break

        else:
        
            print("I don't have all day... Name please:\n")

print (get_name())










# Display list of cities and validate their choice

# Present the user with the list of restaurants and ask them to select one, validate their choice

# Collect collumns of data from the chosen restaurant from the spreadsheet and present individual scores 
# and total scores. Validate their choice.

# Ask if they wish to proceed, if yes: remove the restaurants they have already selected from the list
# add another option in the list, view total scores for all restaurants. 
# add another option in the list, that exits the program.
# if no: ask for name and what restaurant they want to eat at.
# add the name and restaurant to a tab in the spreadsheet, validate their answer and exit the program.

# Repeat until user has viewed the scores for all restaurants, 
# or until they decide on the restaurant and exit the program.

# When user has decided on a restaurant, ask them where they will eat and then exit the program.

# Validate their answer, and save restaurant where they will eat in a tab in the spreadsheet.


