
chance_deck = [
    "Advance to Go (Collect $200)",
    "Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
    "Advance to Mayfair",
    "Advance to Trafalgar Square. If you pass Go, collect $200",
    "Advance to Pall Mall. If you pass Go, collect $200",
    "Take a trip to Marylebone Station. If you pass Go, collect $200",
    "Advance to the nearest Utility. If unowned, you may buy it. If owned, pay owner 10x dice roll",
    "Advance to the nearest Railway Station and pay owner twice the rent",
    "Bank pays you dividend of $50",
    "Get out of Jail Free",
    "Go back three spaces",
    "Make general repairs on all your property: $25 per house, $100 per hotel",
    "Pay poor tax of $15",
    "You have been elected Chairman of the Board. Pay each player $50",
    "Your building loan matures. Collect $150",
    "Speeding fine $15"
]

cc_deck = {
    "Advance to Go (Collect $200)": ["move", 0],
    "Bank error in your favour. Collect $200": ["gain", 200],
    "Doctor's fees. Pay $50": ['loss', 50],
    "From sale of stock you get $50": ['gain', 50],
    "Get out of Jail Free": ['gojf', 0],
    "Go to Jail. Go directly to jail, do not pass Go, do not collect $200": ['jail', 0],
    "Holiday fund matures. Receive $100": ['gain', 100],
    "Income tax refund. Collect $20": ['gain', 20],
    "It is your birthday. Collect $10 from every player": ['bday', 10],
    "Life insurance matures. Collect $100": ['gain', 100],
    "Pay hospital fees of $100": ['loss', 100],
    "Pay school fees of $50": ['loss', 50],
    "Receive $25 consultancy fee": ['loss', 25],
    "You are assessed for street repairs: $40 per house, $115 per hotel": ['repair', 0],
    "You have won second prize in a beauty contest. Collect $10": ['gain', 10],
    "You inherit $100": ['gain', 100]
}

def go_to_jail_fns(player):
    pass


def read_chance_cards(player, chance_card): 
    pass

def read_cc_cards(player, cc_card: list):
    if cc_card[0] == 'jail':
        player.in_jail = True
        player.pos = 10
    elif cc_card[0] == 'gain':
        player.bal += cc_card[1]
        print("players current balance is", player.bal)
    elif cc_card[0] == 'loss':
        if (player.decrease_bal(cc_card[1])):
            print("players current balance is", player.bal)
        else:
            print("Bankruptcy :(")
    elif cc_card == 'move':
        if player.pos > cc_card[1]:
            print("You pass go and collect $200")
            player.bal += 200
            player.pos = cc_card[1]
            player.land(0,0)
        else:
            player.land(0,0)