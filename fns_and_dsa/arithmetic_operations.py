def perform_operation(num1:float, num2:int, operation:str):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0 or num1 == 0:
                return "Error: Division by zero!"
            elif num2 != 0 and num1 != 0:
                return num1 / num2
            else:
                return "Invalid input!"
        case _:
            return "Error: Invalid operation chosen!"
                