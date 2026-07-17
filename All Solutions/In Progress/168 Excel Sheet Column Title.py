import math
columnNumber = 701
letters = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
}

columnTitle = ""
array = []
while columnNumber != 0:
    remainder = columnNumber % 26
    if remainder == 0:
        array.append("Z")
        columnNumber = columnNumber // 26
    else:
        array.append(letters[remainder])
        columnNumber = columnNumber // 26

for i in range(len(array)-1,0,-1):
    columnTitle += array[i]

print(columnTitle)