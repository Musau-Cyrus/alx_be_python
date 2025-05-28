num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Operand prompt
operand = input(print("Choose the operation (+, -, *, /): "))

match operand:
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