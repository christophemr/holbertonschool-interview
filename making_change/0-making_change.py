#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: The fewest number of coins needed to meet the total,
        or -1 if not possible.
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for
    # each amount from 0 to total
    min_coins = [float('inf')] * (total + 1)
    # Base case: 0 coins needed to make amount 0
    min_coins[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update the min_coins list for all amounts from the
        # coin value to the total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If the total amount cannot be met, return -1
    return min_coins[total] if min_coins[total] != float('inf') else -1
