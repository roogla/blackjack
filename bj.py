import random
import os


class Player:

    def __init__(self):
        self.bank = 25
        self.hand = []
        self.bet = None
        self.total = 0

    def hit(self, deck):
        self.hand.append(deck.deal())


class Dealer:

    def __init__(self):
        self.hand = []
        self.total = 0

    def hit(self, deck):
        self.hand.append(deck.deal())


class Deck:

    def __init__(self):
        self.deck_size = 52
        self.suits = ['♠', '♥', '♦', '♣']
        self.cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
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


def busted(hand):
    faces = 'JQK'
    total = 0
    ace = False
    ace_count = 0
    for cards in hand:
        if cards[1] in faces:
            total += 10
        elif cards[1] == 'A':
            ace = True
            ace_count += 1
            total += 11
        else:
            total += int(cards[1])
    print(total)
    if total > 21 and ace:
        for n in range(ace_count):
            total -= 10
        return [False, total]
    elif total > 21:
        return [True, total]
    else:
        return [False, total]


def table(state, player, dealer, deck):
    if len(deck.shuffled_deck) < 7:
        deck.shuffle()

    def draw_t():
        os.system('cls')
        print('Dealer: ' + ''.join(str(c) for c in dealer.hand))
        print('Player: ' + ''.join(str(c) for c in player.hand))
        print(f'P: {player.total} || D: {dealer.total}')
        print(f'Bank: {player.bank}')

    '''
    initial state for game table
    clears player and dealer hand
    deals two cards to dealer and player
    runs 'busted' to set player/dealer totals
    '''
    if state == 1:
        player.bet = int(input('enter a bet amount\n>>>'))
        player.bank -= player.bet
        player.hand = []
        dealer.hand = []
        for hits in range(2):
            player.hit(deck)
            dealer.hit(deck)
        player.total = busted(player.hand)[1]
        dealer.total = busted(dealer.hand)[1]
        draw_t()
        table(2, player, dealer, deck)

    # player state --> hitting and standing, checking for bust
    elif state == 2:
        print(25*'*'+'\n'+'1: hit | 2: stand | 3: exit'+'\n'+25*'*')

        player_choice = input('hit or stand?:\n>>>')

        if player_choice[0] == 'h' or player_choice[0] == '1':
            player.hit(deck)
            bust = busted(player.hand)
            player.total = bust[1]

            if bust[0]:
                draw_t()
                print('you lost fool')
                table(1, player, dealer, deck)
            elif not bust[0]:
                draw_t()
                table(2, player, dealer, deck)

        elif player_choice[0] == 's' or player_choice[0] == '2':
            draw_t()
            bust = busted(player.hand)
            player.total = bust[1]
            table(3, player, dealer, deck)

        elif player_choice[0] == '3' or player_choice[0] == 'q':
            quit()
        else:
            print("Sorry, please select h for hit or s for stand")
            table(2, player, dealer, deck)

    elif state == 3:
        # begin dealer logic
        bust = busted(dealer.hand)
        dealer.total = bust[1]

        if bust[0]:
            player.bank += 2 * player.bet
            draw_t()
            print('You won')
            table(1, player, dealer, deck)

        elif not bust[0]:

            if bust[1] < 17:
                dealer.hit(deck)
                table(3, player, dealer, deck)

            else:

                if dealer.total < player.total:
                    player.bank += 2 * player.bet
                    draw_t()
                    print("winner, winnner, chicken dinner")
                    table(1, player, dealer, deck)

                elif dealer.total == player.total:
                    player.bank += player.bet
                    draw_t()
                    print("push! push it real good")
                    table(1, player, dealer, deck)

                else:
                    draw_t()
                    print("you lose")
                    table(1, player, dealer, deck)


if __name__ == '__main__':
    d = Deck()
    r = Player()
    a = Dealer()
    d.shuffle()
    table(1, r, a, d)
