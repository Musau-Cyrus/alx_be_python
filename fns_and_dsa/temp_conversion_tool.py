FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature_str = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature_str)
        units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        match units:
            case 'C':
                converted = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted}°F")
            case 'F':
                converted = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted}°C")
            case _:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        
if __name__ == "__main__":
    main()