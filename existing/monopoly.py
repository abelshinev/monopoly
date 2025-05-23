from random import choice
import Pieceobj as pc
from time import sleep

chance_deck = ['Kill yourself', 'Pay 1000 to the doctor', 'Leave the game', 'Go to jail permanently']
community_chest = ['You won shitstain of the year award please draw $1 you prick', 'Nah you dont even deserve anything', 'Go to the gulag']

class Wild_cards(): # Chance and Community Chest
    def __init__(self, types, pos): 
        self.types = types
        self.pos = pos
                
    def draw(self):
        if self.types == 'chance':
            c_card = choice(chance_deck)
            print(c_card)
        if self.types == 'comm_chest':
            cc_card = choice(community_chest)
            print(cc_card)

# Number of players and list of players brought to main code
n, player_list = pc.players() 

"""vvv Probably redundant code vvv"""
# # Dictionary of all spaces on the board
# Prop_dict = {} 

# for place in board_lay:
#     Prop_dict[place.pos] = place.name # Key is position, value is the name

c_list = [7, 22, 36]
cc_list = [2, 17, 33]

flag = 0

def turn(): # Function for the turn of a player
    sleep(1)
    global flag 
    double = player_list[i].movement() # Calls movement of player who is in their turn
    '(! Redudant)' # First element of tuple returned is the double boolean
    if double:
        flag += 1
        if flag == 3:
            print('3 doubles go to jail')
            flag = 0
        else:
            player_list[i].location()
            turn()
            flag = 0
            '(! Redundant)'# Second element of returned tuple is the player position on the board
    else:
        player_list[i].location()

while True: # Game Loop
    x = input('play?: ')
    if x == 'n':
        print('SYSTEM: "game_terminate.exec", #221i3e5 End_message = ("Game abrupt end")')
        break
    for i in range(n):
        print(f"\n\tIt is {player_list[i].name}'s turn")
        print('-'*30)
        que = input("Do you want to trade? (Y/N)\n>>> ")
        if que.upper() == 'Y':
            player_list[i].trade() # Goes for trading then rolling
            print('Rolling dice...\n')
            turn()
        else:
            print('Rolling dice...\n')
            turn()
