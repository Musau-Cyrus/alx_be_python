num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Operand prompt
operation = input("Choose the operation (+, -, *, /): ")

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