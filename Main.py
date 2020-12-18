from Prisoner import Prisoner
from Card import Card 
import random

#Amount of cards/prisoners.
AMOUNT_TO_FIND = 100
AMOUNT_OF_TRIES = 50

#Creates list of prisoner object
prisoners = [Prisoner(i, False) for i in range(AMOUNT_TO_FIND)]

def no_strategy():
    #creates list of card object
    cards = [Card(i) for i in range(AMOUNT_TO_FIND)]
    random.shuffle(cards)
    for prisoner in prisoners:
        #amount of tries for the prisoner
        i = 0
        #ensure each iteration starts with False
        prisoner.found_card = False
        #TODO Figure out a different way besides while.
        #TODO Check breaks, figure out a better logical system.
        #TODO Remove found_card system.
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

def optimized_strategy():
    #Create list of cards
    cards = [Card(i) for i in range(AMOUNT_TO_FIND)]
    random.shuffle(cards)
    j = 0

    for prisoner in prisoners:
        i = 0
        #TODO Something in here is broke 
        new_number = cards[prisoner.number].number
        #TODO Look into why this works....
        while not (prisoner.number == new_number or i > AMOUNT_OF_TRIES):
            temp_new_number = cards[new_number].number
            new_number = temp_new_number
            i += 1
        if prisoner.number == new_number:
            j += 1
    return j

success = 0
fail = 0               
for x in range(1000):
    result = optimized_strategy()
    if result == AMOUNT_TO_FIND:
        success += 1
    else:
        fail += 1

print(f"success : {success}")
print(f"fail: {fail}")