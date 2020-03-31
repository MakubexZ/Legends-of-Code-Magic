# -*- coding: utf-8 -*-
import sys
import numpy as np
from collections import Counter

d = open("D:\Python\CCG\GameCoding\Card_items.txt", "r")
line = d.readline()
value_list = {}

# Analyze each line of one item
# Calculate value of each item based on empirical formula
while line:
    item = line.split(";")

    # For Green item calculate strength of basic and special abilities
    if 'Green' in item[2]:
        strength = int(item[4]) + int(item[5])

        if 'B' in item[6]:
            strength += 2
        elif 'C' in item[6]:
            strength += 2.5
        elif 'D' in item[6]:
            strength += 2
        elif 'G' in item[6]:
            strength += 2
        elif 'L' in item[6]:
            strength += 4
        elif 'W' in item[6]:
            strength += 3

        if int(item[7]) != 0:
            strength += int(item[7])*0.5
        if int(item[9]) != 0:
            strength += int(item[9])*2

    # For Red item calculate strength of basic and special abilities
    elif 'Red' in item[2]:
        strength = abs(int(item[4]) + int(item[5]))

        if 'B' in item[6]:
            strength += 2
        elif 'C' in item[6]:
            strength += 2.5
        elif 'D' in item[6]:
            strength += 2
        elif 'G' in item[6]:
            strength += 2
        elif 'L' in item[6]:
            strength += 4
        elif 'W' in item[6]:
            strength += 3

        if int(item[8]) != 0:
            strength -= int(item[8])*1.5
        if int(item[9]) != 0:
            strength += int(item[9])*2

    # For Blue item calculate strength of basic and special abilities
    elif 'Blue' in item[2]:
        strength = abs(int(item[4]) + int(item[5]))

        if int(item[7]) != 0:
            strength += int(item[7])*0.5
        if int(item[8]) != 0:
            strength -= int(item[8])*1.5
        if int(item[9]) != 0:
            strength += int(item[9])*2

    # Calculate value via dividing strength by 2*cost+1
    # 'COST' is the consumption of using this card
    value = strength/(int(item[3])*2 + 1)
    iden = item[0].strip()
    value_list[iden] = value

    line = d.readline()

print(value_list)

d.close()

