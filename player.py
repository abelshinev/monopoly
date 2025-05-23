from random import randint
from squares import *

player_list = list()

# Token class is player object
class Token:

    in_jail = False
    double_counter = 0

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
        if self.pos > 40:
            self.pos -= 40
            print(f"{self.name} has passed go and has collected $200")
            self.bal += 200


    def purchase(self, pos: int, type: str):
        """Function for player to buy a property"""
        cost = property_map[pos].price
        print(f"{property_map[pos].name} costs ${cost}")
        if self.bal > cost:
            print(f"{self.name} buys {property_map[pos].name}")
            self.bal -= cost
            self.property_list.append(property_map[pos])
            property_map[pos].is_owned = True

            print(f"{self.name}'s current balance is {self.bal}\n")
        for i in self.property_list:
            print(i.name, end = " ")
        print("]")

        if type == 'u':

            if (property_map[28] in self.property_list and property_map[12] in self.property_list):
                
                property_map[28].has_alt()
                property_map[12].has_alt()
                print(f"{property_map[28].name} = {property_map[28].multi}")
            

    def pay_rent(self, owner):
        payable_amt = int(property_map[self.pos].price/10)
        print(f"{self.name} pays rent of ${payable_amt} to {owner.name}")
        self.bal -= payable_amt
        owner.bal += payable_amt
        print(f"\nCurrent balance of {self.name} is now {self.bal}" +
              f"\nCurrent balance of {owner.name} is now {owner.bal}")
        
    def pay_util_rent(self, owner, die):
        payable_amt = int(die * property_map[self.pos].multi)
        print(f"{self.name} pays rent of ${payable_amt} to {owner.name}")
        self.bal -= payable_amt
        owner.bal += payable_amt
        print(f"\nCurrent balance of {self.name} is now {self.bal}" +
              f"\nCurrent balance of {owner.name} is now {owner.bal}")


    def land_property(self, die, type: str):
        try:
            property_obj = property_map[self.pos]
            print(f"{self.name} has moved {die} spaces to {property_obj.name}." 
                +f"\n{self.name}'s current balance is {self.bal}\n")
            
            if property_obj.is_owned == False:    # If property is not owned
                print(f"{property_obj.name} costs ${property_obj.price}")
                clause = input(f"Do you want to buy {property_obj.name}? (y/n)\n")
                if clause == "y":
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
                            else:
                                self.pay_util_rent(player, die)

        except KeyError:
            
            print(f"{self.name} has moved {die} spaces to unimplemented position {self.pos}." 
                +f"\n{self.name}'s current balance is {self.bal}\n")
            
    def pay_tax(self):
        print(tax_map[self.pos][0], f", {self.name} pays {tax_map[self.pos][1]}")
        self.bal -= tax_map[self.pos][1]
        print(f"{self.name}'s current balance is {self.bal}\n")

    def move(self):
        
        d1, d2 = self.diceroll()

        print(f"{self.name} has rolled a {d1} and a {d2}!\n")
        if self.double_counter == 2:
            if d1 == d2:
                print("Third double go straight to jail")
                self.in_jail = True
                return
        self.pos += d1 + d2
        self.pos_check()
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
            print("Pickup a chance card") 
        elif map_legend[self.pos] == 'cc':
            print("You landed on community chest")
        elif map_legend[self.pos] == 't':
            print(f"{self.name} has moved {d1+d2} spaces to ", end="")
            self.pay_tax()
        else:
            print("Major ERROR: This message should never be printed")


        if d1 == d2:
            if not self.in_jail:
                print(f"{self.name} rolled a double so its their turn again")
                self.double_counter += 1
                self.move()
        self.double_counter = 0

def init_player_list(no_players: int) -> list[Token]:
    """this shit initialises player list"""
    for i in range(1, no_players + 1):
        name = input("Enter player name: ")
        new_player = Token(name, 0, 1500, [])
        player_list.append(new_player)
    
    return player_list

# github commit test