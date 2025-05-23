from player import init_player_list, Token

no_players = int(input("Enter the number of players: "))
player_list = init_player_list(no_players)

def play_turn(p: Token):
    input("Press `Enter` to roll dice\n")
    p.move()
def play_round():
    for p in player_list:
        print(f"\nIt is currently {p.name}'s turn.")
        if p.in_jail:
            print(f"{p.name} is currently in jail, pay 50 or roll a double")
            x = int(input("1. Pay $50\n2. Roll a double\n--->>"))
            if x == 1:
                print(f"{p.name} has paid $50 to leave jail")
                p.bal -= 50
                p.in_jail = False
                play_turn(p)
            elif x == 2:
                d1, d2 = p.diceroll()
                print(f"{p.name} rolled a {d1} and a {d2}")
                if d1 == d2:
                    print(f"{p.name} rolled a double and is free from jail!\n")
                    p.in_jail = False
                    play_turn(p)
                else:
                    print(f"Maybe next time")
            else:
                print("Invalid option fuck nigga")

        else: play_turn(p)

    

# Actual Game start
while len(player_list) >= 2:
    i = input("Continue? ")
    if i == "n":
        break
    play_round()

# github commit test
