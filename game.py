from player import init_player_list, Token
from cc_function_list import gojf_fix

no_players = int(input("Enter the number of players: "))
player_list = init_player_list(no_players)

def wait(p: Token, mode):
    if mode == 't':
        x = p.trade()
        if x == 'r':
            wait(p, 't')
    elif mode == 'h':
        x = p.handle_housing() 
        if x == 'r':
            wait(p, 'h')
    elif mode == '':
        a = input(f"{p.name}, end turn?(y/n)")
        if a == 'n':
            action = input("Choose action")
            wait(p, action)
            

double_counter = 0
def play_turn(p: Token):
    global double_counter # It will not access top level double_counter otherwise
    if p.bankrupt:
        player_list.remove(p)
        return
    g = input("Type `t` to Trade\nType `h` for House Management\nPress `Enter` to Roll Dice\n")
    if g == '':
        double = p.move(double_counter)
        if double:
            double_counter += 1 
            play_turn(p)
        wait(p, g)
    else:
        wait(p, g)
        play_turn(p)
        g = ''
        wait(p, g)
    double_counter = 0

def play_round():
    """The main game loop"""

    for p in player_list:
        print(f"\nIt is currently {p.name}'s turn.")
        if p.in_jail:
            print(f"{p.name} is currently in jail, pay 50 or roll a double")
            g = input("Type `t` to Trade\nType `h` for House Management")
            wait(p, g)
            if p.gojf:
                print("Enter `GOJF` to use get out of jail free card")
            x = input("1. Pay $50\n2. Roll a double\n--->>")

            if x == '1':
                print(f"{p.name} has paid $50 to leave jail")
                p.bal -= 50
                p.in_jail = False
                play_turn(p)

            elif x == '2':
                d1, d2 = p.diceroll()
                print(f"{p.name} rolled a {d1} and a {d2}")
                if d1 == d2:
                    print(f"{p.name} rolled a double and is free from jail!\n")
                    p.in_jail = False
                    play_turn(p)
                else:
                    print(f"Maybe next time")
            
            elif x.upper() == 'GOJF':
                print(f"{p.name} used their get out of jail free card!")
                play_turn(p)
                p.in_jail = False
                gojf_fix(p) # Fixes go jf

            else:
                print("Invalid option fuck nigga")

        else: play_turn(p)
    

# Actual Game start
while len(player_list) >= 2 and len(player_list) <= 4:
    i = input("Continue? ")

    if i == "n":
        break
    play_round()

if len(player_list) == 1:
    print(f"{player_list[0].name} is the winner!")

