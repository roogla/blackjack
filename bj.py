import random
import os


class Player:

    def __init__(self):
        self.bank = 25
        self.hand = []
        self.bet = None

    def hit(self, deck):
        self.hand.append(deck.deal())


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


def win(hand):
    for cards in hand:
        print(f'{cards} debug')


def table(state, player, dealer, deck):
    if state == 1:
        Player.bet = int(input('enter a bet amount\n>>>'))

    elif state == 2:

        win(player.hand)

        player_choice = input('hit or stand?:\n>>>')

        if player_choice == 'hit':
            player.hit(deck)
        elif player_choice == 'stand':
            win(player.hand)

    elif state == 3:
        # begin dealer logic
        print('ass')
    print(''.join(str(c) for c in dealer.hand))
    print(''.join(str(c) for c in player.hand))


d = Deck()
r = Player()
a = Dealer()
d.shuffle()


