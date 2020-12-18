from Prisoner import Prisoner
from Card import Card 
import random

#Amount of cards/prisoners.
AMOUNT_TO_FIND = 100
AMOUNT_OF_TRIES =  50

#Creates list of prisoner object
prisoners = [Prisoner(i, False) for i in range(AMOUNT_TO_FIND)]

def no_strategy():
    #creates list of card object
    cards = [Card(i) for i in range(AMOUNT_TO_FIND)]
    random.shuffle(cards)
    for prisoner in prisoners:
        #print(f"prisoner number: {prisoner.number}")
        #amount of tries for the prisoner
        i = 0
        #ensure each iteration starts with False
        prisoner.found_card = False
        while prisoner.found_card == False:
            for card in cards:
                if i == AMOUNT_OF_TRIES:
                    break
                
                elif prisoner.number == card.number:
                    cards.remove(card)
                    prisoner.found_card = True
                
                else: 
                    i += 1
                
                if prisoner.found_card == True:
                continue
            break
        if len(prisoners) == 0:
            return cards
    return cards
               
for x in range(1000):
    result = no_strategy()
    
    if len(result) == 0:
        print("success")
    else:
        print("fail")
        




        