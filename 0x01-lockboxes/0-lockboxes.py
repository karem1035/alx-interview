#!/usr/bin/python3
def canUnlockAll(boxes):
    l = len(boxes)
    opened = [False] * l

    def boxCheck(box):
        opened[box] = True
        for key in boxes[box]:
            if not opened[key]:
                boxCheck(key)
    boxCheck(0)
    return (all(opened))
