import random

def get_hint(number, guess):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    return "Correct!"

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number. I'll give you hints to help you out.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            hint = get_hint(number, guess)
            print(hint)

            if guess == number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    play_game()
