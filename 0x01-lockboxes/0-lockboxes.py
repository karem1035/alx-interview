#!/usr/bin/python3
def canUnlockAll(boxes):
    l = len(boxes)
    oppened = [False] * l

    def boxCheck(box):
        oppened[box] = True
        for box in boxes[box]:
            if not oppened[box]:
                boxCheck(box)

    boxCheck(0)
    return (all(oppened))
