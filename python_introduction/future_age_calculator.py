#Prompt user to input their age
age = int(input("How old are you? "))

# Calculate age that user wil bein future
current_year = 2023
future_year = 2050
age_increment = future_year - current_year

final_age = age + age_increment

print("In", future_year, ",you will be", final_age, "yaers old.")