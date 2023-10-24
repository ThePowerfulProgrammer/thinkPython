from intro4 import Card
import random


# Now that we have Cards, the next step is to define Decks. Since a deck is made up of 
# cards, it is natural for each Deck to contain a list of cards as an attribute

class Deck():
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
                
    def __str__(self) -> str:
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
        # Even though the result appears on 52 lines,
        # it is one long string that contains newlines.
        
        
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self,card):
        self.cards.append(card)
        
    # When we shuffle a deck, the cards are arranged in random order, assuming
    # the shuffler does not cheat, talking about you tairy
    def shuffle(self):
        random.shuffle(self.cards)
        
    # When we sort a deck we arrange it in some order typically highest to lowest
    # or lowest to highest
    def sort(self):
        return self.cards.sort()
        
    
        
    


if __name__ == "__main__":
        
    deck = Deck()

    print(deck)
    
