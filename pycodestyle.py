#!/usr/bin/python3
def calculate_sum(numbers):
    """
    Returns the sum of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        int: Sum of all numbers in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total
