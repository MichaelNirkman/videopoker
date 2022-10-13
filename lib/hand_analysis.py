from collections import Counter
import lib.printer as printer

def analyze_hand(hand, deposit, bet):
    print("")
    is_straight, is_royal = find_straight(hand)
    is_flush = find_flush(hand)
    is_multiple, multiple_type = find_multiples(hand)
    prize = 0
    if is_royal and is_flush:
        printer.print_winning_hand("Royal flush!!!")
        prize = 250
    elif is_flush and is_straight:
        printer.print_winning_hand("Straight flush!")
        prize = 50
    elif is_multiple and  multiple_type == "4OAK":
        printer.print_winning_hand("Four of a kind!")
        prize = 25
    elif is_multiple and multiple_type == "fullhouse":
        printer.print_winning_hand("Full house")
        prize = 9
    elif is_flush:
        printer.print_winning_hand("Flush")
        prize = 6
    elif is_straight:
        printer.print_winning_hand("Straight")
        prize = 4
    elif is_multiple:
        if multiple_type == "3OAK":
            printer.print_winning_hand("Three of a kind")
            prize = 3
        elif multiple_type == "2pair":
            printer.print_winning_hand("Two pairs")
            prize = 2
        elif multiple_type == "jacks":
            printer.print_winning_hand("Pair of Jacks or better")
            prize = 1
    else:
        print("No wins")
    
    if prize > 0:
        wins = prize * bet
        printer.print_wins(wins)
        deposit = deposit + wins

    return deposit

def find_straight(hand):
    is_straight = True
    is_royal = False

    sorted_hand = hand.copy()
    sorted_hand.sort(key=(lambda x: x.rank))
    initial_rank = sorted_hand.pop(0).rank
    
    for card in sorted_hand:
        compared_rank = card.rank
        if compared_rank == initial_rank + 1:
            initial_rank = compared_rank
        else:
            is_straight = False
            break
    
    if is_straight and sorted_hand[-1].rank == 12:
        is_royal = True

    return is_straight, is_royal

def find_flush(hand):
    flush = False

    suitcount = Counter(i.suit for i in hand)
    if len(suitcount.values()) == 1:
        flush = True
    
    return flush

def find_multiples(hand):
    is_multiple = True
    multiple_type = ""
    ranks = list(r.rank for r in hand)
    rankcounter = Counter(ranks)
    rankvalues = rankcounter.values()

    if len(rankcounter.keys()) == 2 and 2 in rankvalues and 3 in rankvalues:
        multiple_type = "fullhouse"
    elif 4 in rankvalues:
        multiple_type = "4OAK"
    elif 3 in rankvalues:
        multiple_type = "3OAK"
    elif list(rankvalues).count(2) == 2:
        multiple_type = "2pair"
    elif 2 in rankvalues:
        high_ranks = [c.rank for c in hand if c.high]
        found_pair = rankcounter.most_common(1)[0][0]
       
        if found_pair in high_ranks:
            multiple_type="jacks"
        else:
            is_multiple = False
    else:
        is_multiple = False

    return is_multiple, multiple_type
