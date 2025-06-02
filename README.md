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
- Handling house

2. **`game.py`**

Contains the main game loop. It controls the order of events for each player on their turn, also controls jail related actions.
It is also where the trading/add house mechanism works. Soon to have functions for mortgaging in foreseeable future.

3. **`squares .py`**

It is the registry for all the properties and contains all the data regarding the property which include:
- Location of each space
- If purchased or not
- The Price & Mortgage value of the property
- The current rent of the property if a player which is not the owner were to land on the property
- What colour set it belongs to
- Index arrays which are the keys to access all abilities of each individual space
- Map Legend indicated the type of each property for board to classify what the player can do on current space.
    
## Additional Information

Project is still in testing stage and does  have all above features implemented to completion as of now. Updates will be made once they are added to the source code and a part of the game. 

Two major aspect left is auctioning and mortgaging properties.

## Current Stage 

Currently on Testing Stage, the game is almost production ready. What remains is few rounds of experimental testing before release

## Future Expansions

Converting this entire project into gamescript files in C#, making a 3D UI in Unity for visualization. Core concepts will remain same and use concepts already implemented just translated and able to be viewed as a proper game with functional GUI.