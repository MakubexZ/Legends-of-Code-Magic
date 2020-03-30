# -*- coding: utf-8 -*-
import sys
import numpy as np
from collections import Counter

d = open("D:\Python\CCG\GameCoding\Card_creatures.txt", "r")
line = d.readline()
value_list = {}
cost = []
value_cost = np.zeros(13)
while line:
    creature = line.split(";")
    strength = int(creature[4]) + int(creature[5])
    
    if 'B' in creature[6]:
        strength += int(creature[4])
    elif 'C' in creature[6]:
        strength += int(creature[4])*1.2
    elif 'D' in creature[6]:
        strength += int(creature[4])*0.8
    elif 'G' in creature[6]:
        strength += int(creature[5])
    elif 'L' in creature[6]:
        strength += 4
    elif 'W' in creature[6]:
        strength += 5

    if int(creature[7]) != 0:
        strength += int(creature[7])*0.5
    if int(creature[8]) != 0:
        strength -= int(creature[8])*1.5
    if int(creature[9]) != 0:
        strength += int(creature[9])*2

    if int(creature[5]) - int(creature[4]) > 2:
        strength -= 3
    if int(creature[4]) - int(creature[3]) > 2:
        strength += 4

    if int(creature[3]) != 0:
        value = strength/(int(creature[3])*2 + 1)
    else:
        value = strength/2
    iden = creature[0].strip()
    value_list[iden] = value
    cost.append(int(creature[3]))
    

    if int(creature[3]) == 0:
        value_cost[0] += value
    elif int(creature[3]) == 1:
        value_cost[1] += value
    elif int(creature[3]) == 2:
        value_cost[2] += value
    elif int(creature[3]) == 3:
        value_cost[3] += value
    elif int(creature[3]) == 4:
        value_cost[4] += value
    elif int(creature[3]) == 5:
        value_cost[5] += value
    elif int(creature[3]) == 6:
        value_cost[6] += value
    elif int(creature[3]) == 7:
        value_cost[7] += value
    elif int(creature[3]) == 8:
        value_cost[8] += value
    elif int(creature[3]) == 9:
        value_cost[9] += value
    elif int(creature[3]) == 12:
        value_cost[12] += value
    # print(value_list)
    # break
    line = d.readline()

# cost.sort()
# print(cost)
# print(Counter(cost))
cards_num = dict(Counter(cost))
for key, value in cards_num.items():
    value_cost[key] /= value
print(value_cost)
print(value_list)


d.close()
