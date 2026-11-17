# Unit 1 - P21
# Number guessing game
# The user keeps guessing until the correct number is found

secret = 47
attempts = 0

print("Guess the number between 1 and 100")

guess = int(input("Enter your guess: "))
attempts = attempts + 1

while guess != secret:
    if guess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

print("Correct! You guessed the number in", attempts, "attempts.")
