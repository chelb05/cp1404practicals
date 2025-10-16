import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45  # Must be between 1 and 45.
NUMBERS_PER_PICK = 6

number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)  # Generate random integers between 1 and 45.
        if number not in numbers:
            numbers.append(number)  # Use append calling.
    numbers.sort() # Sort from smallest to largest.
    for i, n in enumerate(numbers):
        if i > 0:
            print(" ", end="")
        print(f"{n:2d}", end="") # String format.
    print()