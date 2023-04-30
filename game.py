from deck import Deck

def rules():
    print('''This is a updated version of the childhood game of War
    to play all you have to do is choose which card from your hand to play
    if your card is bigger than the computers card you win and vice versa
    The winner gets to add both cards to their victory pile
    when you or the computer run out of cards in your deck and your hand
    your victory pile will be shuffled and that becomes your new deck
    if you collect all 52 cards you win! If the computer does that
    then the computer wins. Type 'Quit' to end the game
    Good luck! You can see these rules again at any time by typing in 'rules'
    ''')

# Create initial 52 card deck
game_deck = Deck()
game_deck.populate_standard_52()
game_deck.shuffle_deck()

# Setup player and computers decks
player_deck = Deck()
comp_deck = Deck()
player_deck.add_multiple_cards(game_deck.deal_multiple_cards(26))
comp_deck.add_multiple_cards(game_deck.deal_multiple_cards(26))

# Setup initial hands
player_hand = Deck()
player_hand.add_multiple_cards(player_deck.deal_multiple_cards(5))
comp_hand = Deck()
comp_hand.add_multiple_cards(comp_deck.deal_multiple_cards(5))

# rules explanation
rules()
# game logic
def play_game(player_hand, comp_hand):
    playing = True
    player_victory_pile = []
    comp_victory_pile = []
    while playing:
        if len(player_hand) == 0:
            if len(player_deck.cards) == 0:
                print("Computer wins!")
                playing = False
            player_deck.add_multiple_cards(player_victory_pile)
            player_deck.shuffle_deck()
        if len(player_hand) == 4 and len(player_deck.cards) != 0:
            player_hand.add_card(player_deck.deal_card())
        print("You have: ") 
        player_hand.show_cards()
        print("Choose a card by typing in the number or first letter of the card if face card")
        player_choice = input()
        if player_choice == "rules":
            rules()
        if player_choice == "quit":
            playing = False
        elif player_choice.isdigit():
            play = int(player_choice)
        elif player_choice.lower == "k":
            play = player_hand.pop("king")
        elif player_choice.lower == "q":
            play = player_hand.pop("queen")
        elif player_choice.lower == "j":
            play = player_hand.pop("jack")
        elif player_choice == "a":
            play = player_hand.pop("ace")
        else:
            print("please choose only a card in your hand")