from Prisoner import Prisoner
from Card import Card 

#Amount of cards/prisoners.
AMOUNT_TO_FIND = 100

#Creates list of prisoner object
prisoners = [Prisoner(i) for i in range(AMOUNT_TO_FIND)]
#creates list of card object
cards = [Card(i) for i in range(AMOUNT_TO_FIND)]
copy_of_cards = cards.copy()

for prisoner in prisoners