class Spaces:
    def rent():
        pass

class Station(Spaces): # Station Objects
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        
class Property(): # Property Objects
    def __init__(self, name, pos, cost, house_no, purchased):
        self.name = name
        self.pos = pos
        self.cost = cost
        self.house_no = house_no
        self.purchased = purchased

    def do_sumn(self):
        print(self.name)


# Every space
old_kent = Property('Old Kent Road', 1, 60, 0, False)
whitechapel = Property('Whitechapel Road', 3, 60, 0, False)
kings_cross = Station('Kings Cross Station', 5)
angel_isl = Property('The Angel Islington', 6, 100, 0, False)
euston_road = Property('Euston Road', 8, 100, 0, False)
pentonville = Property('Pentonville Road', 9, 120, 0, False)
pall_mall = Property('Pall Mall', 11, 140, 0, False)
whitehall = Property('Whitehall', 13, 140, 0, False)
northumber = Property('Northumberland Avenue', 14, 160, 0, False)
marylebone = Station('Marylebone Station', 15)
bow_street = Property('Bow Street', 16, 180, 0, False)
marlborough = Property('Marlborough Street', 18, 180, 0, False)
vine_str = Property('Vine Street', 19, 200, 0, False)
strand = Property('The Strand', 21, 220, 0, False)
fleet_str = Property('Fleet Street', 23, 220, 0, False)
trafalgar = Property('Trafalgar Square', 24, 240, 0, False)
fenchurch = Station('Fenchurch Station', 25)
leicester = Property('Leicester Square',26, 260, 0, False)
coventry = Property('Coventry Street', 27, 260, 0, False)
piccadilly = Property('Piccadilly', 29, 280, 0, False)
regent_str = Property('Regent Street', 31, 300, 0, False)
oxford_str = Property('Oxford Street', 32, 300, 0, False)
bond_str = Property('Bond Street', 34, 320, 0, False)
liverpool = Station('Liverpool Station', 35)
park_lane = Property('Park Lane', 37, 350, 0, False)
mayfair = Property('Mayfair', 39, 400, 0, False)




board_lay = [           # List of all places for to be accessed in dictionary
    old_kent, whitechapel, kings_cross, angel_isl, euston_road, pentonville,
    pall_mall, whitehall, northumber, marylebone, bow_street, marlborough, vine_str,
    strand, fleet_str, trafalgar, fenchurch, leicester, coventry, piccadilly,
    regent_str, oxford_str, bond_str, liverpool, park_lane, mayfair
]

# Dictionary of all spaces on the board
Prop_dict = {} 

for place in board_lay:
    Prop_dict[place.pos] = place.name # Key is position, value is the namey
    