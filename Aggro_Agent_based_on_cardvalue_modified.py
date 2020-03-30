import sys
import math
import bisect
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

card_value_list = {'1': 1.1666666666666667, '2': 1.5, '3': 1.3333333333333333, '4': 0.6, '5': 1.0, '6': 1.0, '7': 1.8, '8': 1.0, '9': 1.0, '10': 0.9142857142857144, '11': 1.0, '12': 0.5714285714285714, '13': 1.1111111111111112, '14': 1.5555555555555556, '15': 1.0, '16': 0.8888888888888888, '17': 1.0, '18': 1.6666666666666667, '19': 1.0, '20': 1.2727272727272727, '21': 1.0, '22': 0.9230769230769231, '23': 1.0666666666666667, '24': 1.1666666666666667, '25': 1.2, '26': 1.3, '27': 1.0, '28': 1.0, '29': 1.0, '30': 1.2857142857142858, '31': 0.7857142857142857, '32': 1.0, '33': 1.0, '34': 0.9090909090909091, '35': 1.0769230769230769, '36': 0.9230769230769231, '37': 1.0769230769230769, '38': 1.5999999999999999, '39': 1.5333333333333332, '40': 0.9428571428571428, '41': 0.9142857142857144, '42': 1.0222222222222221, '43': 1.0769230769230769, '44': 0.7230769230769231, '45': 1.1923076923076923, '46': 1.0315789473684212, '47': 0.76, '48': 2.0, '49': 1.0, '50': 1.2857142857142858, '51': 1.3333333333333333, '52': 1.1111111111111112, '53': 0.35555555555555557, '54': 1.1428571428571428, '55': 1.4, '56': 0.6666666666666666, '57': 0.6666666666666666, '58': 1.2307692307692308, '59': 1.0666666666666667, '60': 0.6, '61': 1.0526315789473684, '62': 1.44, '63': 1.0, '64': 0.6, '65': 1.8, '66': 1.0, '67': 1.3846153846153846, '68': 1.3076923076923077, '69': 1.7142857142857142, '70': 1.6666666666666667, '71': 0.8888888888888888, '72': 1.4444444444444444, '73': 1.5555555555555556, '74': 1.2727272727272727, '75': 1.5454545454545454, '76': 1.1538461538461537, '77': 1.4, '78': 1.3235294117647058, '79': 1.411764705882353, '80': 1.5294117647058822, '81': 0.9473684210526315, '82': 1.0, '83': 1.6, '84': 0.64, '85': 1.0571428571428572, '86': 0.6, '87': 0.7111111111111111, '88': 1.1636363636363638, '89': 0.9818181818181819, '90': 0.9411764705882353, '91': 1.75, '92': 1.0, '93': 1.3333333333333333, '94': 1.2, '95': 1.6, '96': 1.4, '97': 1.2857142857142858, '98': 1.4285714285714286, '99': 1.2857142857142858, '100': 1.4285714285714286, '101': 1.2222222222222223, '102': 1.1666666666666667, '103': 1.3333333333333333, '104': 1.3333333333333333, '105': 1.4545454545454546, '106': 1.3636363636363635, '107': 0.9545454545454546, '108': 1.0, '109': 1.0, '110': 1.3636363636363635, '111': 1.3846153846153846, '112': 1.1538461538461537, '113': 0.9230769230769231, '114': 1.4, '115': 0.8823529411764706, '116': 0.96, '117': 1.3333333333333333, '118': 3.0, '119': 1.0, '120': 1.0, '121': 1.0, '122': 1.2, '123': 0.8, '124': 0.7142857142857143, '125': 0.7142857142857143, '126': 0.7142857142857143, '127': 0.8571428571428571, '128': 0.7777777777777778, '129': 0.7777777777777778, '130': 0.8888888888888888, '131': 0.5555555555555556, '132': 0.7272727272727273, '133': 0.6363636363636364, '134': 0.6666666666666666, '135': 0.7692307692307693, '136': 2.0, '137': 0.6, '138': 0.8, '139': 0.4444444444444444, '140': 0.5, '141': 2.0, '142': 2.0, '143': 2.0, '144': 0.6666666666666666, '145': 0.5714285714285714, '146': 0.7777777777777778, '147': 0.6, '148': 0.8, '149': 0.5714285714285714, '150': 0.6, '151': 9.181818181818182, '152': 0.6, '153': 0.5, '154': 1.0, '155': 0.6428571428571429, '156': 0.8571428571428571, '157': 0.5, '158': 0.5714285714285714, '159': 0.5, '160': 0.8}

