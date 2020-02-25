import random


class Player:

    def __init__(self):
        self.bank_amt = 25
        self.hand = []
        self.bet = None

    def bank(self, win):
        pass

    def hit(self, deck):
        self.hand.append(deck.deal())

    def bet(self):
        pass


class Dealer:

    def __init__(self):
        self.hand = []

    def hit(self, deck):
        self.hand.append(deck.deal())


class Deck:

    def __init__(self):
        self.deck_size = 52
        self.suits = ['♠', '♥', '♦', '♣']
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
        card = self.shuffled_deck[-1]
        self.shuffled_deck.pop()
        return card
