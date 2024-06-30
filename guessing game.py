import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Let's see if you can guess it!")

    secret_number = random.randint(1, 10)

    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Enter your guess (between 1 and 10): "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number within the valid range of 1 to 10.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to guess the number.")
                guessed = True

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number_game()

