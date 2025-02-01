def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage that can lead to a ZeroDivisionError
average = calculate_average([])