from Prisoner import Prisoner
from Card import Card 
import random

#Amount of cards/prisoners.
AMOUNT_TO_FIND = 10
AMOUNT_OF_TRIES = 5

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
   
    for prisoner in prisoners:
        i = 0
        if prisoner.number == cards[prisoner.number].number:
            print(f"number found. prisoner = {prisoner.number} amount of tries = {i}")
            break
        #TODO Something in here is broke 
        else:
            new_number = cards[prisoner.number].number
            while prisoner.number != new_number or i < AMOUNT_OF_TRIES:
                print(f"number not found. prisoner = {prisoner.number} card = {new_number} amount of tries = {i}")
                temp_new_number = cards[new_number].number
                new_number = temp_new_number
                i += 1
            break
    return cards
               
for x in range(1000):
    result = optimized_strategy()
    
    if len(result) == 0:
        print("success")
    else:
        print("fail")     