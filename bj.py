import random


class Player:

    def __init__(self):
        self.bank_amt = 25
        self.hand = []
        self.bet = None

    def bank(self, win):
        pass

    def hand(self):
        pass

    def bet(self):
        pass


class Dealer:

    def hand(self):
        pass


class Deck:

    def __init__(self):
        self.deck_size = 52
        self.suits = ['club', 'diamond', 'heart', 'spade']
        self.symbols = ['♠', '♥', '♦', '♣']
        self.cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                      'Q': 10, 'K': 10}
        self.shuffled_deck = []

    def shuffle(self):
        self.shuffled_deck = []
        for suites in self.suits:
            for cards in self.cards:
                self.shuffled_deck.append([suites, cards])
        random.shuffle(self.shuffled_deck)

    def deal(self):
        pass


class Table:

    def __init__(self):
        self.slots = 5
        self.pieces = ['_', '|']


number = None
suit = None


def update_draw(hand):
    global number
    global suit

    if hand is None:
        return
    else:
        print(len(hand))
        for n in hand:
            if n == 'heart':
                suit = '♥'
            elif n == 'club':
                suit = '♣'
            elif n == 'diamond':
                suit = '♦'
            elif n == 'spade':
                suit = '♠'

            # card = [f'|{number}  |', f'| {suit} |', f'|__{number}|']
