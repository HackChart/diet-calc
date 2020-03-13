import math
from datetime import datetime

# TODO: Add error handling? 
def calculate_rmr(weight):
    return weight * 10

# Calculates Total Energy Expenditure based on Resting Metabolic
# Rate and Activity Level ( TEE =  RMR * af )
def calculate_daily_expenditure(rmr, activity_level):
    if activity_level == "Very Light":
        return int(rmr * 1.3)
    elif activity_level == "Low Active":
        return int(rmr * 1.6)
    elif activity_level == "Active":
        return int(rmr * 1.7)
    elif activity_level == "Heavily Active":
        return int(rmr * 2.1)
    else:
        # TODO: Update to record error in error log
        print("Unrecognized activity level, defaulting to Very Light")
        return int(rmr * 1.3)

# Calculates total daily caloric goal based on a healthy gain/loss
# rate of 1 lb per week. ( 500 cals/day = 3500 cals/week )
# ( 3500 cals = 1 lb) 
def calculate_caloric_goal(daily_expenditure, is_bulking= False, is_cutting= False):
    if is_bulking:
        return int(daily_expenditure + 500)
    elif is_cutting:
        return int(daily_expenditure - 500)
    else:
        return int(daily_expenditure) # Implemented to account for users that just want to maintain current weight

# Returns number of calories that should be eaten at each meal
def calculate_cals_per_meal(daily_intake, number_of_meals):
    return int(daily_intake * number_of_meals)

# TODO: Implement meal timing recommendations based on number of meals
# to be eaten per day
def calculate_time_between_meals(number_of_meals):
    pass



# UNDER CONSTRUCTION
# -----------------------------------------------------------------
accepted_answers = ["Y", "y", 
"Yes", "yes", 
"Yeah", "yeah", ]

has_account = input("Do you already have an account?\n(Y/N): ")
if has_account in accepted_answers:
    has_account = True
    username = input("Username: ")
    password = input("Password: ")
    # TODO: Validate user credentials using SQL 
    # TODO: Read previous data from save file 
else:
    will_create_account = input("Would you like to create an account?\nCreating an account allows you to save your diet plan and view\nyour progress over time\n(Y/N): ")
    if will_create_account in accepted_answers:
        # Creates a username 
        username = input("Please enter your desired username: ")
        username_is_unverified = True

        while username_is_unverified:
            is_correct = input(f"Is this correct? Username: {username}")
            if is_correct in accepted_answers:
                username_is_unverified = False
            else:
                username = input("Please enter your desired username: ")
        # TODO: Write decided username to save file/sql database for future use

        # Creates a password for the user
        password = ""
        password_verification = None

        while password != password_verification:
            password = input("Plase enter your desired password: ")
            password_verification = input("Please confirm your password: ")
            if password != password_verification:
                print("Sorry, those don't match.")
        # TODO: Writed decided password to save file/sql database for future use

        # TODO: Welcome user/prompt for information

    else:
        print("You won't be able to save any of your data this way")