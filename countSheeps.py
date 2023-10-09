# Count Sheep

# Generate a random number between 1 and 10 to represent the number of sheep needed to fall asleep.
import random

# Random number variable
sheep_to_sleep = random.randint(1, 100)

# Are you still awake
awake = True

# Count sheep until you fall asleep

# Counter variable
sheep = 0

# Count sheep
while awake and sheep < 100:  # Introduce the limit of 20 sheep
    print(f'{sheep + 1} sheep - baa!')

    # Add one sheep to the number
    sheep += 1

    # Check if it's time to fall asleep
    if sheep == sheep_to_sleep:
        awake = False

# Sweet dreams
if not awake:
    print('\n...zZzZzZzZ...')
