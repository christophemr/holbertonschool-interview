#!/usr/bin/python3
""" defines method to solve lockboxes problem """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened_boxes = set()
    keys_to_check = [0]

    while keys_to_check:
        current_key = keys_to_check.pop(0)

        if current_key < 0 or current_key >= n or current_key in opened_boxes:
            continue

        opened_boxes.add(current_key)

        for new_key in boxes[current_key]:
            if new_key not in opened_boxes and new_key not in keys_to_check:
                keys_to_check.append(new_key)

    return len(opened_boxes) == n
