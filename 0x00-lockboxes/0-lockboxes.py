#!/usr/bin/python3

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
