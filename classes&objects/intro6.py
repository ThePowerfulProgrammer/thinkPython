from intro5 import Deck

class Hand(Deck):
    # Represents a hand of playing cards
    
    # If we provide dunder methods here, it overrides the parent dunder methods, why would we want to do this?
    # Maybe the parent init method does not do what we want it to do OR maybe we want to add functionality 
    
    def __init__(self, label=""):
        self.cards = []
        self.label = label
        
    # def __str__(self):
    #     cardStrings = [str(card) for card in self.cards]
    #     return f"{self.label}:{cardStrings}"
     
    
    def move_cards(self,hand,num):
        '''
            Remove num cards from self and add them to hand.
        '''
        for i in range(num):
            hand.add_card(self.pop_card())
        
        
if __name__ == "__main__":
    hand = Hand('new hand')
    print(hand.cards)
    print(hand.label)
    
    deck = Deck() # Create a deck
    card = deck.pop_card() # Pop a card
    hand.add_card(card) # add card to empty hand
    print(hand.cards) # Duh
    
    # Pop i cards from deck and add them to hand
    for i in range(5):
        card = deck.pop_card()
        hand.add_card(card)
    
    print(hand) # Duh
    
     
    oppenentHand = Hand('opp') # Create an empty hand for opponent
    hand.move_cards(oppenentHand,2) # Eliminate cards from hand and add to oppenent hand
    print(oppenentHand) # DUH
    