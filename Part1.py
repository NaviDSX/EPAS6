#### 1. Write a single expression that includes lambda, zip, and map functions to select create 52 cards in a deck - 50 pts

vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

deck = set(map(lambda x: (x[0], x[1]), zip(suits*13, vals*4)))



# #### 2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pt

def create_deck(vals: 'List of Values',
                suits: 'List of Suits') -> 'Set of Deck':
    '''
    A function which creates a deck of playing cards.
    
    Inputs:
    vals: The values of cards of each suit.
    suits: The different suits of cards.

    Output:
    deck: Set of Cards.
    '''
    deck = set()
    for suit in suits:
        for val in vals:
            deck.add((suit, val))
    return deck
