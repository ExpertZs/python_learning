secret_number = 6       #Declering a secrate number
guess_count=0
guess_limit = 3         #Liniting the number of time for wrong guess
while guess_count < guess_limit :       #Checking the number of time for wrong guess
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print(f"You won! The secret number is {secret_number}")
        break
else:
    print("Sorry, You failed")

