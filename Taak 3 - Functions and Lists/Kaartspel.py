import random

def kaartspel(seed):
    random.seed(seed)
    deck = []
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10","Jack", "Queen", "King",]
    for suit in suits:
        for value in values:
            deck.append(f"{value} of {suit}")
    card_numbers = list(range(1, 53))
    random.shuffle(card_numbers)
    for i in range(4):
        print(f"Card number {card_numbers[i]-1} is {deck[card_numbers[i]-1]}")