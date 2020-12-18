# 100-prisoners-
100 prisoners task from https://rosettacode.org/wiki/100_prisoners


# Rules/Constraints
100 prisoners are individually numbered 1 to 100
A room having a cupboard of 100 opaque drawers numbered 1 to 100, that cannot be seen from outside.
Cards numbered 1 to 100 are placed randomly, one to a drawer, and the drawers all closed; at the start.
Prisoners start outside the room
They can decide some strategy before any enter the room.
Prisoners enter the room one by one, can open a drawer, inspect the card number in the drawer, then close the drawer.
A prisoner can open no more than 50 drawers.
A prisoner tries to find his own number.
A prisoner finding his own number is then held apart from the others.
If all 100 prisoners find their own numbers then they will all be pardoned. If any don't then all sentences stand.

# Task
Simulate several thousand instances of the game where the prisoners randomly open drawers
Simulate several thousand instances of the game where the prisoners use the optimal strategy mentioned in the Wikipedia article, of:
First opening the drawer whose outside number is his prisoner number.
If the card within has his number then he succeeds otherwise he opens the drawer with the same number as that of the revealed card. (until he opens his maximum).