prefer_cost_curve = [3, 3, 3, 4, 4, 4, 3, 2, 2, 2]
picked_cost_curve = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# game loop
while True:
    for i in range(2):
        player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
        # print("first line",player_health, player_mana, player_deck, player_rune, player_draw, file=sys.stderr)
        if i == 0:
            player_state = [player_health, player_mana, player_deck, player_rune, player_draw]
        else:
            op_state = [player_health, player_mana, player_deck, player_rune, player_draw]
    opponent_hand, opponent_actions = [int(i) for i in input().split()]
    for i in range(opponent_actions):
        card_number_and_action = input()
        
    card_count = int(input())
    card_draft_id = []
    card_draft_list = {}
    player_hand = {}
    player_board = {}
    op_board = {}
    for i in range(card_count):
        card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw = input().split()
        card_number = int(card_number)
        instance_id = int(instance_id)
        location = int(location)
        card_type = int(card_type)
        cost = int(cost)
        attack = int(attack)
        defense = int(defense)
        my_health_change = int(my_health_change)
        opponent_health_change = int(opponent_health_change)
        card_draw = int(card_draw)
        
        if player_state[1] == 0:
            card_draft_list[str(card_number)] = [card_value_list[str(card_number)], card_type, cost]
            card_draft_id.append(card_number)
        else:
            if location == 0:
                player_hand[str(card_value_list[str(card_number)])] = [card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw]
            elif location == 1:
                player_board[str(card_value_list[str(card_number)])] = [card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw]
            elif location == -1:
                op_board[str(card_value_list[str(card_number)])] = [card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw]
    
    print_str = ""
    if player_state[1] == 0:
        print("Draft", file=sys.stderr)
        pick_percent = []
        for i in range(3):
            if card_draft_list[str(card_draft_id[i])][1] == 0:
                if card_draft_list[str(card_draft_id[i])][2] < 2:
                    p = prefer_cost_curve[0] - picked_cost_curve[0]
                elif card_draft_list[str(card_draft_id[i])][2] < 3:
                    p = prefer_cost_curve[1] - picked_cost_curve[1]
                elif card_draft_list[str(card_draft_id[i])][2] < 4:
                    p = prefer_cost_curve[2] - picked_cost_curve[2]
                elif card_draft_list[str(card_draft_id[i])][2] < 5:
                    p = prefer_cost_curve[3] - picked_cost_curve[3]
                elif card_draft_list[str(card_draft_id[i])][2] < 6:
                    p = prefer_cost_curve[4] - picked_cost_curve[4]
                elif card_draft_list[str(card_draft_id[i])][2] < 7:
                    p = prefer_cost_curve[5] - picked_cost_curve[5]
                else:
                    p = prefer_cost_curve[6] - picked_cost_curve[6]
            elif card_draft_list[str(card_draft_id[i])][1] == 1:
                p = prefer_cost_curve[7] - picked_cost_curve[7]
            elif card_draft_list[str(card_draft_id[i])][1] == 2:
                p = prefer_cost_curve[8] - picked_cost_curve[8]
            else:
                p = prefer_cost_curve[9] - picked_cost_curve[9]
            pick_percent.append(p)
        # print("prefer", prefer_cost_curve, file=sys.stderr)
        # print("pick_percent", pick_percent, file=sys.stderr)
        for i in range(3):
            if pick_percent[i] > 0:
                pick_percent[i] = (1 + pick_percent[i]/50) * card_draft_list[str(card_draft_id[i])][0]
        # print("pick_percent", pick_percent, file=sys.stderr)
        pick_number = pick_percent.index(max(pick_percent))
        print_str += "PICK " + str(pick_number)
        
        if card_draft_list[str(card_draft_id[pick_number])][1] == 0:
            if card_draft_list[str(card_draft_id[pick_number])][2] < 2:
                picked_cost_curve[0] += 1
            elif card_draft_list[str(card_draft_id[pick_number])][2] < 3:
                picked_cost_curve[1] += 1
            elif card_draft_list[str(card_draft_id[pick_number])][2] < 4:
                picked_cost_curve[2] += 1
            elif card_draft_list[str(card_draft_id[pick_number])][2] < 5:
                picked_cost_curve[3] += 1
            elif card_draft_list[str(card_draft_id[pick_number])][2] < 6:
                picked_cost_curve[4] += 1
            elif card_draft_list[str(card_draft_id[pick_number])][2] < 7:
                picked_cost_curve[5] += 1
            else:
                picked_cost_curve[6] += 1
        elif card_draft_list[str(card_draft_id[pick_number])][1] == 1:
            picked_cost_curve[7] += 1
        elif card_draft_list[str(card_draft_id[pick_number])][1] == 2:
            picked_cost_curve[8] += 1
        else:
            picked_cost_curve[9] += 1
        # print("picked", picked_cost_curve, file=sys.stderr)
            
    else:
        print("Battle", file=sys.stderr)
        G = 0
        op_G = {}
        for value in op_board.values():
            if "G" in value[7]:
                G = 1
                op_G[str(value[1])] = [value[6], value[1]]
        op_G_seq = sorted(op_G.values())
        
        att_seq = []
        for value in player_board.values():
            bisect.insort(att_seq, [value[5], value[1]])
        
        if len(player_hand) > 0 and len(player_board) < 6:
            value_seq = sorted(player_hand.keys())
            value_seq.reverse()
            used = []
            for i in range(len(player_hand)):
                use_card = 0
                if player_state[1] < 0:
                    break
                if player_hand[value_seq[i]][4] < player_state[1]:
                    if player_hand[value_seq[i]][3] == 0:
                        print_str += "SUMMON " + str(player_hand[value_seq[i]][1]) + ";"
                        used.append(i)
                        use_card = 1
                        player_board[value_seq[i]] = player_hand[value_seq[i]]
                        if "C" in player_board[value_seq[i]][7]:
                            bisect.insort(att_seq, [player_board[value_seq[i]][5], player_board[value_seq[i]][1]])
                    elif player_hand[value_seq[i]][3] == 1:
                        if len(att_seq) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(att_seq[-1][1]) + ";"
                            used.append(i)
                            use_card = 1
                    elif player_hand[value_seq[i]][3] == 2:
                        if len(op_G) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(op_G_seq[0][1]) + ";"
                            op_G_seq[0][0] -= player_hand[value_seq[i]][6]
                            if op_G_seq[0][0] <= 0:
                                del op_G_seq[0]
                            used.append(i)
                            use_card = 1
                    elif player_hand[value_seq[i]][3] == 3:
                        if len(op_G) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(op_G_seq[0][1]) + ";"
                            op_G_seq[0][0] -= player_hand[value_seq[i]][6]
                            if op_G_seq[0][0] <= 0:
                                del op_G_seq[0]
                        else:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + "-1" + ";"
                        used.append(i)
                        use_card = 1
                if use_card == 1:
                    player_state[1] -= player_hand[value_seq[i]][4]
            for i in range(len(used)):
                del player_hand[value_seq[used[i]]]
                
        if len(player_hand) > 0 and len(player_board) < 6:
            value_seq = sorted(player_hand.keys())
            value_seq.reverse()
            used = []
            for i in range(len(player_hand)):
                use_card = 0
                if player_state[1] < 0:
                    break
                if player_hand[value_seq[i]][4] < player_state[1]:
                    if player_hand[value_seq[i]][3] == 0:
                        print_str += "SUMMON " + str(player_hand[value_seq[i]][1]) + ";"
                        used.append(i)
                        use_card = 1
                        player_board[value_seq[i]] = player_hand[value_seq[i]]
                        if "C" in player_board[value_seq[i]][7]:
                            bisect.insort(att_seq, [player_board[value_seq[i]][5], player_board[value_seq[i]][1]])
                    elif player_hand[value_seq[i]][3] == 1:
                        if len(att_seq) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(att_seq[-1][1]) + ";"
                            used.append(i)
                            use_card = 1
                    elif player_hand[value_seq[i]][3] == 2:
                        if len(op_G) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(op_G_seq[0][1]) + ";"
                            op_G_seq[0][0] -= player_hand[value_seq[i]][6]
                            if op_G_seq[0][0] <= 0:
                                del op_G_seq[0]
                            used.append(i)
                            use_card = 1
                    elif player_hand[value_seq[i]][3] == 3:
                        if len(op_G) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(op_G_seq[0][1]) + ";"
                            op_G_seq[0][0] -= player_hand[value_seq[i]][6]
                            if op_G_seq[0][0] <= 0:
                                del op_G_seq[0]
                        else:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + "-1" + ";"
                        used.append(i)
                        use_card = 1
                if use_card == 1:
                    player_state[1] -= player_hand[value_seq[i]][4]
            for i in range(len(used)):
                del player_hand[value_seq[used[i]]]
                    
        
        atted = []
        for i in range(len(att_seq)):
            killed = []
            for value in op_G_seq:
                print_str += "ATTACK " + str(att_seq[i][1]) + " " + str(value[1]) + ";"
                atted.append(att_seq[i][1])
                op_G[str(value[1])][0] -= att_seq[i][0]
                if op_G[str(value[1])][0] <= 0:
                    killed.append(value)
                break
            if len(killed) > 0:
                op_G_seq.remove(killed[0])
            if len(op_G_seq) == 0:
                break
        for value in player_board.values():
            if value[1] not in atted:
                print_str += "ATTACK " + str(value[1]) + " -1" + ";"
                
        if len(player_hand) > 0 and len(player_board) < 6:
            value_seq = sorted(player_hand.keys())
            value_seq.reverse()
            used = []
            for i in range(len(player_hand)):
                use_card = 0
                if player_state[1] < 0:
                    break
                if player_hand[value_seq[i]][4] < player_state[1]:
                    if player_hand[value_seq[i]][3] == 0:
                        print_str += "SUMMON " + str(player_hand[value_seq[i]][1]) + ";"
                        used.append(i)
                        use_card = 1
                        player_board[value_seq[i]] = player_hand[value_seq[i]]
                        if "C" in player_board[value_seq[i]][7]:
                            bisect.insort(att_seq, [player_board[value_seq[i]][5], player_board[value_seq[i]][1]])
                    elif player_hand[value_seq[i]][3] == 1:
                        if len(att_seq) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(att_seq[-1][1]) + ";"
                            used.append(i)
                            use_card = 1
                    elif player_hand[value_seq[i]][3] == 2:
                        if len(op_G) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(op_G_seq[0][1]) + ";"
                            op_G_seq[0][0] -= player_hand[value_seq[i]][6]
                            if op_G_seq[0][0] <= 0:
                                del op_G_seq[0]
                            used.append(i)
                            use_card = 1
                    elif player_hand[value_seq[i]][3] == 3:
                        if len(op_G) > 0:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + str(op_G_seq[0][1]) + ";"
                            op_G_seq[0][0] -= player_hand[value_seq[i]][6]
                            if op_G_seq[0][0] <= 0:
                                del op_G_seq[0]
                        else:
                            print_str += "USE " + str(player_hand[value_seq[i]][1]) + " " + "-1" + ";"
                        used.append(i)
                        use_card = 1
                if use_card == 1:
                    player_state[1] -= player_hand[value_seq[i]][4]
            
        

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(print_str)
