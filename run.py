from email.headerregistry import HeaderRegistry
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

nata = SHEET.worksheet('nata')
paradis = SHEET.worksheet('paradis')
frikkos = SHEET.worksheet('frikkos')
babylon = SHEET.worksheet('babylon')
yazhou = SHEET.worksheet('yazhou')
mommes = SHEET.worksheet('mommes')
libanesiska = SHEET.worksheet('libanesiska')
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
    """Displays the scores for the selected restaurant
    also has the tabulate library applied to make it look nice""" # replicate data 
    print("Here are the scores for the selected restaurant:\n")

    while True:
        if   city_str == "1" and restaurant_str == "1":
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


################################

#def update_restaurant_data(nata, paradis, frikkos, babylon, yazhou, mommes, libanesiska):
   # """Updates the restaurant data in google sheet"""
   # print("Updating restaurant data...\n")
   # nata.append_row(av_score)
   # paradis.append_row(av_score)
   # frikkos.append_row(av_score)
   # babylon.append_row(av_score)
   # yazhou.append_row(av_score)
   # mommes.append_row(av_score)
   # libanesiska.append_row(av_score)

  #  print("Restaurant data updated successfully.\n")

################################

 #def get_list():
   # """
   # Takes the data values from restaurant_score and lists them
   # Will be used to calculate the average score
   # And make the data more readable for the user"""
    # score_list = (nata_score, paradis_score, frikkos_score, babylon_score,\
        # yazhou_score, mommes_score, libanesiska_score)
    # for k, v in list(score_list)():
    #    print(k, v)
################################

def average_score(nata_averages):
    """Calculates the average score for the selected restaurant"""
    nata_averages = nata
    nata_averages = [[3,5,3,4,5], [4,5,4,5,5], [4,4,2,5,5], [4,5,5,4,4], [4,4,3,4,5]]
    zipped = zip(*nata_averages)
    zipped_list = list(zipped)
    print(zipped_list)
    list_sums = nata_averages
    list_sums = 0
    for i in range(len(nata_averages)):
        list_sums += nata_averages[i]
      #  average = sum_of_list / len(nata_averages)
        column_average = [ list_sums / len(nata_averages) for list_sums  in zip(*nata_averages)]
    column_average = average_score(nata)
    print(column_average)
    return column_average

# def Average(lst):
#     sum_of_list = 0
#     for i in range(len(lst)):
#         sum_of_list += lst[i]
#     average = sum_of_list / len(lst)
#     return average

# lst=[1,2,3,4,5]
# average = Average(lst)
# print(average)

## why does the += work here but not above? 

def get_total_score():
    """Displays the average score for the selected restaurant"""
    print("Would you like to see the total score?\n")
    total_score = input("Enter Y or N\n")
    while True:
        if total_score == "Y":
            print("The total score for the selected restaurant is:\n")
        #print(function)
            break
        elif total_score == "N":
            print("Thank you for using the program!\n")
            break
        else:
            print("Try again, please enter Y or N\n")
            total_score = input("Enter Y or N\n")
            continue
    return

def play_again():
    print("Would you like to see the scores for another restaurant?\n")
    repeat_game = input("Enter Y or N\n")
    while True:
        if repeat_game == "Y":
            get_city()
            continue
        elif repeat_game == "N":
            print("Thank you for using the program!\n")



################################

#def get_average():
   # """ gets avg score """
    #total_score = 0
    #for i in range(len((nata_score))):
       # total_score += i
       # avg_score = total_score / len(nata_score)
      #  nata.append_row([avg_score])
   # return avg_score
    
    
#print(get_average)

################################

#def get_average():
    # """ gets avg score """
  #  list_of_lists = [[nata_score], [paradis_score], [frikkos_score], [babylon_score], [yazhou_score], [mommes_score], [libanesiska_score]]
 #   for i in list_of_lists:
   #     for j in i:
     #       for k in j:
       #         print(k)
        #        print(sum(k)/len(k))
         #       append_row([sum(k)/len(k)])
   # return

################################

#def get_average():
   # """Average score of lists"""
  #  calc_avg = [xxx]
    #print(range(len((nata_score))))
    #for xxx in range(len((nata_score))):
      #  xxx = [int() for num in nata_score]
      #  average = sum()/len(nata_score)
       # calc_avg = average
      #  calc_avg.append.nata(calc_avg)
       # return(calc_avg)
  #  print("hope this  working")

################################

#def get_average():
   # """Gets the average score for the selected restaurant"""
  #  lst = []
   # for ind in range(len(nata_score)):
     #   num = ???
     #   average = sum(num)/len(nata_score)
     #   lst.append(average)
     #   return(lst)
  #  print(get_average())

################################

    #for n in (range(len((nata_score)))):
    #numbers = int(input('Enter number '))
    #lst.append(numbers)
#print("Sum of elements in given list is :", sum(lst))

################################

#def get_average():
 #   """Calculates the average score for the selected restaurant"""
   # print("calc avg wait")
   # new_score = nata_score
   # new_score = int(new_score)
   # print(new_score)
   # for i in [nata_score]:
       # new_score += int(i)     
        #average_score = new_score / len(new_score)
        #print(average_score)
       # return(average_score)
################################

#def get_average():
#   """Gets the average score for the selected restaurant"""
#  new_restaurant_score = []
    #   for new_score in nata_score:
    #      new_score = [int(num)for num in (nata_score)]
    #      average = sum(new_score) / len(nata_score)
    #      new_restaurant_score = average
    #      return(new_restaurant_score)

    #  new_restaurant_score.append(display_scores)
    # print(new_restaurant_score) 
################################

def main():
    """
    Run all program functions
    """
    get_name()
    city = get_city()
    restaurant = get_restaurant()
    display_scores(city, restaurant)
    nata_averages = nata
    average_score(nata_averages)

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
