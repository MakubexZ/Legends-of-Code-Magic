import sys
import math
import bisect

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
card_value_cost = [2.16666667, 1.29012346, 1.03833333, 1.00529101, 1.00589226, 0.93838384, 0.96428571, 0.99074074, 1.00392157, 0.9005848, 0., 0., 1.]

card_value_list = {'1': 1.1666666666666667, '2': 1.5, '3': 1.3333333333333333, '4': 1.2, '5': 1.0, '6': 1.0, '7': 1.4, '8': 1.0, '9': 1.0, '10': 0.7142857142857143, '11': 1.0, '12': 1.0, '13': 1.1111111111111112, '14': 1.1111111111111112, '15': 1.0, '16': 0.8888888888888888, '17': 1.0, '18': 1.2222222222222223, '19': 1.0, '20': 0.9090909090909091, '21': 1.0, '22': 0.9230769230769231, '23': 1.0666666666666667, '24': 1.1666666666666667, '25': 1.2, '26': 1.3, '27': 1.0, '28': 1.0, '29': 1.0, '30': 1.2857142857142858, '31': 0.7857142857142857, '32': 1.0, '33': 1.0, '34': 0.9090909090909091, '35': 0.8846153846153846, '36': 0.9230769230769231, '37': 1.0769230769230769, '38': 1.4444444444444444, '39': 1.222222222222222, '40': 0.8095238095238095, '41': 0.7142857142857143, '42': 0.8148148148148148, '43': 0.8974358974358974, '44': 0.8461538461538461, '45': 0.9615384615384616, '46': 0.8596491228070174, '47': 1.2666666666666666, '48': 2.0, '49': 0.6666666666666667, '50': 1.2857142857142858, '51': 1.3333333333333333, '52': 1.1111111111111112, '53': 0.2777777777777778, '54': 1.1428571428571428, '55': 1.1666666666666665, '56': 1.0, '57': 1.0, '58': 1.0384615384615385, '59': 1.0666666666666667, '60': 0.8, '61': 1.0526315789473684, '62': 1.2, '63': 0.9333333333333333, '64': 0.4333333333333333, '65': 1.4, '66': 0.8181818181818182, '67': 1.2307692307692308, '68': 1.1538461538461537, '69': 1.4285714285714286, '70': 1.3333333333333333, '71': 0.7222222222222222, '72': 1.1666666666666667, '73': 1.3333333333333333, '74': 1.0454545454545454, '75': 1.2727272727272727, '76': 0.9615384615384616, '77': 1.1666666666666667, '78': 1.1764705882352942, '79': 1.1764705882352942, '80': 1.2941176470588236, '81': 0.7894736842105263, '82': 0.8333333333333334, '83': 2.5, '84': 0.5, '85': 0.8571428571428571, '86': 0.9285714285714286, '87': 0.8888888888888888, '88': 0.9090909090909091, '89': 0.7272727272727273, '90': 0.7352941176470589, '91': 1.8333333333333335, '92': 0.7222222222222223, '93': 1.0555555555555556, '94': 1.1333333333333333, '95': 1.1, '96': 1.0666666666666667, '97': 0.9285714285714286, '98': 0.9523809523809524, '99': 1.119047619047619, '100': 1.1428571428571428, '101': 0.8518518518518519, '102': 0.8888888888888888, '103': 1.1111111111111112, '104': 0.9629629629629629, '105': 1.0, '106': 0.9848484848484849, '107': 0.7272727272727273, '108': 0.8181818181818182, '109': 1.0, '110': 0.9545454545454546, '111': 1.0, '112': 0.9358974358974359, '113': 0.6666666666666667, '114': 1.011111111111111, '115': 0.6372549019607844, '116': 0.8, '117': 1.3333333333333333, '118': 3.0, '119': 1.0, '120': 1.0, '121': 1.0, '122': 1.2, '123': 0.8, '124': 0.7142857142857143, '125': 0.7142857142857143, '126': 0.7142857142857143, '127': 0.8571428571428571, '128': 0.7777777777777778, '129': 0.7777777777777778, '130': 0.8888888888888888, '131': 0.5555555555555556, '132': 0.7272727272727273, '133': 0.6363636363636364, '134': 0.6666666666666666, '135': 0.7692307692307693, '136': 2.0, '137': 0.6, '138': 0.8, '139': 0.4444444444444444, '140': 0.5, '141': 2.0, '142': 2.0, '143': 2.0, '144': 0.6666666666666666, '145': 0.5714285714285714, '146': 0.7777777777777778, '147': 0.6, '148': 0.8, '149': 0.5714285714285714, '150': 0.6, '151': 9.181818181818182, '152': 0.6, '153': 0.5, '154': 1.0, '155': 0.6428571428571429, '156': 0.8571428571428571, '157': 0.5, '158': 0.5714285714285714, '159': 0.5, '160': 0.8}

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
            card_draft_list[str(card_number)] = card_value_list[str(card_number)]
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
        pick_card_id = max(card_draft_list, key=card_draft_list.get)
        pick_number = card_draft_id.index(int(pick_card_id))
        print_str += "PICK " + str(pick_number)
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
            for i in range(len(player_hand)):
                if player_state[1] <= 0:
                    break
                if player_hand[value_seq[i]][4] < player_state[1]:
                    print_str += "SUMMON " + str(player_hand[value_seq[i]][1]) + ";"
                    player_state[1] -= player_hand[value_seq[i]][4]
        
            
        

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(print_str)
