import math

# Function to calculate standard deviation
def calculate_std_dev(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return std_dev

# User input
try:
    num_list = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if len(num_list) == 0:
        print("No numbers provided.")
    else:
        std_deviation = calculate_std_dev(num_list)
        print(f"Standard Deviation: {std_deviation:.4f}")
except ValueError:
    print("Please enter valid numbers.")
