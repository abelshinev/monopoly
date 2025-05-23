# Monopoly

A pet project of monopoly recreated in python. Contains no GUI
- Has multiple player accessibility
- Turn based 
- Random dice mechanism with doubles giving an additional turn included

# Modules

Modules include: 

1. **`player.py`**
 
Controls the player mechanism and turns. The dice mechanism is included along with the movements that the player moves where it accesses properties and places on the board. 

It is the brain of the system governing aspects of the game like 
- Landing on board spaces
- Purchasing properties 
- Trading
- Paying rent

2. **`game.py`**

Contains the main game loop. It controls the order of events for each player on their turn, also controls jail related actions.

3. **`squares .py`**

It is the registry for all the properties and contains all the data regarding the property which include:
- Location of each space
- If purchased or not
- The Price & Mortgage value of the property
- The current rent of the property if a player which is not the owner were to land on the property
- What colour set it belongs to
- Index arrays which are the keys to access all abilities of each individual space
    
## Additional Information

Project is still in development stage and does not have all above features implemented to completion as of now. Updates will be made once they are added to the 
source code and a part of the game. 

## Current Stage 

Currently working on Trading mechanism, players can access other players inventories and request trades

Next steps will be to work on the house and hotel management. The groundwork for which has been done with the introduction of color sets in the latest commit.