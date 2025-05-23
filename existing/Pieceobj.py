from random import randint
from properti import Prop_dict

in_jail = False  # DEFAULT
start_pos = 0    # VALUES
bal = 2000
property_l = []

def diceroll():    # Dice function
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1, d2


class Piece: # Player Objects 
    def __init__(self, name: str, position: int, in_jail: bool, bal, properties):
        self.name = name
        self.position = position
        self.in_jail = in_jail
        self.bal = bal
        self.properties = properties

    def movement(self): # Movement Function 
        doubles = False

        d1, d2 = diceroll()

        if d1 == d2: doubles = True

        print(f'{self.name} rolled a {d1} and {d2}')
        self.position += (d1+d2) # Movement due to dice 
        if self.position >= 40:              # Reset position after passing GO
            self.position -= 40
            print(f'{self.name} has passed Go and recieves $200')
            self.bal += 200
        print(f'\nCurrent player balance is ${self.bal}')
        

        return doubles #, self.position
    
    def trade(self): # Trade function
        flag = 0
        player = input("Enter the player you want to trade with\n>>> ")
        for i in player_list:
            if i.name == player: # Check if player exists
                if self.name == player:
                    print('RetardError: Cant trade with yourself bozo')
                else:
                    print('ok go trade ')
                    flag += 1
        if flag == 0:
            print(f"ERROR @0x028ab384c1: functype = <'trade'>, await_msg = Player,'{player}' not found")

    def location(self): # Property function
        try:
            location = Prop_dict[self.position]
            print(f'{self.name} is on {location}')
        except KeyError:
            print(f'ERROR @0x019334d11: Location <val = {self.position}> has not been implemented')
            


def players():  

    global player_list  
   
    n = int(input("Enter the number of players\n>>> "))

    if n == 2:
        p1n = input("Enter name of player 1: ")
        p2n = input("Enter name of player 2: ")
        p1 = Piece(p1n, start_pos, in_jail, bal, property_l)
        p2 = Piece(p2n, start_pos, in_jail, bal, property_l)
        player_list = [p1, p2]

    elif n == 3:
        p1n = input("Enter name of player 1: ")
        p2n = input("Enter name of player 2: ")
        p3n = input("Enter name of player 3: ")
        p1 = Piece(p1n, start_pos, in_jail, bal, property_l)
        p2 = Piece(p2n, start_pos, in_jail, bal, property_l)
        p3 = Piece(p3n, start_pos, in_jail, bal, property_l)
        player_list = [p1, p2, p3]

    elif n == 4:
        p1n = input("Enter name of player 1: ")
        p2n = input("Enter name of player 2: ")
        p3n = input("Enter name of player 3: ")
        p4n = input("Enter name of player 4: ")
        p1 = Piece(p1n, start_pos, in_jail, bal, property_l)
        p2 = Piece(p2n, start_pos, in_jail, bal, property_l)
        p3 = Piece(p3n, start_pos, in_jail, bal, property_l)
        p4 = Piece(p4n, start_pos, in_jail, bal, property_l)
        player_list = [p1, p2, p3, p4]
    
    return n, player_list