#!/usr/bin/python3
"""
Defines a method that determines if a given data set
represents valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """

    if not isinstance(data, list):
        return False
    # Number of bytes expected for the current character
    remaining_bytes = 0

    for byte in data:
        # Consider only the 8 least significant bits
        # Equivalent to byte % 256
        byte &= 0xFF
        # Start of a new character
        if remaining_bytes == 0:
            # 1-byte character
            if byte >> 7 == 0b0:
                continue
            # 2-byte character
            elif byte >> 5 == 0b110:
                remaining_bytes = 1
            # 3-byte character
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            # 4-byte character
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False
        # Invalid starting byte
        else:  # Continuation byte
            if byte >> 6 != 0b10:
                # Invalid continuation byte
                return False
            remaining_bytes -= 1
    # All characters must be complete
    return remaining_bytes == 0
