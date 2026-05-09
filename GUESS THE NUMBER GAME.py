# GUESS THE NUMBER
import random
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)  # For color reset after each line

def print_boxed_grid(guesses, correct_number):
    print("\n" + "-"*70)
    for i in range(1, 101):
        box = f"{i:3}"
        color = Back.RESET

        if i in guesses:
            if i == correct_number:
                color = Back.GREEN + Fore.BLACK  # Correct
            elif i < correct_number:
                color = Back.CYAN + Fore.BLACK  # Too low
            else:
                color = Back.RED + Fore.WHITE   # Too high
        else:
            color = Back.WHITE + Fore.BLACK

        print(color + f"[{box}]", end=" ")

        if i % 10 == 0:
            print(Style.RESET_ALL)  # New line after 10 numbers
    print("-"*70 + "\n")

def guess_the_number():
    correct_number = random.randint(1, 100)
    guesses = []
    max_attempts = 10

    print(Fore.YELLOW + "\n🎯 Welcome to 'Guess the Number' (Visual Edition)!\n")
    print("You have", max_attempts, "attempts to guess a number between 1 and 100.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"\n🔢 Attempt {attempt}: Your guess? "))
            if guess < 1 or guess > 100:
                print(Fore.RED + "❌ Please guess a number between 1 and 100.")
                continue

            guesses.append(guess)
            print_boxed_grid(guesses, correct_number)
            time.sleep(0.5)

            if guess == correct_number:
                print(Fore.GREEN + "🎉 You guessed it right! You win!")
                break
            elif guess < correct_number:
                print(Fore.CYAN + "🔼 Too low! Try again.")
            else:
                print(Fore.RED + "🔽 Too high! Try again.")
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number.")
    else:
        print(Fore.MAGENTA + f"\n❌ Game Over! The number was {correct_number}.")

if __name__ == "__main__":
    guess_the_number()
# DUA NAJAM