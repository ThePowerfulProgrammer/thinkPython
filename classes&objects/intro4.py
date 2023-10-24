class Card():
    # Defined outside any function, means it is accessible my all class instances
    # Shared among all instances of the class and are accessed using the class name rather than instance references
    # Called class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=2):
        # WE assign if default values are overidden
        # instance attributes
        self.suit = suit
        self.rank = rank
        
    def __str__(self) -> str:
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"
    
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __le__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 <= t2

    def __eq__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 == t2

    def __ne__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 != t2

    def __gt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 > t2

    def __ge__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 >= t2

    
if __name__ == "__main__":
    
    queen_of_diamonds = Card(1, 12)

    print(queen_of_diamonds)
    
    king_of_diamonds = Card(1,13)
    
    print(queen_of_diamonds <= king_of_diamonds)