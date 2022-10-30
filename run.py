from email.headerregistry import HeaderRegistry
from random import gammavariate
from sqlite3 import ProgrammingError
import sys
from tabulate import tabulate
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

# All the worksheets and their variables to call them

nata = SHEET.worksheet('nata')
paradis = SHEET.worksheet('paradis')
frikkos = SHEET.worksheet('frikkos')
babylon = SHEET.worksheet('babylon')
yazhou = SHEET.worksheet('yazhou')
mommes = SHEET.worksheet('mommes')
libanesiska = SHEET.worksheet('libanesiska')
inputValues = SHEET.worksheet('inputValues')
mcdonalds = SHEET.worksheet('mcdonalds')
maxham = SHEET.worksheet('maxham')
chicago = SHEET.worksheet('chicago')
yallayalla = SHEET.worksheet('yallayalla')
bagdadkebab = SHEET.worksheet('bagdadkebab')
etage = SHEET.worksheet('etage')

nata_score = nata.get_all_values()
paradis_score = paradis.get_all_values()
frikkos_score = frikkos.get_all_values()
babylon_score = babylon.get_all_values()
yazhou_score = yazhou.get_all_values()
mommes_score = mommes.get_all_values()
libanesiska_score = libanesiska.get_all_values()
mcdonalds_score = mcdonalds.get_all_values()
maxham_score = maxham.get_all_values()
chicago_score = chicago.get_all_values()
yallayalla_score = yallayalla.get_all_values()
bagdadkebab_score = bagdadkebab.get_all_values()
etage_score = etage.get_all_values()


print("\n")
print("Are you hungry? Let us help you with that.\n")


def get_name():
    """Gets the name from the user
    and adds the input to google sheet to see
    who used the program"""
    print("\n")
    name_str = input("Enter your name:\n\n")
    print("\n")
    email_str = input("And your e-mail please:\n\n")
    while True:
        if name_str.isalpha() == True:
            email_str.isalpha() == True
            print("\n")
            print(f"Okay then, {name_str}! Let's get started.\n\n")
            inputValues.append_row([name_str])
            inputValues.append_row([email_str])
            break
        else:
            print("\n")
        print("I don't have all day...\n")
        print("\n")
        input("Name please:\n\n")
        while True:
            if name_str.isalpha():
                print(f"Okay then, {name_str}! Let's get started.\n")
                inputValues.append_row([name_str])
                break
            else:
                try:
                    sys.exit()
                except SystemExit:
                    print('\n')
                    print("In that case ...\n")
                    break
                finally:
                    print("No Soup For You!\n")
                    sys.exit()


def print_restaurant_report(restaurant_averages):
    """calculates the average of column
    in each (non-placeholder) restaurant and 
    then sums all the values for a total average score"""
    restaurant_average_list = []
    index = 0
    for restaurant_average in restaurant_averages:
        if index > 0:
            restaurant_average_list.append(list(map(int, restaurant_average)))
        index = index + 1
    list_sum = []
    for data_list in restaurant_average_list:
        element_sum = sum(data_list)
        list_sum.append(element_sum)
    index_y = 0
    total_elements = len(restaurant_average_list)
    while index_y < total_elements:
        data_row = " "
        index_x = 0
        while index_x < total_elements:
            data_row += str(restaurant_average_list[index_x][index_y]) + ""
            index_x = index_x + 1
        index_y = index_y + 1
    data_row = "A: "
    data_average = []
    for data_sum in list_sum:
        data_row += str(data_sum/total_elements) + "       "
        data_average.append(data_sum/total_elements)
    print(data_row)
    total_average = sum(data_average)/len(data_average)
    print("--------------------------------------------------")
    print(f"                Total Average: {round(total_average,1)}")
    print("--------------------------------------------------")
    return


def get_city():
    """Gets the city from the user
    and then displays the restaurants in that city
    will touch on the city_str variable in README"""
    print("\n")
    city_str = input(
        "Select City, Enter a number:\n\n1. Helsingborg\n2. Göteborg\n3. Malmö\n\n")
    while True:
        if city_str == "1":
            print("\n")
            print("You have chosen Helsingborg.\n")
            print("Restaurants in Helsingborg:\n")
            break
        elif city_str == "2":
            while True:
                if city_str == "2":
                    print("\n")
                    print("You have chosen Göteborg.\n")
                    print("\n\n")
                    city_str = input(
                        "Restaurants in Göteborg:\n 1. McDonalds\n 2. Maxham\n\n")
                    break
        elif city_str == "3":
            while True:
                if city_str == "3":
                    print("\n")
                    print("You have chosen Malmö.\n")
                    print("\n\n")
                    city_str = input(
                        "Restaurants in Malmö:\n 1. Chicago\n 2. Yalla Yalla\n 3. Bagdad Kebab\n 4. Etage\n\n")
                    break
        else:
            print("\n")
            print("Try again, please select a number between 1-3\n")
            city_str = input(
                "City?\n 1. Helsingborg\n 2. Göteborg\n 3. Malmö\n ")
            continue
    return city_str


