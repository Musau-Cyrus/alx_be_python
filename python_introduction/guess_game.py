secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
    guess_count +1
    guess = int(input(print("Enter a number: ")))
    
print(f"You guessed in {guess_count} tries!")
