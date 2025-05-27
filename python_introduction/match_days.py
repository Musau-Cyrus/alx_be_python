days =input(print("Enter a day")).lower()

match days:
    case "monday":
        print("Ugh its monday again.")
    case "tuesday":
        print("Another working day")
    case "wednesday":
        print("Hump_Day")
    case "thursday":
        print("Almost there")
    case "friday":
        print("It's here")
    case "saturday":
        print("It's weekend")
    case _:
        print("Invalid input")