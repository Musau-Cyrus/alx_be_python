def safe_divide(float(numerator), float(denominator)):
    try:
        quotient = numerator / denominator
        return f"The result of the division is {quotient}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        print("Error: Please enter numeric values only.")