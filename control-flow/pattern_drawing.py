#Prompt the user for the input of the length of the pattern
size = int(input("Enter the size of the pattern:"))

# A while loop to draw the pattern
count = 0
while count <= size:
    print("*" * size) 
    count += 1