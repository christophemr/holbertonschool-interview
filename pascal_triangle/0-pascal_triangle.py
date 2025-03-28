#!/usr/bin/python3
"""
Defines a function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists of int: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each subsequent row
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Calculate the values in the row
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with a 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle
