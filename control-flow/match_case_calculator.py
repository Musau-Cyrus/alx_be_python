#Prompt the user to enter num1 and num2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Operand prompt
operation = input("Choose the operation (+, -, *, /): ")

# A match case control flow that controls the type of input that a user enters
match operation:
    case "+":
        result = num1 + num2
        print("The result is", result)
    case "-":
        result = num1 - num2
        print("The result is", result)
    case "*":
        result = num1 * num2
        print("The result is", result)
    case "/":
        result = num1 / num2 
        print("The result is", result)
    case _:
        print("Invalid input")