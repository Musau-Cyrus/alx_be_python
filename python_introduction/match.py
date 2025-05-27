age = input(print("Enter age"))

match age:
    case 18 | 19:
        if age > 18:
            print("You are eligible for voting")
        else:
            print("You are not eligible to vote")
    case _:
        print("Inavlid input")
