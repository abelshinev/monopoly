from random import randint, choice
from squares import *
from cc_function_list import *

player_list = list()


def return_names(property): # Helper function for comprehensibility
    try:
        return property.name
    except AttributeError:
        print("/!\ WARN: money was inputted to property finder system")
        return property
    
def lock_property(pos: int):
    property_map[pos].lock_child()
    

# Token class is player object
class Token:

    """
    **The brain of the game.**

    To initialise, 
    - name : players name

    Other
    - pos : Live position of the player on the board
    - bal : Current balance of the player
    - properties : An array of all properties owned
        
    """
    in_jail = False
    double_counter = 0
    gojf = False
    bankrupt = False

    def __init__(self, name: str, pos: int, bal: int, properties: list): # Constructor
        self.name = name
        self.pos = pos
        self.bal = bal
        self.property_list = properties

    def diceroll(self):    # Dice function
        d1 = randint(1,6)
        d2 = randint(1,6)
        return d1, d2
    
    def pos_check(self) -> int:
        if self.pos >= 40:
            self.pos -= 40
            print(f"{self.name} has passed go and has collected $200")
            self.bal += 200

    def decrease_bal(self, amt: int):
        if amt < self.bal:
            self.bal -= amt
            return True
        else:
            print(f"/!\ Insufficient balance: You are short ${amt - self.bal}")
            self.bankrupt = True
            return False


    def purchase(self, pos: int, type: str):
        """Function for player to buy a property"""
        cost = property_map[pos].price
        print(f"{property_map[pos].name} costs ${cost}")
        if self.bal > cost:
            print(f"{self.name} buys {property_map[pos].name}")
            self.decrease_bal(cost)
            self.property_list.append(property_map[pos])
            property_map[pos].is_owned = True

            print(f"{self.name}'s current balance is {self.bal}\n")
        else:
            print(f"/!\{self.bal} you have insufficient balance, you are short {cost - self.bal}")
        for i in self.property_list:
            print(i.name, end = " ")
        print("]")

        if type == 'u':

            if (property_map[28] in self.property_list and property_map[12] in self.property_list):
                
                property_map[28].has_alt()
                property_map[12].has_alt()
                print(f"{property_map[28].name} = {property_map[28].multi}")
            

    def pay_rent(self, owner):
        target_property = property_map[self.pos]
        payable_amt = 0

        if target_property.child_lock: 
            if target_property.house_ct == 0:
                payable_amt = (target_property.cost/10 - 4) * 2
            else:
                payable_amt = rent_index[target_property.name][target_property.house_ct-1]
                if (target_property.house_ct <= 4):
                    print(f"{target_property.name} has {target_property.house_ct} houses and therefore rent = ${payable_amt}")
                else:
                    print(f"{target_property.name} has 1 hotel and therefore rent = ${payable_amt}")
            
        else:
            payable_amt = int(target_property.price/10) - 4
        
        x = self.decrease_bal(payable_amt)
        if x:
            print(f"{self.name} pays rent of ${payable_amt} to {owner.name}")
            owner.bal += payable_amt
            print(f"\nCurrent balance of {self.name} is now {self.bal}" +
                f"\nCurrent balance of {owner.name} is now {owner.bal}")
        else:
            print("Sell or be bankrupt")
            

    def trade(self):
        tradee = input("Enter player to trade with: ")
        player = ''     # player is the trade player object
        if tradee == self.name:
            print("/!\ You cannot trade with yourself")
            return 'r'
        for i in player_list:
            if i.name == tradee:
                player = i
        if player == '':
            print(f"{tradee} is not a valid player")
            return 'r'
        
        print(f"You chose to trade with {player.name}")
        print(f"{player.name} has current balance of {player.bal}")
        print(f"Your current balance: {self.bal}")
        print(f"Properties owned are [ ", end="")
        for trade_props in player.property_list:
            print(trade_props.name, end=" ")
        print("]")
        
        def setup_my_list(): 
            """Returns a list with all the property objects that self wants to trade"""
            item_names = list(map(return_names, self.property_list))
            print(item_names)
            my_items = list()   
            
            x = 'a'
            while(x.lower() != 'x'):
                x = input("Enter element/s to trade [X to stop]\n")
                if x in item_names:
                    for prop in self.property_list:
                        if prop.name == x:
                            if prop.child_lock:
                                print(f"{prop.name} is a part of a color set and cant be traded")
                            else:
                                my_items.append(prop)
                                print(f"{prop.name} has been added to inventory")
                elif x.isnumeric():
                    my_items.append(int(x))
                elif x == 'x':
                    pass
                else:
                    print(f"/!\ '{x}' is not a valid place!")

            return my_items

        trade_list = player.property_list
        trade_list_name = list(map(return_names, trade_list))
        trade_item = "a"
        trade_cart = []

        while trade_item.lower() != 'x':
            trade_item = input("Enter interested element from the list [X to stop]\n")
            if (trade_item.isnumeric()):    # Money Input
                print(f"${trade_item} has been added to trade inventory")
                trade_cart.append(int(trade_item))
            elif trade_item in trade_list_name: # Property input
                    for prop in trade_list:
                        if (prop.name == trade_item):
                            # print(f"The child lock on {prop.name} is {prop.child_lock}")    
                            if prop.child_lock:         # Check for color set locking
                                print(f"{prop.name} is a part of a color set and cant be traded")
                            else:
                                trade_cart.append(prop)
                                print(f"{prop.name} has been added to trade inventory")
            elif trade_item == 'x':
                pass
            else:
                print(f"/!\ '{trade_item}' is not a valid place!")

        trade_cart_names = list(map(return_names, trade_cart))
        print(f"{player.name}'s wanted goods -> {trade_cart_names}")
        
        my_list = setup_my_list() 
        my_list_names = list(map(return_names, my_list))
        print(f"{self.name}'s offered -> {my_list_names}")
        print(f"{player.name}'s wanted goods -> {trade_cart_names}")

        confirm = input(f"{player.name}, do you accept the trade?\n\ty: Yes\n\tn: No\n\tc: Counter Offer\n")
        if confirm.lower() == 'y':

            """Self Transactions"""
            for item in trade_cart:  # Recieving
                if isinstance(item, Square):
                    self.property_list.append(item)
                else:
                    self.bal += item
            for item in my_list:    # Sending
                if isinstance(item, Square):
                    self.property_list.remove(item)
                else:
                    self.decrease_bal(item)
            
            """Tradee Transactions"""
            for item in my_list:    # Recieving
                if isinstance(item, Square):
                    player.property_list.append(item)
                else:
                    player.bal += item
            for item in trade_cart: # Sending
                if isinstance(item, Square):
                    player.property_list.remove(item)
                else:
                    player.decrease_bal(item)

            my_new_p_list = list(map(return_names, self.property_list))
            print(my_new_p_list)
            tradee_new_p_list = list(map(return_names, player.property_list))
            print(tradee_new_p_list)

        elif confirm.lower() == 'n':
            print(f"{self.name}, {player.name} has declined your trade")


        finish_check = input("Done?\n")
        if 'n' in finish_check:
            return 'r'
        if 'oth' in finish_check:
            return 'n' # Goes to check statement

    def handle_housing(self):
        target_prop = ''        # target_prop will be the property object
        my_prop_list = list(map(return_names, self.property_list))
        print(my_prop_list)
        t = input("Enter targetted property to add a house to: ")
        
        if t not in my_prop_list:
            return
        
        for prop in self.property_list:
            if prop.name == t:
                target_prop = prop
    
        def house_count(idx: int): # Helper function for mapping
            return property_map[idx].house_ct
        

        print(f"You have chosen to upgrade {target_prop.name}")
        print(target_prop.color, "property")
        color_set = color_index[target_prop.color]
        for prop_index in color_set:
            if property_map[prop_index].name not in my_prop_list:
                print(f"/!\You do not have the full {target_prop.color}  color set!")
                return 'f'
        
        color_set_house_list = list(map(house_count, color_set))
        print(color_set_house_list)

        list(map(lock_property, color_set))
        print(target_prop.color, "PROPERTIES HAVE BEEN LOCKED")
        
        if target_prop.house_ct != min(color_set_house_list):
            print("/!\ Revoking purchase: Your other properties are not up to level")
            return 'r'
        
        
        house_cost = color_to_cost_index[target_prop.color]
        if self.bal < house_cost:
            print(f"/!\ Insufficient balance to upgrade to a house, you are {house_cost - self.bal} short.") 
            return

        if target_prop.house_ct < 4:
            target_prop.house_ct += 1 
            print(f"Buying house on {self.name}'s {target_prop.name} for ${house_cost} ")
            print(f"{target_prop.name} currently has {target_prop.house_ct} houses")
        elif target_prop.house_ct == 5:
            print("You are already at a hotel for", {target_prop.name}, "You cannot build further")
            return
        else: 
            target_prop.house_ct = 5
            print(f"Upgraded to hotel on {self.name}'s {target_prop.name}")
            print(f"{target_prop.name} currently has a hotel") 
        self.decrease_bal(house_cost)
        print("Current balance is", self.bal)


    def pay_util_rent(self, owner, die):
        payable_amt = int(die * property_map[self.pos].multi)
        print(f"{self.name} pays rent of ${payable_amt} to {owner.name}")
        x = self.decrease_bal(payable_amt)
        if x:
            owner.bal += payable_amt
            print(f"\nCurrent balance of {self.name} is now {self.bal}" +
                f"\nCurrent balance of {owner.name} is now {owner.bal}")
        else:
            print("Sell or be bankrupt")
        
    def pay_station(self, owner):
        payable_amt = 50
        print(f"{self.name} pays rent of ${payable_amt} to {owner.name}")
        x = self.decrease_bal(payable_amt)
        if x:
            owner.bal += payable_amt
            print(f"\nCurrent balance of {self.name} is now {self.bal}" +
                f"\nCurrent balance of {owner.name} is now {owner.bal}")
        else:
            print("Sell or be bankrupt")


    def land_property(self, die, type: str):
        try:
            property_obj = property_map[self.pos]
            print(f"{self.name} has moved {die} spaces to {property_obj.name}." 
                +f"\n{self.name}'s current balance is {self.bal}\n")
            
            if type == 'p':
                print(f"Other properties in {property_obj.color} :- \n")
                for property_index in color_index[property_obj.color]:
                    print(f"{property_map[property_index].name}", end="  ")
                print()
            
            if property_obj.is_owned == False:    # If property is not owned
                print(f"{property_obj.name} costs ${property_obj.price}")
                clause = input(f"Do you want to buy {property_obj.name}? (y/n)\n")
                if clause.lower() == "y":
                    self.purchase(self.pos, type=type)
                

            else:
                for player in player_list:
                    if property_obj in player.property_list:
                        if player.name == self.name:
                            print(f"{property_obj.name} belongs to you")
                        else:
                            print(f"{self.name} has landed on {property_obj.name} which belongs to {player.name}")
                            if (type == 'p'):
                                self.pay_rent(player)
                            elif (type == 's'):
                                self.pay_station(player)
                            else:
                                self.pay_util_rent(player, die)

        except KeyError:
            
            print(f"{self.name} has moved {die} spaces to unimplemented position {self.pos}." 
                +f"\n{self.name}'s current balance is {self.bal}\n")
            for i in range(15):
                print("*" * 30)
            
    def pay_tax(self):
        print(tax_map[self.pos][0], f", {self.name} pays {tax_map[self.pos][1]}")
        x = self.decrease_bal(tax_map[self.pos][1])
        if x:
            print(f"{self.name}'s current balance is {self.bal}\n")
        else:
            print("Sell or be bankrupt")

    def wildcard_edge_case(self, card: list): # For very rare edge cases where player_list input required
        if card[1] == 'bday':
            bday(self, player_list)

    def land(self, d1, d2):
        print(f"{self.name}'s current pos = {self.pos}, {map_legend[self.pos]} [temporary]\n\n")
        if map_legend[self.pos] == 'p':
            self.land_property(d1+d2, 'p')
        elif map_legend[self.pos] == 'u':
            self.land_property(d1+d2, 'u')
        elif map_legend[self.pos] == 's':
            self.land_property(d1+d2, 's')
        elif map_legend[self.pos] == 'n':
            print(self.name, null_map[self.pos])
        elif map_legend[self.pos] == 'j':
            print("Go to Jail for fraud")
            self.pos = 10
            self.in_jail = True
        elif map_legend[self.pos] == 'c':
            print(self.name, "Pickup a chance card it reads:\n")
            chance_card = choice(list(chance_deck))     # Typecasts dictionary to list of its keys to use as a choice
            print(chance_card)                          # while still allowing for it to pass the entire key-val pair into the function
            # print("Sendning over to chance fn")
            read_chance_cards(self, chance_deck[chance_card])

        elif map_legend[self.pos] == 'cc': # If current player spot is community chest

            def wildcard_edge_case(card: list): # For very rare edge cases where player_list input required
                if card[0] == 'bday':
                    bday(self, player_list)
            
            print(self.name, "Pickup a community chest card it reads:\n")
            cc_card = choice(list(cc_deck))
            print(cc_card)

            if cc_deck[cc_card][0] == 'bday':
                wildcard_edge_case(cc_deck[cc_card])
            else:
                read_cc_cards(self, cc_deck[cc_card])

        elif map_legend[self.pos] == 't':
            print(f"{self.name} has moved {d1+d2} spaces to ", end="")
            self.pay_tax()
        else:
            print("Major ERROR: This message should never be printed")


    def move(self, double_counter: int):
        
        d1, d2 = self.diceroll()
        print(f"{self.name}'s current position is {self.pos} \ncurrent bal is {self.bal}")

        print(f"{self.name} has rolled a {d1} and a {d2}!\n")
        if double_counter == 2:
            if d1 == d2:
                print("Third double go straight to jail")
                self.in_jail = True
                self.pos = 10
                return
        self.pos += d1 + d2
        self.pos_check()
        self.land(d1, d2)

        if d1 == d2:
            if not self.in_jail:
                print(f"{self.name} rolled a double so its their turn again")
                return True
        
        return False


def init_player_list(no_players: int) -> list[Token]:
    """this shit initialises player list"""
    for i in range(1, no_players + 1):
        name = input("Enter player name: ")
        new_player = Token(name, 0, 1500, [])
        player_list.append(new_player)
    
    return player_list
