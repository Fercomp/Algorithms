class Card:
    def __init__(self, value, suit):
        self.value = value # 1 <= value <= 13
        self.suit = suit # clubs, hearts, spades, diamonds

deck = [Card(8, "hearts"), Card(8, "clubs"), Card(3, "clubs"), Card(3, "hearts")]

def sort_by_field(deck):
    suit_to_precedence = {"clubs": 1, "hearts": 2, "spades": 3, "diamonds": 4}
    # Use tuples when we have different precedence levels. The first element is considered first.
    return sorted(deck, key=lambda x: (x.value, suit_to_precedence[x.suit]))