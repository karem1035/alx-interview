#!/usr/bin/python3
"""
Lockbox solution
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): List where each element is a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    unlocked = [0]  # Keep track of unlocked boxes (initially box 0)
    for box_id, box in enumerate(boxes):
        if not box:  # Skip empty boxes (no keys)
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    return len(unlocked) == len(boxes)  # Check if all boxes are unlocked
