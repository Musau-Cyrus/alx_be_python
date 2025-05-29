# Prompt the user for a ingle task
task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = input("Is it time_bound-bound? (yes/no): ").lower()

# A match case to raect differently
match priority:
    case "high": 
        if time_bound == "yes":
            print(f"Reminder:", '{task}', "is a", priority, "priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder:", '{task}', "is a", priority, "priority task that requires immediate attention today!")
        else:
            print("Invalid time_bound priority!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder:", '{task}', "is a", priority, "priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder:", '{task}', "is a", priority, "priority task that requires immediate attention today!")
        else:
            print("Invalid time_bound priority!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder:", '{task}', "is a", priority, "priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder:", '{task}', "is a", priority, "priority task that requires immediate attention today!")
        else:
            print("Invalid time_bound priority!")
    case _:
        print("Priority entered!")