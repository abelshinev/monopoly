# from player import Token
from squares import Property

chance_deck = {
#     "Advance to Go (Collect $200)": ['move', 0],
#     "Go to Jail. Go directly to jail, do not pass Go, do not collect $200": ['jail', 0],
#     "Advance to Mayfair": ['move', 40],
#     "Advance to Trafalgar Square. If you pass Go, collect $200": ['gain', 200],
#     "Advance to Pall Mall. If you pass Go, collect $200": ['move', 11],
#     "Take a trip to Marylebone Station. If you pass Go, collect $200": ['move', 15],
#     "Advance to the nearest Utility. If unowned, you may buy it. If owned, pay owner 10x dice roll": ['move', 12],
#     "Advance to the nearest Railway Station and pay owner twice the rent": ['move', 5],
#     "Bank pays you dividend of $50": ['gain', 50],
    "Get out of Jail Free": ['gojf', 0],
    # "Go back three spaces": ['move', -3],
    "Make general repairs on all your property: $25 per house, $100 per hotel": ['repair', 'c'],
#     "Pay poor tax of $15": ['loss', 15],
#     "You have been elected Chairman of the Board. Pay each player $50": ['lossall', 50],
#     "Your building loan matures. Collect $150": ['gain', 150],
#     "Speeding fine $15": ['loss', 15],
}
CHANCE_GOJF_LOCK = False

cc_deck = {
    # "Advance to Go (Collect $200)": ["move", 0],
    # "Bank error in your favour. Collect $200": ["gain", 200],
    # "Doctor's fees. Pay $50": ['loss', 50],
    # "From sale of stock you get $50": ['gain', 50],
    "Get out of Jail Free": ['gojf', 0],
    # "Go to Jail. Go directly to jail, do not pass Go, do not collect $200": ['jail', 0],
    # "Holiday fund matures. Receive $100": ['gain', 100],
    # "Income tax refund. Collect $20": ['gain', 20],
    "It is your birthday. Collect $10 from every player": ['bday', 10],
    # "Life insurance matures. Collect $100": ['gain', 100],
    # "Pay hospital fees of $100": ['loss', 100],
    # "Pay school fees of $50": ['loss', 50],
    # "Receive $25 consultancy fee": ['loss', 25],
    "You are assessed for street repairs: $40 per house, $115 per hotel": ['repair', 'cc'],
    # "You have won second prize in a beauty contest. Collect $10": ['gain', 10],
    # "You inherit $100": ['gain', 100],
}
CC_GOJF_LOCK = False

def gojf_fix(player):
    global CC_GOJF_LOCK, CHANCE_GOJF_LOCK
    print("UNLOCKING GOJF")
    if CC_GOJF_LOCK:
        cc_deck.update({"Get out of Jail Free": ['gojf', 0]})
        CC_GOJF_LOCK = False
        print("\nCOMM CHEST GOJF REFILLED")
    elif CHANCE_GOJF_LOCK:
        chance_deck.update({"Get out of Jail Free": ['gojf', 0]})
        CHANCE_GOJF_LOCK = False
        print("\nCHANCE GOJF REFILLED")
    player.gojf = False


def gojf(player):
    print("GET OUT OF JAIL FREE card has been added to your inventory,", player.name)
    player.gojf = True
    print("GOJF LOCKED")
    


def bday(player, player_list: list):
    print("BDAY FN")
    for other in player_list:
        player.bal += 10
        other.decrease_bal(10)

def repair(player, type: str):
    print("REPAIR FN")
    houses = 0
    hotels = 0
    for prop in player.property_list:
        if isinstance(prop, Property):
            print(prop.name, "-", prop.house_ct)
            if prop.house_ct == 5:
                hotels += 1
            else:
                houses += prop.house_ct
        
    print("Hotels -> ", hotels, "\nHouses -> ", houses)
    payable_amt = 0
    if type == 'c':
        payable_amt = 100 * hotels + 25 * houses
    elif type == 'cc':
        payable_amt = 115 * hotels + 40 * houses
    else:
        print("This cannot happen")
    
    print(f"Amount = {100 * hotels} + {25 * houses} = {payable_amt}")
    payment_status = player.decrease_bal(payable_amt)
    if not payment_status:
        print("Bankruptcy :(")


def go_to_jail_fns(player):
    print(f"{player.name} is now in {player.pos} aka Jail [temporary]")
    player.in_jail = True
    player.pos = 10


def read_chance_cards(player, chance_card: list): 
    global CHANCE_GOJF_LOCK
    # print("Recieved chance fn", chance_card)
    if chance_card[0] == 'jail':
        go_to_jail_fns(player)
    elif chance_card[0] == 'gain':
        player.bal += chance_card[1]
        print("players current balance is", player.bal)
    elif chance_card[0] == 'loss':
        if (player.decrease_bal(chance_card[1])):
            print("players current balance is", player.bal)
        else:
            print("Bankruptcy :(")
    elif chance_card[0] == 'move':
        # print("Movement detected")
        if chance_card[1] < 0:
            print(f" {player.name} is moving {chance_card[1]} steps")
            player.pos += chance_card[1]
        else:
            if player.pos > chance_card[1]:
                print("You pass go and collect $200")
                player.bal += 200
                player.pos = chance_card[1]
        
        player.land(0,0)
    elif chance_card[0] == 'repair':
        repair(player, chance_card[1])
    elif chance_card[0] == 'gojf':
        CHANCE_GOJF_LOCK = True
        del chance_deck["Get out of Jail Free"]
        gojf(player)

    else:
        print("IMPOSSIBLE! NOT HERE ?!")

def read_cc_cards(player, cc_card: list):
    global CC_GOJF_LOCK
    if cc_card[0] == 'jail':
        go_to_jail_fns(player)
    elif cc_card[0] == 'gain':
        player.bal += cc_card[1]
        print("players current balance is", player.bal)
    elif cc_card[0] == 'loss':
        if (player.decrease_bal(cc_card[1])):
            print("players current balance is", player.bal)
        else:
            print("Bankruptcy :(")
    elif cc_card[0] == 'move':

        if player.pos > cc_card[1]:
            print("You pass go and collect $200")
            player.bal += 200
            player.pos = cc_card[1]
        
        player.land(0,0)
    elif cc_card[0] == 'repair':
        repair(player, cc_card[1])
    elif cc_card[0] == 'gojf':
        CC_GOJF_LOCK = True
        del cc_deck["Get out of Jail Free"]
        gojf(player)

    else:
        print("NOT HERE ? ")