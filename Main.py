import random

# Amount of cards/prisoners.
AMOUNT_TO_FIND = 1000
AMOUNT_OF_TRIES = 500
AMOUNT_OF_ITERATIONS = 100


class Prisoner:
    def __init__(self, number, found_card):
        self.number = number
        self.found_card = found_card


class Card:
    def __init__(self, number):
        self.number = number


def no_strategy():
    for prisoner in prisoners:
        i = 0
        while i < AMOUNT_OF_TRIES:
            if prisoner.number == cards[i].number:
                prisoner.found_card = True
                break
            else:
                i += 1


def optimized_strategy():
    for prisoner in prisoners:
        i = 0
        to_check = cards[prisoner.number - 1].number
        while i < AMOUNT_OF_TRIES:
            if to_check == prisoner.number:
                prisoner.found_card = True
                break
            else:
                to_check = cards[to_check - 1].number
                i += 1

    return prisoners


wins = 0
losses = 0

for x in range(AMOUNT_OF_ITERATIONS):
    prisoners = [Prisoner(i, False) for i in range(AMOUNT_TO_FIND)]
    cards = [Card(i) for i in range(AMOUNT_TO_FIND)]
    random.shuffle(cards)

    success = 0
    fail = 0

    optimized_strategy()
    # no_strategy()

    for prisoner in prisoners:
        if prisoner.found_card == True:
            success += 1
        else:
            fail += 1

    if success == AMOUNT_TO_FIND:
        wins += 1
    else:
        losses += 1
    print(f"Iteration: {x}", flush=True)

print(f"Wins: {wins}")
print(f"Fails: {losses}")
