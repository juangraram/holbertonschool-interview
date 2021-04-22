#!/usr/bin/python3

def canUnlockAll(boxes):

    listBoxUnlocked = [0]

    for keyUnlocked in listBoxUnlocked:
        for keyBoxes in boxes[keyUnlocked]:
            if keyBoxes not in boxes[keyBoxes]:
                if keyBoxes < len(boxes):
                    listBoxUnlocked.append(keyBoxes)
    if len(listBoxUnlocked) == len(boxes):
        return True
    return False
