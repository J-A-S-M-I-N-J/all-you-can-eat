from email.headerregistry import HeaderRegistry
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



print("Are you hungry? Let us help you with that.\n")

def get_name():
    """Gets the name from the user
    and adds the input to google sheet"""
    name_str = input("But first, enter your name:\n ")
    while True:
        if  name_str.isalpha() == True:
            print(f"Okay then, {name_str}! Let's get started.\n")
            inputValues.append_row([name_str])
            break
           
        else:
            print("I don't have all day...\n")
            name_str = input("Name please:\n ")

        if  name_str.isalpha():
            print(f"Okay then, {name_str}! Let's get started.\n")
            inputValues.append_row([name_str])
            break
            
        else:
            print("No soup for you!\n")
            break
        
    return name_str

# print(get_name())

def get_city():
    """Gets the city from the user
    and then displays the restaurants in that city"""
    city_str = input("Where are you located? Enter a number:\n 1. Helsingborg\n 2. Placeholder\n 3. Placeholder2\n ")
    while True:
        if city_str == "1":
            print("You have chosen Helsingborg. Here are the restaurants in Helsingborg:\n")
            break
        elif city_str == "2":
            print("You have chosen Göteborg. Here are the restaurants in Placeholder:\n")
            break
        elif city_str == "3":
            print("You have chosen Malmö. Here are the restaurants in Placeholder2:\n")
            break
        else:
            print("Try again, please select a number between 1-3\n")
            city_str = input("City?\n 1. Helsingborg\n 2. Placeholder\n 3. Placeholder2\n ")
            continue
    return city_str

# print(get_city())

def get_restaurant():
    """Gets the restaurant from the user"""
    restaurant_str = input("Select a restaurant from 1-7 to see their score!\n 1. Nata\n 2. Paradis\n 3. Frikkos\n 4. Babylon\n 5. Yazhou\n 6. Mommes\n 7. Libanesiska\n ")
    while True:
        if restaurant_str == "1":
            print("You have chosen Nata.\n")
            break
        elif restaurant_str == "2":
            print("You have chosen Paradis.\n")
            break
        elif restaurant_str == "3":
            print("You have chosen Frikkos.\n")
            break
        elif restaurant_str == "4":
            print("You have chosen Babylon.\n")
            break
        elif restaurant_str == "5":
            print("You have chosen Yazhou.\n")
            break
        elif restaurant_str == "6":
            print("You have chosen Mommes.\n")
            break
        elif restaurant_str == "7":
            print("You have chosen Libanesiska.\n")
            break
        else:
            print("Try again, please select a number between 1-7\n")
            restaurant_str = input("Which restaurant do you want to see?\n 1. Nata\n 2. Paradis\n 3. Frikkos\n 4. Babylon\n 5. Yazhou\n 6. Mommes\n 7. Libanesiska\n ")
            continue
    return restaurant_str

# print (get_restaurant())

def display_scores(city_str, restaurant_str):
    """Displays the scores for the selected restaurant"""
    restaurant_score = (city_str, restaurant_str)
    print(restaurant_score)

    while True:
        if   city_str == "1" and restaurant_str == "1":
             print(nata.get_all_values())
             break
        elif city_str == "1" and restaurant_str == "2":
             print(paradis.get_all_values())
             break
        elif city_str == "1" and restaurant_str == "3":
             print(frikkos.get_all_values())
             break
        elif city_str == "1" and restaurant_str == "4":
             print(babylon.get_all_values())
             break
        elif city_str == "1" and restaurant_str == "5":
             print(yazhou.get_all_values())
             break
        elif city_str == "1" and restaurant_str == "6":
             print(mommes.get_all_values())
             break
        elif city_str == "1" and restaurant_str == "7":
             print(libanesiska.get_all_values())
             break
    return


def main():
    """
    Run all program functions
    """
    get_name()
    city = get_city()
    restaurant = get_restaurant()
    display_scores(city, restaurant)

main()











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


