#!/usr/bin/python3

"""
def canUnlockAll(boxes):
    # Box it's a list than tha key it's 0 forever Unlocked 
    listBoxUnlocked = [0]
    
    # 
    for keyUnlocked in listBoxUnlocked:
        for keyBoxes in boxes[keyUnlocked]:
            if keyBoxes not in listBoxUnlocked:
                if keyBoxes < len(boxes):
                    listBoxUnlocked.append(keyBoxes)
    if len(listBoxUnlocked) == len(boxes):
        return True
    return False
""" 

def canUnlockAll(boxes):

    numbers = []
    listunlock = []
    len_boxes = len(boxes)

    for keyboxes in boxes:
        listunlock.append(0)
    listunlock[0] = 1

    for keyUnlocked in boxes[0]:
        numbers.append(keyUnlocked)

    for number in numbers:
        if number < len_boxes and listunlock[number] == 0:
            listunlock[number] = 1

            for keyUnlocked in boxes[number]:
                if keyUnlocked not in numbers:
                    numbers.append(keyUnlocked)

    if 0 in listunlock:
        return False
    else:
        return True
