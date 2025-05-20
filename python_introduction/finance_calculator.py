# Prompting the user for their monthly income and total monthly expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculating monthly savings by subtracting monthly expenses form monthly income
monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings *12 + (monthly_savings * 12 * 0.05)

# Display user's monthly savings and projected annual savings after including interest
print("Your monthly savings are $",monthly_savings, ".")
print("Projected savings after one year, with interest, is:", projected_savings)

