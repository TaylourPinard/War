from deck import Deck

# Create initial 52 card deck
game_deck = Deck()
game_deck.populate_standard_52()
game_deck.shuffle_deck()

# Setup player and computers decks
player_deck = Deck()
comp_deck = Deck()
player_deck.add_multiple_cards(game_deck.deal_multiple_cards(26))
comp_deck.add_multiple_cards(game_deck.deal_multiple_cards(26))

#Setup initial hands
player_hand = Deck()
player_hand.add_multiple_cards(player_deck.deal_multiple_cards(5))
comp_hand = Deck()
comp_hand.add_multiple_cards(comp_deck.deal_multiple_cards(5))