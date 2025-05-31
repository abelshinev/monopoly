from squares import chance_deck, cc_deck
from player import Token

def go_to_jail_fns(player: Token):
    pass


def read_chance_cards(player: Token, chance_card): 
    pass

def read_cc_cards(player: Token, cc_card):
    if cc_deck[cc_card][0] == 'jail':
        player.in_jail = True
        player.pos = 10
    elif cc_deck[cc_card][0] == 'gain':
        player.bal += cc_deck[cc_card][1]