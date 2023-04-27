class Card:

    def __init__(self, face, suit, value):
        self.face = face
        self.suit = suit
        self.value = value
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self._cards):
            self.index = -1
            raise StopIteration
        else:
            return self._cards

    def __repr__(self):
        return f"{self.face} of {self.suit}"

    def __str__(self):
        return f"{self.face} of {self.suit}"

    def get_face(self):
        return self.face

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
    
