from time import sleep
from var.constants import bcolors as c
import os, platform

def print_intro():
    clear_screen()
    print(f"\n{c.BOLD}Terminal Poker Night{c.ENDC}\n")

def print_goodbye():
    print("\n\nGoodbye!\n")

def print_hand(hand, first_draw=False):
    clear_screen()
    if first_draw:
        print(f"\n\n{c.BOLD}- Dealing cards- {c.ENDC}\n")
    else:
        print("")
    for i in range(0, len(hand)):
        print(hand[i], end=" ", flush=True)
        sleep(500/1000)
    if first_draw:
        print("\n\n 1   2   3   4   5\n")
    else:
        print("")

def print_status(deposit, bet):
    print(f"\nCash: {c.WARNING}{deposit}{c.ENDC}, bet: {c.OKBLUE}{bet}{c.ENDC}\n")

def prompt_keeps():
    print("\nKeep any cards?")
    keeps = input("1-5 or \"all\": ")
    print("")
    return keeps

def prompt_continue(deposit):
    running = True
    if deposit > 0:
        input("\nPress enter to continue")
    else:
        print("\nYou ran out of money, better luck next time...\n")
        running = False
    return running

def prompt_deposit():
    deposit = prompt_for_int("Input cash deposit (50): ", 50)
    bet = prompt_for_int("Input Bet (5): ", 5)
    return deposit, bet

def prompt_for_int(msg, default):
    prompting = True
    value = ""
    while prompting:
        try:
            value = int(input(msg) or default)
            prompting = False
        except ValueError:
            print("Please supply a number")
    return value

def print_winning_hand(msg):
    print(f"{c.OKGREEN}{msg}{c.ENDC}")

def print_wins(prize):
    print(f"You win {c.WARNING}{prize}{c.ENDC}")

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')