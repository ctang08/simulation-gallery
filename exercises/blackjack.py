'''
__str__ method was modified to output the card using unicode characters for the suits, and to display the rank of face cards and Aces as their first letter 
__eq__ method was implemented to allow for comparison of two Card instances based on their suit and rank
'''


"""Project 5 (Part 1): Blackjack

Author		Christopher Tang
Date		04/27/2026

This class represents a card in a standard deck of playing cards, which is used in the game of Blackjack. Each card has a suit and a rank, and the class provides methods to get the suit, rank, and value of the card.

AI Usage: 	AI wasn't used for this project.

Sources:    
https://en.wikipedia.org/wiki/Blackjack
https://www.digitalocean.com/community/tutorials/python-str-repr-functions
https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
"""

class Card:
    '''
    __init__
        Initializes a card with a suit and rank.

        Args:
            suit: A string representing the suit of the card (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades').
            rank: A string representing the rank of the card (e.g., '2', '3', ..., '10', 'Jack', 'Queen', 'King', 'Ace').
    '''
    def __init__(card, suit, rank):
        card.suit = suit
        card.rank = rank
    
    '''
    set_suit
        Sets the suit of the card.

        Args:
            card: An instance of the Card class.
            suit: A string representing the new suit of the card.
    '''
    def set_suit(card, suit):
        card.suit = suit
    
    '''
    set_rank
        Sets the rank of the card.

        Args:
            card: An instance of the Card class.
            rank: A string representing the new rank of the card.
    '''
    def set_rank(card, rank):
        card.rank = rank

    '''
    get_suit
        Returns the suit of the card.

        Args:
            card: An instance of the Card class.

        Returns: A string representing the suit of the card.
    '''
    def get_suit(card):
        return card.suit
    
    '''
    get_rank
        Returns the rank of the card.

        Args:
            card: An instance of the Card class.

        Returns: A string representing the rank of the card.
    '''
    def get_rank(card):
        return card.rank
    
    '''
    get_value
        Returns the value of the card in a Blackjack game. Number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces are worth 11.

        Args:
            card: An instance of the Card class.

        Returns: An integer representing the value of the card.
    '''
    def get_value(card):
        if card.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif card.rank == 'Ace':
            return 11
        else:
            return int(card.rank)

    '''
    __str__
        Returns a string representation of the card.

        Args:
            card: An instance of the Card class.

        Returns: A string representing the card.
    '''
    def __str__(card):
        if card.rank in ['Jack', 'Queen', 'King', 'Ace']:
            rank = card.rank[0]
        else:
            rank = card.rank
        if card.suit == 'Spades':
            suit = "\u2660"
        elif card.suit == 'Hearts':
            suit = "\u2665"
        elif card.suit == 'Clubs':
            suit = "\u2663"
        elif card.suit == 'Diamonds':
            suit = "\u2666"
        return f"{rank}{suit}"

    '''
    __eq__
        Compares two Card instances for equality based on their suit and rank.

        Args:
            value: An object to compare with the current Card instance.
        
        Returns: True if the value is a Card instance with the same suit and rank, False otherwise.
    '''
    def __eq__(self, value):
        if isinstance(value, Card):
            return self.suit == value.suit and self.rank == value.rank
        return False
    