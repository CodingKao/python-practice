# Calculate average score and compared to your score

def better_than_average(class_points, your_points):
    # Calculate the average of class points including your points
    total_points = sum(class_points) + your_points
    average = total_points / (len(class_points) + 1)  # Adding 1 for your point
    
    # Compare your points to the average and return True if better, else False
    return your_points > average

# Class scores
class_points = [80, 85, 90, 75, 70, 80, 75, 76, 98, 95, 94, 90, 87, 85, 88, 82, 78]

# Your scor
your_points = int(input("Enter your score: "))
result = better_than_average(class_points, your_points)


# Print the appropriate message based on the result
if result:
    print("You scored higher than average")
else:
    print("You scored lower than average")
