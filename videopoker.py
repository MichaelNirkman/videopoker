from lib.assets import deck
import lib.debug_functions as d
from lib.hand_analysis import analyze_hand
import lib.printer as printer

def main():
    printer.print_intro()
    running = True
    try:
        deposit, bet = printer.prompt_deposit()
        while running:
        
            deposit = deposit - bet

            current_deck = deck(shuffle=True)
            new_hand = current_deck.pick_card(amount=5)

            printer.print_hand(new_hand, first_draw=True)
            current_deck.shuffle()

            keeps = printer.prompt_keeps()
            new_hand = current_deck.replace_cards(new_hand, keeps)
            printer.print_hand(new_hand)

            deposit = analyze_hand(new_hand, deposit, bet)
            printer.print_status(deposit, bet)

            running = printer.prompt_continue(deposit)

    except KeyboardInterrupt:
        printer.print_goodbye()
        exit()


if __name__ == "__main__":
    main()