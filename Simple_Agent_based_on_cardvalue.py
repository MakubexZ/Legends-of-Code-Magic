import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
card_value_cost = [2.5, 0.92592593, 0.85, 0.81746032, 0.85353535, 0.80606061, 0.78021978, 0.88888889, 0.72941176, 0.80701754, 0., 0., 0.8]
 
card_value_list = {'1': 1.0, '2': 1.0, '3': 1.3333333333333333, '4': 1.2, '5': 1.0, '6': 1.0, '7': 0.8, '8': 1.0, '9': 1.0, '10': 0.5714285714285714, '11': 1.0, '12': 1.0, '13': 0.8888888888888888, '14': 1.1111111111111112, '15': 1.0, '16': 0.8888888888888888, '17': 1.0, '18': 1.2222222222222223, '19': 1.0, '20': 0.9090909090909091, '21': 1.0, '22': 0.9230769230769231, '23': 1.0666666666666667, '24': 0.6666666666666666, '25': 0.8, '26': 1.0, '27': 0.8, '28': 0.6, '29': 0.6, '30': 0.8571428571428571, '31': 0.5714285714285714, '32': 0.7142857142857143, '33': 0.7777777777777778, '34': 0.7272727272727273, '35': 0.5384615384615384, '36': 0.6153846153846154, '37': 0.9230769230769231, '38': 1.3333333333333333, '39': 1.0, '40': 0.7142857142857143, '41': 0.5714285714285714, '42': 0.6666666666666666, '43': 0.7692307692307693, '44': 0.7692307692307693, '45': 0.8461538461538461, '46': 0.7368421052631579, '47': 1.2, '48': 0.6666666666666666, '49': 0.6, '50': 0.7142857142857143, '51': 0.8888888888888888, '52': 0.6666666666666666, '53': 0.2222222222222222, '54': 0.5714285714285714, '55': 1.0, '56': 1.0, '57': 1.0, '58': 0.8461538461538461, '59': 0.9333333333333333, '60': 0.8, '61': 1.0526315789473684, '62': 0.96, '63': 0.8, '64': 0.4, '65': 0.8, '66': 0.5454545454545454, '67': 0.7692307692307693, '68': 0.9230769230769231, '69': 1.1428571428571428, '70': 1.0, '71': 0.5555555555555556, '72': 0.8888888888888888, '73': 0.8888888888888888, '74': 0.8181818181818182, '75': 1.0, '76': 0.7692307692307693, '77': 0.9333333333333333, '78': 0.5882352941176471, '79': 0.9411764705882353, '80': 0.9411764705882353, '81': 0.631578947368421, '82': 0.6666666666666666, '83': 2.0, '84': 0.4, '85': 0.7142857142857143, '86': 0.8571428571428571, '87': 0.7777777777777778, '88': 0.7272727272727273, '89': 0.45454545454545453, '90': 0.5882352941176471, '91': 3.0, '92': 0.3333333333333333, '93': 1.0, '94': 1.0, '95': 1.0, '96': 1.0, '97': 0.8571428571428571, '98': 0.8571428571428571, '99': 1.0, '100': 1.0, '101': 0.7777777777777778, '102': 0.6666666666666666, '103': 1.0, '104': 0.8888888888888888, '105': 0.9090909090909091, '106': 0.9090909090909091, '107': 0.5454545454545454, '108': 0.7272727272727273, '109': 1.0, '110': 0.8181818181818182, '111': 0.9230769230769231, '112': 0.8461538461538461, '113': 0.46153846153846156, '114': 0.9333333333333333, '115': 0.5882352941176471, '116': 0.64}

# game loop
while True:
    for i in range(2):
        player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
        # print("first line",player_health, player_mana, player_deck, player_rune, player_draw, file=sys.stderr)
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
        
        if player_mana == 0:
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
    if player_mana == 0:
        print("Draft", file=sys.stderr)
        pick_card_id = max(card_draft_list, key=card_draft_list.get)
        pick_number = card_draft_id.index(int(pick_card_id))
        print_str += "PICK " + str(pick_number)
    else:
        print("Battle", file=sys.stderr)
        if len(player_hand) > 0:
            value_seq = sorted(player_hand.keys())
            for i in range(len(player_hand)):
                if player_mana <= 0:
                    break
                if player_hand[value_seq[i]][4] < player_mana:
                    print_str += "SUMMON " + str(player_hand[value_seq[i]][1]) + ";"
                    player_mana -= player_hand[value_seq[i]][4]
        for value in player_board.values():
            print_str += "ATTACK " + str(value[1]) + " -1" + ";"
            
        

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(print_str)
