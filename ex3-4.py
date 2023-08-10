import random
number = random.randint(1, 20)
attempts = 0
game_over = False
print("Welcome to guess the number")
while game_over == False:
    guess = int(input("Enter your guess between 1 and 20: "))
    if guess > number:
        attempts += 1
        print("Too high, guess again")
    elif guess < number:
        attempts += 1
        print("Too low, guess again")
    else:
        if guess == number:
            game_over = True
            print(f"Congratulations! you guessed the right number: {number} in: {attempts} attempts")

            