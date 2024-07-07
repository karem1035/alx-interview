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

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    boxes_length = len(boxes)
    opened = [False] * boxes_length

    def boxCheck(box):
        opened[box] = True
        for key in boxes[box]:
            if key < boxes_length and not opened[key]:
                boxCheck(key)

    boxCheck(0)
    return all(opened)
