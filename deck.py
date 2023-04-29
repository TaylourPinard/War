from card import Card
import random


'''Standard 52 card playing deck generated during __init__ method,
    as well as some funtions for using the deck in a game'''
class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        "\n".join([str(card.__str__()) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    def add_multiple_cards(self, cards):
        for card in cards:
            self.add_card(card)

    def deal_card(self):
        return self.cards.pop()

    # Not sure if this is working yet the way I intended
    # More testing to make sure its playing nicely with
    # add_multiple_cards function
    def deal_multiple_cards(self, num_cards_dealt):
        new = []
        for i in range(num_cards_dealt):
            new.append(self.deal_card())
        return new
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def show_cards(self):
        for card in self.cards:
            print(str(f"{card.face} of {card.suit}"))

    def populate_standard_52(self):
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        faces = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King"]
        for suit in suits:
            for face in faces:
                try:
                    if str(face).isdigit():
                        value = int(face)
                        face = str(value)
                    elif face == "Ace":
                        value = 1
                    elif face in ["Jack", "Queen", "King"]:
                        value = 10
                    else:
                        raise ValueError(f"Invalid face card: {face}")
                except ValueError as e:
                    print(e)
                else:
                    card = Card(face, suit, value)
                    self.add_card(card)
                    
# For Debugging will remove
deck = Deck()
deck.populate_standard_52()
deck.shuffle_deck()
new = Deck()
new.add_multiple_cards(deck.deal_multiple_cards(26))
new.show_cards()