def get_restaurant(city_str):
    """Has an input for the user to select a restaurant
    and then prints a message confirming the selection"""
    restaurant_str = input(
        "Select a restaurant to see score!\n\n1. Nata\n2. Paradis\n3. Frikkos\n4. Babylon\n5. Yazhou\n6. Mommes\n7. Libanesiska\n\n")

    while True:
        if city_str == "1" and restaurant_str == "1":
            print("\n")
            print("You have chosen Nata.\n")
            break
        elif city_str == "1" and restaurant_str == "2":
            print("\n")
            print("You have chosen Paradis.\n")
            break
        elif city_str == "1" and restaurant_str == "3":
            print("\n")
            print("You have chosen Frikkos.\n")
            break
        elif city_str == "1" and restaurant_str == "4":
            print("\n")
            print("You have chosen Babylon.\n")
            break
        elif city_str == "1" and restaurant_str == "5":
            print("\n")
            print("You have chosen Yazhou.\n")
            break
        elif city_str == "1" and restaurant_str == "6":
            print("\n")
            print("You have chosen Mommes.\n")
            break
        elif city_str == "1" and restaurant_str == "7":
            print("\n")
            print("You have chosen Libanesiska.\n\n")
            break
        elif city_str == "2" and restaurant_str == "1":
            print("\n")
            print("You have chosen McDonalds.\n")
            break
        elif city_str == "2" and restaurant_str == "2":
            print("\n")
            print("You have chosen Maxham.\n")
            break
        elif city_str == "3" and restaurant_str == "1":
            print("\n")
            print("You have chosen Chicago.\n")
            break
        elif city_str == "3" and restaurant_str == "2":
            print("\n")
            print("You have chosen Yalla Yalla.\n")
            break
        elif city_str == "3" and restaurant_str == "3":
            print("\n")
            print("You have chosen Bagdad Kebab.\n")
            break
        elif city_str == "3" and restaurant_str == "4":
            print("\n")
            print("You have chosen Etage.\n")
            break
        else:
            print("\n")
            print("Try again.\n")
            restaurant_str = input(
                "Which restaurant do you want to see?\n\n1. Nata\n2. Paradis\n3. Frikkos\n4. Babylon\n5. Yazhou\n6. Mommes\n7. Libanesiska\n ")
            continue
    return restaurant_str


def display_scores(city_str, restaurant_str):
    """Displays the inputs from survey for the selected restaurant
    uses the tabulate library to create grid for styling"""
    print("Here are the scores for the selected restaurant:\n")

    while True:
        if city_str == "1" and restaurant_str == "1":
            print(tabulate(nata_score, tablefmt="grid"))
            break
        elif restaurant_str == "2":
            print(tabulate(paradis_score, tablefmt="grid"))
            break
        elif restaurant_str == "3":
            print(tabulate(frikkos_score, tablefmt="grid"))
            break
        elif restaurant_str == "4":
            print(tabulate(babylon_score, tablefmt="grid"))
            break
        elif restaurant_str == "5":
            print(tabulate(yazhou_score, tablefmt="grid"))
            break
        elif restaurant_str == "6":
            print(tabulate(mommes_score, tablefmt="grid"))
            break
        elif restaurant_str == "7":
            print(tabulate(libanesiska_score, tablefmt="grid"))
            break
    return


def get_restaurant_average_values(city_str, restaurant_str):
    """Returns the average values for the selected restaurant"""

    while True:
        if city_str == "1" and restaurant_str == "1":
            return nata_score
        elif restaurant_str == "2":
            return paradis_score
        elif restaurant_str == "3":
            return frikkos_score
        elif restaurant_str == "4":
            return babylon_score
        elif restaurant_str == "5":
            return yazhou_score
        elif restaurant_str == "6":
            return mommes_score
        elif restaurant_str == "7":
            return libanesiska_score
        break


def start_over():
    """Restarts the program and makes the program loop
    until the user chooses to quit"""
    play_again_str = input(
        "Would you like to view more restaurants?\n\n 1. Yes\n 2. No\n\n")
    while True:
        if play_again_str == "1":
            print("\n")
            print("Moving on...\n")
            city = get_city()
            restaurant = get_restaurant(city)
            display_scores(city, restaurant)
            restaurant_to_print = get_restaurant_average_values(
                city, restaurant)
            print_restaurant_report(restaurant_to_print)
            start_over()
            break
        elif play_again_str == "2":
            print("\n")
            print("Very well then...\n")
            break
        else:
            print("\n")
            print("Try again.\n")
            play_again_str = input("Try again:\n\n 1. Yes\n 2. No\n\n ")
            print(play_again_str)


def main():
    """
    Runs all program functions
    Inside a while loop
    """
    get_name()
    while True:
        quit = input("Enter any key to continue, or 0 to quit:\n\n")
        if quit == "0":
            break
        else:
            city = get_city()
            restaurant = get_restaurant(city)
            display_scores(city, restaurant)
            restaurant_to_print = get_restaurant_average_values(
                city, restaurant)
            print_restaurant_report(restaurant_to_print)
            start_over()


main()

# collect email?
# print(tabulate(table, headers=["Taste" "Care" "Clean "Price" Speed"]))
