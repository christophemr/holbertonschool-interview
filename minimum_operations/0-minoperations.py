#!/usr/bin/env python3
"""
method that calculates the fewest number of operations needed
to result in exactly n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible.
    """

    if not isinstance(n, int) or n <= 0:
        return 0
    # Base case: Already have one 'H'
    if n == 1:
        return 0

    operations = 0
    # Start with one 'H'
    pasted_count = 1
    # Initially, we have copied one 'H'
    copied_count = 1

    # If n is divisible by pasted_count, copy all
    while pasted_count < n:
        if n % pasted_count == 0:
            copied_count = pasted_count
            # Copy All operation
            operations += 1
        paste_count_to_add = (
            copied_count if (n - pasted_count) >= copied_count
            else (n - pasted_count))

        pasted_count += paste_count_to_add
        operations += 1

    return operations
