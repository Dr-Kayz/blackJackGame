import random
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""
cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_first(cards_list):
    p_first=deal_card(cards_list)
    p_second=deal_card(cards_list)
    comp_first=deal_card(cards_list)
    comp_sec=deal_card(cards_list)
    if p_first==11 and p_second==11:
        p_second=1
    if comp_first==1 and comp_sec==1:
        comp_sec=1
    p_hand=[p_first,p_second]
    c_hand=[comp_first,comp_sec]
    return p_hand, c_hand

def deal_card(cards_list):
    card=random.choice(cards_list)
    return card

def get_total(hand):
    total =0
    for i in hand:
        total+=i
    return total

def show_hands(p_hand,c_hand):
    total= get_total(p_hand)
    print(f"Your cards: {p_hand}, Current score: {total}")
    print(f"Computer's first card: {c_hand[0]}")

def final_print(p_hand, c_hand):
    p_tot= get_total(p_hand)
    c_tot= get_total(c_hand)
    print(f"Your final hand: {p_hand}, Final score: {p_tot}")
    print(f"Computer's final hand: {c_hand}, Final score: {c_tot}")

def check_result(player_hand, comp_hand):
    player_total=get_total(player_hand)
    comp_total= get_total(comp_hand)
    if player_total > 21 and comp_total>21:
        final_print(player_hand, comp_hand)
        print("Draw! You and the computer went above the limit of 21 🙂")
    elif player_total >21:
        final_print(player_hand, comp_hand)
        print("You lose! You went over the limit 🤨 ")
    elif comp_total>21:
        final_print(player_hand, comp_hand)
        print("Computer went over. You win! 😁")
    elif player_total>comp_total:
        final_print(player_hand, comp_hand)
        print("You win! 😎🥳")
    elif player_total < comp_total:
        final_print(player_hand, comp_hand)
        print("You lose! 🫠")
    elif player_total==comp_total:
        final_print(player_hand, comp_hand)
        print("It's a draw! 🫥")

def blackJack():
    check= input("Do you want to play the black Jack game? Type 'y' or 'n': ").lower()
    if check=='y':
        print(logo)
        player_hand,computer_hand=deal_first(cards)
        show_hands(player_hand, computer_hand)
        comp_total= get_total(computer_hand)

        while True:
            if comp_total<17:
                new_card=deal_card(cards)
                if new_card==11 and comp_total>10:
                    new_card=1
                computer_hand.append(new_card)
            add=input("Type 'y' to get another card or 'n' to pass: ").lower()
            if add=='y':
                p_new=deal_card(cards)
                if p_new==11:
                    tot=get_total(player_hand)
                    if tot>10:
                        p_new=1
                player_hand.append(p_new)
                if get_total(player_hand)>21:
                    check_result(player_hand, computer_hand)
                    break
                show_hands(player_hand,computer_hand)
            else:
                check_result(player_hand, computer_hand)
                break
        blackJack()
blackJack()