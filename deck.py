from card import Card
import random


'''Standard 52 card playing deck generated during __init__ method,
    as well as some funtions for using the deck in a game'''
class Deck_Standard_52:
    def __init__(self):
        self.cards = []
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

    def __str__(self):
        "\n".join([str(card.__str__()) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    def deal_card(self):
        self.cards.pop()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def show_cards(self):
        for card in self.cards:
            print(str(f"{card.face} of {card.suit}"))
