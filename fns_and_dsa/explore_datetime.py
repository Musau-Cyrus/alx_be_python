import datetime
from datetime import date, timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = date.today()
    future_date = today + timedelta(days = number_of_days)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()