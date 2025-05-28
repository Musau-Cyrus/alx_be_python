#Prompt the user to enter the number for which they want to see the multiplication table
number = int(input("Enter a number to see its multiplication table:"))

#Generate the multiplication table using a for loop
for count in range(1, 11):
    print(f"{number} * {count} = {number * count}")
