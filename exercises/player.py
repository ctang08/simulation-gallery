'''
Project 6: Blackjack Part 3

Author      Tony Song, Christopher Tang                             
Date        05/14/2026

This program creates a player class of the blackjack game. Each player has a name,
amount of money, bet amount, and a hand. There are methods to obtain the card,
check the value of the hand, and determine if the player has blackjack or has busted.
There are also examples in the main method to test the class.

AI Usage: None

Sources:
'''

import random
from Deck import Deck
from blackjack import Card

class Player:
    def __init__(self, name, startingMoney):
        '''
        Initializes a player and their name, money, and hand of cards.
        '''
        self.hand = []
        self.name = name
        self.money = startingMoney
        self.bet = 0
    
    def obtain_card(self, card):
        '''
        Adds a card to the player's hand.

        Args:
            card: The card to be added to the player's hand.
        '''
        self.hand.append(card)    
    
    def is_blackjack_bust(self):
        '''
        Checks if the player has a blackjack.

        Returns: An integer that's 0 if the player is alive, 
        1 if the player has a blackjack, and 2 if the player busted.
        '''
        total_value = self.check_value()
        if total_value > 21:
            return 2
        elif total_value == 21:
            return 1
        else:
            return 0
        
    def check_value(self):
        '''
        Calculates the total value of the player's hand.

        Returns: The total value of the player's hand.
        '''
        sum_of_cards = 0
        for card in self.hand:
            sum_of_cards += card.value
            
        while sum_of_cards > 21:
            for card in self.hand:
                if card.rank == "Ace" and card.value == 11:
                    card.changeAce("down")
                    sum_of_cards -= 10
                    break
            return sum_of_cards
    
        return sum_of_cards 
        
    def place_bet(self, bet):
        '''
        Places a bet for the player.

        Args:
            bet: The amount of money the player wants to bet.
        '''
        if bet > self.money:
            print("Not enough money")
        else:
            self.bet = bet
    
    def __str__(self):
        '''
        Returns a string representation of the player.

        Returns: A string containing the player's name, money, hand, and current bet.
        '''
        str1 = "Name: " + self.name + "\nMoney: " + str(self.money) + "\nCurrent Bet: " + str(self.bet) + "\nHand: "
        for card in self.hand:
            str1 += f'{card} '
        return str1

def main():
    """
    Main function to run example code for the Player class. 
    """
    # Examples to test the Player class
    player1 = Player("Tony", 100)
    print(player1) # testing __str__
    card1 = Card("Ace", "Spades")
    card2 = Card("10", "Hearts")
    player1.obtain_card(card1)
    player1.obtain_card(card2)
    print(player1) # testing obtain_card and __str__
    print(player1.check_value()) # testing check_value (should be 21)
    print(player1.is_blackjack_bust()) # testing is_blackjack_bust (should be 1)

    player1.obtain_card(Card("2", "Clubs")) # obtaining a card to test busting
    print(player1) # testing obtain_card and __str__
    print(player1.is_blackjack_bust())
    print(player1.check_value()) 
    player1.obtain_card(Card("9", "Diamonds")) 
    print(player1) 
    print(player1.is_blackjack_bust()) # should be 2

    player2 = Player("Chris", 50)
    print(player2) 
    card3 = Card("King", "Diamonds")
    card4 = Card("9", "Clubs")
    player2.obtain_card(card3)
    player2.obtain_card(card4)
    print(player2) 
    print(player2.check_value()) # should be 19
    print(player2.is_blackjack_bust()) # should be 0
    
    player2.obtain_card(Card("Ace", "Clubs")) # obtaining an Ace to test busting
    print(player2) 
    print(player2.is_blackjack_bust()) 
    print(player2.check_value()) # should be 20
    
    player2.obtain_card(Card("Ace", "Hearts")) 
    print(player2) 
    print(player2.is_blackjack_bust()) # should be 1
    print(player2.check_value()) # should be 21
    
if __name__ == "__main__":
    main()