weight = input("How much do you weigh?  ")
rmr = weight * 10
accepted_goals = ["Cut", "Bulk", "Maintain"]
goal = None
while goal not in accepted_goals:
    goal = input("What is your current goal?\nPlease select from:\nCut\nBulk\nMaintain")
    goal = goal.title()
if goal == "Cut":
    pass
elif goal == "Bulk":
    pass
else:
    pass