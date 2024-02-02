import random

#  Welcome messages
print("\nWelcome to the number guessing game!")
print("\nPlease select the range of numbers you would like to guess from.")

#  User enters the range of numbers. Checking for value errors or if the first number is lower than the second one.
while True:

    try:
        num1 = int(input("\nEnter the first (lowest) number: "))
        num2 = int(input("\nEnter the second (highest) number: "))
        if num1 > num2:
            print("\nThe first number can't be higher than the second one! Try again!")
        else:
            break
    except ValueError:
        print("\nThat is not a number! Try again!")
        continue

#  Generating a random number. Declaring variables needed.
random_num = random.randint(num1, num2)  # Generates a random number
counter = 1
current_lowest = 0
current_highest = 0

while True:

    try:
        guess = int(input(f"\nPlease enter your guess (between {num1} and {num2}): "))
        if guess < num1 or guess > num2:
            print("\nYou can't guess outside of the range you chose! Try again!")
            continue
    except ValueError:
        print("\nThat is not a number! Enter your guess again!")
        continue

    if guess == random_num:
        print(f"\nCongratulations, that's the right number! It took you {counter} guesses to guess correctly!")
        break
    elif guess > random_num:
        print("\nLower")
        counter += 1
        num2 = guess
        continue
    else:
        print("\nHigher")
        counter += 1
        num1 = guess
        continue
