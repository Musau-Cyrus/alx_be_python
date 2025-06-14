def safe_divide(numerator, denominator):
    try:
        quotient = numerator / denominator
        return f"The result of the division is {quotient}"
    except ZeroDivisionError:
        return "Error! Division by zero."
    except ValueError:
        return "You entered an invalid input"