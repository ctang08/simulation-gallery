'''
Project 6: Blackjack Part 4

Author      Tony Song, Christopher Tang                             
Date        05/19/2026

This program creates a game class for a game of blackjack. It initializes a game with a player, dealer, and deck of cards.
The game relies on four classes: Card, Deck, Player, and Game. The game class has methods to play a round of blackjack, 
deal cards, determine the player's move, determine the dealer's move, and determine the winner of the game. 
The main function runs an example game with user input.

The classes were originally written in separate files but combined for this submission.

Written in VSCode.

AI Usage: None

Sources: https://en.wikipedia.org/wiki/Blackjack#Player_decisions
'''

import random

class game:
    def __init__(self, player):
        '''
        Initializes a game with a player and a dealer.

        Args:
            player: The player of the game.
            dealer: The dealer of the game.
        '''
        self.player = player
        dealer = Player("Dealer", 0)
        self.dealer = dealer
        self.deck = Deck()
        self.deck.shuffle() # need to shuffle
        self.split_hands = [] # for storing the split hands

    def play(self, bet_amount):
        '''
        Plays a game of blackjack

        Args:
            bet_amount: The amount of money the player wants to bet for this round.
        '''
        self.player.place_bet(bet_amount)
        if self.player.bet == 0:
            print("This will be a practice round with 0 bet. No money will be won or lost.") # If you don't have enough money or place a bet too large
        self.deal() # deal cards
        game_status = 0
        while game_status == 0: # integer so multiple states can be represented
            game_status = self.player.is_blackjack_bust()
            if game_status == 1:
                print(self.player.name + " has a blackjack!")
                break
            elif game_status == 2:
                print(self.player.name + " has busted!")
                break
            else:
                game_status = self.player_move()
                
        if game_status == -1 or game_status == 1: # player stands or cannot do anything else
            self.dealer_move()
            self.determine_winner()
        if game_status == 2:
            self.determine_winner() # to determine the loss from the bust
        if game_status == -2: # split hands
            self.play_split_hands()


    def deal(self):
        '''
        Deals two cards to the player and the dealer at the start of the game.
        '''
        self.player.reset_hand()
        self.dealer.reset_hand()
        for i in range(2):
            self.player.obtain_card(self.deck.deal_card())
            self.dealer.obtain_card(self.deck.deal_card())
        print(self.player.name + "'s hand: " + self.player.show_hand())
        print("Dealer's hand: " + str(self.dealer.hand[0]) + " and [Hidden Card]")
        print("Remaining cards in deck: " + str(len(self.deck.cards)))

    def player_move(self):
        '''
        Asks the player if they want to hit, stand, split, or double and performs the corresponding action.
        '''
        move = self.player.ask_move()
        if move == "h":
            self.player.obtain_card(self.deck.deal_card())
            print(self.player.name + "'s hand: " + self.player.show_hand())
            return 0
        elif move == "st":
            print(self.player.name + " stands with a hand value of " + str(self.player.check_value()))
            return -1
        elif move == "sp":
            if self.player.hand[0].rank == self.player.hand[1].rank and len(self.player.hand) == 2:
                if self.player.bet * 2 > self.player.money+self.player.bet:
                    #print(self.player.bet, self.player.bet*2, self.player.money) debug
                    print("Not enough money to split the hand. Please choose another move.")
                    return 0
                else:
                    print("Splitting hand into two hands.")
                    self.split_hands = []
                    # Create a new hand for the split
                    split_hand = [self.player.hand.pop()]
                    self.split_hands.append(split_hand)
                    split_hand = [self.player.hand.pop()]
                    self.split_hands.append(split_hand)
                    return -2 # to indicate that the player has split and is now playing the split hands
            else:
                print("You cannot split this hand. Please choose another move.")
                return 0
        elif move == "d":
            if len(self.player.hand) != 2:
                print("You can only double down on your initial hand. Please choose another move.")
                return 0
            temp_bet = self.player.bet
            self.player.no_bet() # to reset the player's bet to 0 before placing the new bet for doubling down
            self.player.place_bet(temp_bet * 2)
            if self.player.bet == 0 and temp_bet != 0: # if the bet becomes 0 after trying to double, that means the player did not have enough money to double
                print("Not enough money to double the bet. Please choose another move.")
                self.player.no_bet()
                self.player.place_bet(temp_bet)
                return 0
            else:
                self.player.obtain_card(self.deck.deal_card()) # you get a card after doubling automatically
                print(self.player.name + "'s hand: " + self.player.show_hand())
                if self.player.check_value() >= 21: # blackjack and bust are dealt with in the play method loop
                    return 0
                return -1
        else:
            print("Invalid input. Please enter 'h' for hit, 'st' for stand, 's' for split, or 'd' for double.")
            return 0

    def dealer_move(self):
        '''
        The dealer hits until their hand value is at least 17, then stands. 
        They must hit even if their hand's value is greater than the player's hand.
        This method simulates the dealer. It is to be called after the player stands or has no more moves to make.
        '''
        print("Dealer's hand: " + self.dealer.show_hand())
        
        while self.dealer.check_value() < 17:
            self.dealer.obtain_card(self.deck.deal_card())
            print("Dealer hits and now has: " + self.dealer.show_hand())
        
        if self.dealer.check_value() > 21:
            print("Dealer busts with a hand value of " + str(self.dealer.check_value()))
        elif self.dealer.check_value() == 21:
            print("Dealer has a blackjack!")
        else:
            print("Dealer stands with a hand value of " + str(self.dealer.check_value()))
        

    def determine_winner(self):
        '''
        Determines the winner of the game based on the player's and dealer's hand values and updates the player's money accordingly.
        '''
        player_value = self.player.check_value()
        dealer_value = self.dealer.check_value()
        
        if player_value == 21:
            if dealer_value == 21:
                print("Both " + self.player.name + " and the dealer have a blackjack! It's a tie with both having a hand value of 21. No money is won or lost.")
                self.player.tie_bet()
            else:
                self.player.win_bet()
        elif player_value > 21:
            self.player.lose_bet()
        elif dealer_value > 21:
            self.player.win_bet()      
        elif player_value > dealer_value:
            print(self.player.name + " wins with a hand value of " + str(player_value) + " against the dealer's hand value of " + str(dealer_value) + "!")
            self.player.win_bet()
        elif player_value < dealer_value:
            print(self.player.name + " loses with a hand value of " + str(player_value) + " against the dealer's hand value of " + str(dealer_value) + ".")
            self.player.lose_bet()
        else:
            print("It's a tie with both having a hand value of " + str(player_value) + ". No money is won or lost.")
            self.player.tie_bet()

    def play_split_hands(self):
        '''
        Plays out the split hands after the player has chosen to split. 
        Each hand is played separately and then compared to the dealer's hand to determine the winner for each hand.
        '''
        totalbets = self.player.bet*2
        if len(self.split_hands) == 0:
            return
        else:
            print("Playing out the split hands.")
            temp_players = []
            count = 0
            for hand in self.split_hands: # create a temporary player for each hand
                count +=1
                temp_player = Player(self.player.name + "'s Split Hand #" + str(count), self.player.money+self.player.bet) # create a temporary player for the split hand with the same amount of money as the original player since they will be placing the same bet
                temp_player.hand = hand
                temp_player.obtain_card(self.deck.deal_card()) # deal one more card to the split hand
                temp_player.place_bet(self.player.bet)
                print("Split hand #" + str(count) + ": " + temp_player.show_hand())

                game_status = 0
                while game_status == 0: # same logic as main game loop but abbreviated
                    game_status = temp_player.is_blackjack_bust()
                    if game_status == 1:
                        print(temp_player.name + " has a blackjack!")
                        break
                    elif game_status == 2:
                        print(temp_player.name + " has busted!")
                        break
                    else:
                        move = temp_player.ask_split_move()
                        if move == "h":
                            temp_player.obtain_card(self.deck.deal_card())
                            print(temp_player.name + "'s hand: " + temp_player.show_hand())
                        elif move == "st":
                            print(temp_player.name + " stands with a hand value of " + str(temp_player.check_value()))
                            break
                        elif move == "d":
                            if len(temp_player.hand) != 2:
                                print("You can only double down on your initial hand. Please choose another move.")
                            else:
                                if totalbets + temp_player.bet > self.player.money+self.player.bet:
                                    print("Not enough money to double the bet. Please choose another move.")
                                else:
                                    totalbets += temp_player.bet
                                    temp_bet = temp_player.bet
                                    temp_player.no_bet()
                                    temp_player.place_bet(temp_bet * 2)
                                    temp_player.obtain_card(self.deck.deal_card()) # you get a card after doubling automatically
                                    print(temp_player.name + "'s hand: " + temp_player.show_hand())
                                    if temp_player.check_value() >= 21: # blackjack and bust are dealt with in the play method loop
                                        game_status = 0
                                    else:
                                        game_status = -1
                                        break
                        else:
                            print("Invalid input. Please enter 'h' for hit, 'st' for stand, or 'd' for double down.")
                temp_players.append(temp_player)
            self.dealer_move()
            total_earnings = 0
            self.player.no_bet() # to reset the player's bet to 0 since the split hands have already placed their bets

            for hand in temp_players: # calculate the total amount earned from the split hands as we were not directly modifying the player object before
                self.determine_winner_split(hand)
                total_earnings += hand.money-self.player.money
            self.player.money = self.player.money+total_earnings # update the player's money based on the outcomes of the split hands

    def determine_winner_split(self, temp_player):
        '''
        Determines the winner of the split hand based on the player's and dealer's hand values and updates the player's money accordingly.
        
        Args:
            temp_player: The temporary player object representing the split hand being evaluated.
        '''
        player_value = temp_player.check_value()
        dealer_value = self.dealer.check_value()
        
        if player_value > 21:
            temp_player.lose_bet() # player busted already and lost money already in the earlier game loop
        elif player_value == 21:
            if dealer_value == 21:
                print("Both " + temp_player.name + " and the dealer have a blackjack! It's a tie with both having a hand value of 21. No money is won or lost.")
                temp_player.tie_bet()
            else:
                temp_player.win_bet() # player has a blackjack and won money already in the earlier game loop
        elif dealer_value > 21:
            temp_player.win_bet()
        elif player_value > dealer_value:
            print(temp_player.name + " wins with a hand value of " + str(player_value) + " against the dealer's hand value of " + str(dealer_value) + "!")
            temp_player.win_bet()
        elif player_value < dealer_value:
            print(temp_player.name + " loses with a hand value of " + str(player_value) + " against the dealer's hand value of " + str(dealer_value) + ".")
            temp_player.lose_bet()
        else:
            print("It's a tie with both having a hand value of " + str(player_value) + ". No money is won or lost.")
            temp_player.tie_bet()

