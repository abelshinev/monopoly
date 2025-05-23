class Square:
    
    def __init__(self, name: str, pos: int):
        self.name = name
        self.pos = pos

class Property(Square):

    house_ct = 0
    is_owned = False
    
    def __init__(self, name, pos, price: int, color: str):
        super().__init__(name, pos)
        self.price = price
        self.color = color


class Station(Square):

    price = 200
    is_owned = False

    def __init__(self, name, pos):
        super().__init__(name, pos)

class Utility(Square):

    price = 150
    is_owned = False
    multi = 4

    def __init__(self, name, pos):
        super().__init__(name, pos)
    
    def has_alt(self):
        self.multi = 10
    
    

class Cards(Square):

    def __init__(self, name, pos):
        super().__init__(name, pos)

""" PROPERTY OBJECTS """

old_kent = Property('Old Kent Road', 1, 60, "brown")
whitechapel = Property('Whitechapel Road', 3, 60, "brown")
kings_cross = Station('Kings Cross Station', 5)
angel_isl = Property('The Angel Islington', 6, 100, "aqua")
euston_road = Property('Euston Road', 8, 100, "aqua")
pentonville = Property('Pentonville Road', 9, 120, "aqua")
pall_mall = Property('Pall Mall', 11, 140, "pink")
electric_co = Utility('Electric Company', 12)
whitehall = Property('Whitehall', 13, 140, "pink")
northumber = Property('Northumberland Avenue', 14, 160, "pink")
marylebone = Station('Marylebone Station', 15)
bow_street = Property('Bow Street', 16, 180, "orange")
marlborough = Property('Marlborough Street', 18, 180, "orange")
vine_str = Property('Vine Street', 19, 200, "orange")
strand = Property('The Strand', 21, 220, "red")
fleet_str = Property('Fleet Street', 23, 220, "red")
trafalgar = Property('Trafalgar Square', 24, 240, "red")
fenchurch = Station('Fenchurch Station', 25)
leicester = Property('Leicester Square',26, 260, "yellow")
coventry = Property('Coventry Street', 27, 260, "yellow")
water_works = Utility('Water Works', 28)
piccadilly = Property('Piccadilly', 29, 280, "yellow")
regent_str = Property('Regent Street', 31, 300, "green")
oxford_str = Property('Oxford Street', 32, 300, "green")
bond_str = Property('Bond Street', 34, 320, "green")
liverpool = Station('Liverpool Station', 35)
park_lane = Property('Park Lane', 37, 350, "blue")
mayfair = Property('Mayfair', 39, 400, "blue")


# List of all places for to be accessed in dictionary
board_lay = [
    old_kent, whitechapel, kings_cross, angel_isl, euston_road, pentonville,
    pall_mall, electric_co, whitehall, northumber, marylebone, bow_street, marlborough, vine_str,
    strand, fleet_str, trafalgar, fenchurch, leicester, coventry, water_works, piccadilly,
    regent_str, oxford_str, bond_str, liverpool, park_lane, mayfair
]
"""List with board Layout"""

color_index = {
    "brown": [1, 3], "aqua": [6, 8, 9],
    "pink": [11, 13, 14], "orange": [16, 18, 19],
    "red": [21, 23, 24], "yellow": [26, 27, 29],
    "green": [31, 32, 34], "blue": [37, 39]
}
"""
Index of all the properties in one colour group

    - Key: colour string
    - Val: location array
"""

property_map = dict()
"""
Dictionary of all property on the board

    - Key : position
    - Value : space object
"""

for place in board_lay:
    property_map[place.pos] = place # Key is position, value is the object
    
tax_map = {
    4 : ["Income Tax", 200],
    38 : ["Luxury Tax", 100]
}

null_map = {
    10: "is just visiting jail",
    20: "is on free parking",
    40: "is on go"
}

wild_card_map = {}

map_legend = {
    1: "p", 2: "cc", 3: "p", 4: "t", 5: "s", 6: "p", 7: "c", 8: "p", 9: "p", 10: "n",
    11: "p", 12: "u", 13: "p", 14: "p", 15: "s", 16: "p", 17: "cc", 18: "p", 19: "p", 20: "n",
    21: "p", 22: "c", 23: "p", 24: "p", 25: "s", 26: "p", 27: "p", 28: "u", 29: "p", 30: "j",
    31: "p", 32: "p", 33: "cc", 34: "p", 35: "s", 36: "c", 37: "p", 38: "t", 39: "p", 40: 'n'
}
"""
Map Legend maps every square to space type
    - Key: position
    - Value: type of square
"""
