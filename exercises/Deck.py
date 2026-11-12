'''
Added shuffle and reset methods

Project 6: Blackjack pt2

Author		Christopher Tang
Date		05/04/2026

This class represents a deck of cards used in the game of Blackjack. It initializes a standard deck of 52 playing cards, provides a method to shuffle the deck, and a method to deal a card from the deck.

AI Usage: 	AI wasn't used for this project.

Sources: 
https://en.wikipedia.org/wiki/Standard_52-card_deck#New-deck_order_%28NDO%29
'''

import random
from blackjack import Card

class Deck:
    '''
    __init__
        Initializes a standard deck of 52 playing cards.

        Args: None
    '''
    def __init__(self):
        self.cards = []
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    '''
    deal_card
        Removes and returns the top card from the deck.

        Args: None

        Returns: The card that was dealt from the deck.
    '''
    def deal_card(self):
        return self.cards.pop()
    
    '''
    shuffle
        Shuffles the cards in the deck.

        Args: None
    '''
    def shuffle(self):
        random.shuffle(self.cards)

    '''
    reset
        Resets the deck to its original state with all 52 cards.

        Args: None
    '''
    def reset(self):
        self.cards = []
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    '''
    __str__
        Returns a string representation of the deck.

        Args: None

        Returns: A string containing all the cards in the deck.
    '''
    def __str__(self):
        str = ''
        for card in self.cards:
            str += f'{card}\n'
        return str

    '''
    __eq__
        Compares two decks for equality.

        Args:
            other (Deck): The other deck to compare with.

        Returns:
            bool: True if the decks are equal, False otherwise.
    '''
    def __eq__(self, other):
        return self.cards == other.cards