class Deck:
    def __init__(self, number_of_decks = 1):
        '''
        Initializes a standard deck of 52 playing cards with 4 suits and 13 ranks.
        '''
        self.cards = []
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for deck in range(number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))
    
    
    def deal_card(self):
        '''
        Removes and returns the top card from the deck.

        Returns: The card that was dealt from the deck.
        '''
        if len(self.cards) == 0:
            print("No more cards in the deck. Obtaining new deck.")
            self.reset()
        return self.cards.pop()
    
    
    def shuffle(self):
        '''
        Shuffles the cards in the deck using random.shuffle. Makes sure that it is not the same as before.
        '''
        if len(self.cards) > 1:
            original = self.cards[:]
            while self.cards == original:
                random.shuffle(self.cards)
        for card in self.cards:
            if card.rank == "Ace":
                card.changeAce("up")

    def reset(self):
        '''
        Resets the deck to its original state with all 52 cards.
        '''
        self.__init__()
        

    def __str__(self):
        '''
        Returns a string representation of the deck.

        Returns: A string containing all the cards in the deck.
        '''
        str1 = ''
        for card in self.cards:
            str1 += f'{card}\n'
        return str1

    
    def __eq__(self, other):
        '''
        Compares two decks for equality.

        Args:
            other (Deck): The other deck to compare with.

        Returns:
            bool: True if the decks are equal, False otherwise.
        '''
        return self.cards == other.cards

