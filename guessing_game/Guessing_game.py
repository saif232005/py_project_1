import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("Choose a level:")
    print("1. Easy (1 - 10, 3 trials)")
    print("2. Intermediate (1 - 100, 7 trials)")
    print("3. Hard (1 - 1000, 15 trials)")

    # Choose level
    level = input("Enter level (1/2/3): ")

    if level == "1":
        limit_low, limit_high, n_trials = 1, 10, 3
    elif level == "2":
        limit_low, limit_high, n_trials = 1, 100, 7
    elif level == "3":
        limit_low, limit_high, n_trials = 1, 1000, 15
    else:
        print("Invalid choice. Defaulting to Easy level.")
        limit_low, limit_high, n_trials = 1, 10, 3

    # Generate random number
    secret_number = random.randint(limit_low, limit_high)

    print(f"\nI have chosen a number between {limit_low} and {limit_high}.")
    print(f"You have {n_trials} trials to guess it.\n")

    # Game loop
    for attempt in range(1, n_trials + 1):
        try:
            guess = int(input(f"Trial {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempt} trial(s).")
            break
        elif guess < secret_number:
            print("Increase!")
        else:
            print("Decrease!")

        if attempt == n_trials:
            print(f"❌ You Lose! The number was {secret_number}.")

# Run the game
guessing_game()