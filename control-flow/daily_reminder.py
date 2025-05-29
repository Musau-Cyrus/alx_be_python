# Prompt the user for a ingle task
task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time = input("Is it time bound? ").lower()

# A match case to raect differently
match priority:
    case "high": 
        if time == "yes":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate attention today!")
        elif time == "no":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate attention today!")
        else:
            print("Invalid time priority!")
    case "medium":
        if time == "yes":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate attention today!")
        elif time == "no":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate attention today!")
        else:
            print("Invalid time priority!")
    case "low":
        if time == "yes":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate attention today!")
        elif time == "no":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate attention today!")
        else:
            print("Invalid time priority!")
    case _:
        print("Priority entered!")