class Card:
    def __init__(self, rank, suit):
        """Initializes the instance based on card rank and suit.

        Args:
          rank: String representing the rank of the card found on the card face
          suit: String representing the suit of the card found on the card face
        """
        self.rank = rank

        # The rank of the card determines its value in blackjack
        if self.rank in ["Jack", "Queen", "King"]: 
            self.value = 10
            self.symbol = self.rank[0] # J, Q, K 
        elif self.rank == "Ace":
            self.value = 11
            self.symbol = "A"
        else:
            self.value = int(self.rank)
            self.symbol = self.rank
            if self.rank == "10":
                self.symbol = "T"
        self.suit = suit

    suits = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"} # for printing out unicode symbols

    def describe(self):
        """
        Prints out a description of the card including its rank, suit, and value.
        """
        print(self.rank + " of " + self.suit + " worth " + str(self.value))

    def changeAce(self, direction = "down"):
        """
        Changes the value of an Ace from 11 to 1 for blackjack purposes. If the card is not an Ace, nothing happens.
        
        Returns: boolean on whether the ace was changed
        """
        if self.rank == "Ace" and self.value == 11 and direction == "down":
            self.value = 1
        elif self.rank == "Ace" and self.value == 1 and direction == "up":
            self.value = 11
        #else:
            #print("This card is not an Ace and its value was not changed")


    # Overriding string printout for the Card class
    def __str__(self):
        return self.symbol+self.suits[self.suit]


    # Overriding equivalence for the Card class to compare based on rank and suit
    # My understanding is that both rank and suit need to be the same for two cards to be considered equal
    def __eq__(self, other):
        """
        Checks if two Card objects are equal based on their rank and suit.

        Args:
          other: Another Card object to compare with
        """
        try:
            return self.rank == other.rank and self.suit == other.suit
        except:
            return False
        
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

    def reset_hand(self):
        '''
        Resets the player's hand to an empty list.
        '''
        self.hand = []
    
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
        Places a bet for the player. The money is taken out of the total money first.

        Args:
            bet: The amount of money the player wants to bet.
        '''
        if bet > self.money:
            print("Not enough money.")
            self.bet = 0
        else:
            self.money -= bet
            self.bet = bet

    def win_bet(self):
        '''
        Updates the player's money when they win a bet.
        '''
        self.money += 2*self.bet
        print(self.name + " wins $" + str(self.bet))
        self.bet = 0

    def lose_bet(self):
        '''
        Updates the player's money when they lose a bet.
        '''
        print(self.name + " loses $" + str(self.bet))
        self.bet = 0
        

    def tie_bet(self):
        '''
        Updates the player's money when they tie a bet (no change).
        '''
        self.money += self.bet
        print(self.name + " ties the bet.")
        self.bet = 0

    def no_bet(self):
        '''
        Removes the bet and returns the money to the player. Mainly for use with split bets.
        '''
        self.money += self.bet
        self.bet = 0

    def show_hand(self):
        '''
        Displays the player's hand.

        Returns: A string representation of the player's hand.
        '''
        hand_str = ""
        for card in self.hand:
            hand_str += f'{card} '
        return hand_str
    
    def ask_move(self):
        '''
        Asks the player for their move.

        Returns: A string representing the player's move.
        '''
        move = input("Do you want to hit or stand? (Enter 'h' for hit, 'st' for stand, 'sp' for split, 'd' for double) > ")
        return move
    
    def ask_split_move(self):
        '''
        Asks the player for their move when they have split hands.

        Returns: A string representing the player's move for the split hand.
        '''
        move = input("Do you want to hit or stand for the split hand? (Enter 'h' for hit, 'st' for stand, or 'd' for double) > ")
        return move

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
    Main function to run an example game of blackjack with user input for name, money, and bets
    """
    name = input("What is your name? > ")
    total_money = int(input("How much money do you want to start with? > "))
    player1 = Player(name, total_money)
    game1 = game(player1)
    while True:
        print(player1.name + " now has $" + str(player1.money) + ".")
        bet1 = int(input("How much do you want to bet? (0: practice round; -1: quit) > "))
        if bet1 == -1:
            print("Goodbye!")
            break
        game1.play(bet1)
    
if __name__ == "__main__":
    main()