import random
from datetime import datetime

# Generate and print a random set of numbers
print("Random set of numbers:")
for _ in range(5):  # Print 5 random numbers as an example
    print(random.randint(1, 100))  # Generates a random number between 1 and 100

# Print the current date
current_date = datetime.now().date()
print("\nCurrent Date:", current_date)

# Generate a random float, round it, and print the result
random_float = random.uniform(1, 100)  # Generates a random float between 1 and 100
rounded_number = round(random_float, 2)  # Round to 2 decimal places
print("\nRounded Random Number:", rounded_number)