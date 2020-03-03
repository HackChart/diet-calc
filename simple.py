def display_breakdown(daily_values: list, macros: list, meal_count: int, goal: str):
    print(f"""
    Here's your plan for {goal}
    ----------------------------------

    Rest Day:
    Total Calories: {daily_values[0]}
    Calories Per Meal {(daily_values[0] / meal_count)}
    Total Macro Breakdown (P/C/F): {macros[0][0]}/{macros[0][1]}/{macros[0][2]}
    Macro Breakdown Per Meal (P/C/F): {round(macros[0][0] / meal_count)}/{round(macros[0][1] / meal_count)}/{round(macros[0][2] / meal_count)}

    Cardio Only:
    Total Calories: {daily_values[1]}
    Calories Per Meal: {(daily_values[1] / meal_count)}
    Total Macro Breakdown (P/C/F): {macros[1][0]}/{macros[1][1]}/{macros[1][2]}
    Macro Breakdown Per Meal (P/C/F): {round(macros[1][0] / meal_count)}/{round(macros[1][1] / meal_count)}/{round(macros[1][2] / meal_count)}

    Weightlifting Day:
    Total Calories: {daily_values[2]}
    Calories Per Meal: {(daily_values[2] / meal_count)}
    Total Macro Breakdown (P/C/F): {macros[2][0]}/{macros[2][1]}/{macros[2][2]}
    Macro Breakdown Per Meal (P/C/F): {round(macros[2][0] / meal_count)}/{round(macros[2][1] / meal_count)}/{round(macros[2][2] / meal_count)}

    Weightlifting + Another Strenuous Exercise:
    Total Calories: {daily_values[3]}
    Calories Per Meal: {(daily_values[3] / meal_count)}
    Total Macro Breakdown (P/C/F): {macros[3][0]}/{macros[3][1]}/{macros[3][2]}
    Macro Breakdown Per Meal (P/C/F): {round(macros[3][0] / meal_count)}/{round(macros[3][1] / meal_count)}/{round(macros[3][2] / meal_count)}
    """)

def calculate_macros(protein: float, carbs: float, lipids: float) -> list:
    macros = []
    for val in daily_values:
        percent_protein = val * protein
        percent_carbs = val * carbs
        percent_lipid = val * lipids
        protein_grams = round(percent_protein /4)
        carbs_grams = round(percent_carbs / 4)
        lipid_grams = round(percent_lipid / 9)
        day = [protein_grams, carbs_grams, lipid_grams]
        macros.append(day)
    return macros

# Calculates RMR based on user input 
# Resting Metabolic Rate = user weight * 10
rmr = None
while type(rmr) != int:
    try:
        rmr = (int(input("How much do you weigh?\n")) * 10)
    except ValueError:
        print("Sorry, that didn't work. Please enter a numeric value.")

# Calculates daily expenditures based on different activity factors 
daily_values = []
rest_day = rmr * 1.2
daily_values.append(rest_day)
cardio_only = rmr * 1.5
daily_values.append(cardio_only)
lifting_only = rmr * 1.6
daily_values.append(lifting_only)
heavy_active = rmr * 1.9
daily_values.append(heavy_active)

# Determines user goal 
accepted_goals = ["Cut", "Bulk", "Maintain", "C", "B", "M"]
goal = None
while goal not in accepted_goals:
    goal = input(
"""
What is your current goal?
Please select from:
(C)ut
(B)ulk
(M)aintain
""")
    goal = goal.title()

# Augments daily values based on goal
if goal == "Cut" or goal == "C":
    for i in range(len(daily_values)):
        daily_values[i] -= 500
    goal = "Cutting"

    # 40/35/25
    macros = calculate_macros(0.4, 0.35, 0.25)

elif goal == "Bulk" or goal == "B":
    for i in range(len(daily_values)):
        daily_values[i] += 500
    goal = "Bulking"

    # 30/50/20
    macros = calculate_macros(0.3, 0.5, 0.2)

else:
    goal = "Maintaining"

    # 35/45/25
    macros = calculate_macros(0.35, 0.45, 0.25)

# Determines desired daily meal count
meal_count = None
while type(meal_count) != int:
    try:
        meal_count = int(input("How many meals would you like to eat every day?\n")) 
    except ValueError:
        print("Sorry, please enter a numeric value.")


display_breakdown(daily_values, macros, meal_count, goal)

