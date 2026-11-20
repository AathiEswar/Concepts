from random import shuffle

suit = ("Hearts","Diamonds","Spade","Clover")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():
    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.suit + " of " + self.rank

class Deck():
    def __init__(self):
        self.deck = []

        for suits in suit:
            for rank in ranks:
                created_card = Card(suits,rank)

                self.deck.append(created_card)

    def shuffle(self):
        shuffle(self.deck)
                
    def deal_one(self):
        return self.deck.pop()


class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.append(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)

        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards "


player1 = Player("Player 1")
player2 = Player("Player 2")


new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

game_on = True
round_count = 0

while game_on:
    round_count += 1
    print(f"ROUND {round_count}!!")

    if len(player1.all_cards) == 0:
        print("PLAYER 1 HAS LOST!  PLAYER 2 WON!")
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print("PLAYER 2 HAS LOST!  PLAYER 1 WON!")
        game_on = False
        break

    player1_cards = []
    player1_cards.append(player1.remove_one())

    player2_cards = []
    player2_cards.append(player2.remove_one())

at_war = True

while at_war:
    if player1_cards[-1].value > player2_cards[-1].value:

        player1.add_cards(player1_cards)
        player1.add_cards(player2_cards)

        at_war= False

    elif player2_cards[-1].value > player1_cards[-1].value:

        player2.add_cards(player2_cards)
        player2.add_cards(player1_cards)
        at_war = False
    else:
        print("War!!")

        if len(player1.all_cards) < 3:
            print("Not Enough Cards for Player1")
            print("PLAYER2 WON!!")
            game_on = False
            break

        elif len(player2.all_cards) < 3:
            print("Not Enough Cards for Player2")
            print("PLAYER1 WON!!")
            game_on = False
            break


        else:
            for num in range(3):

                player1_cards.append(player1.remove_one())
                player2_cards.append(player2.remove_one())
















    








