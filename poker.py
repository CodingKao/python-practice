# Generate 13 random cards from a standard deck

# Import 'random' function
import random
from collections import Counter

# Define the poker hand ranking
poker_hand_rankings = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

# Function to generate 13 random cards from a standard deck
def deal_cards():
    # Define the suits and ranks in a deck of cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades',]
    ranks = ['2', '3', '4', '4', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace' ]

    # Generate a full deck of 52 cards by combining each rank with each suit
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

    # Shuffle the deck to randomize the order of the cards
    random.shuffle(deck)

    # Deal the first 13 cards from the shuffled deck
    player_hand = deck[:5]
    dealer_hand = deck[6:10]

    # Return the 13 random cards
    return player_hand, dealer_hand

# Function to extract rank and suit information from the hand
def extract_ranks_and_suits(hand):
    ranks = []
    suits = []
    for card in hand:
        rank, suit = card.split(' of ')
        ranks.append(rank)
        suits.append(suit)
    return ranks, suits

# Deal 5 cards to each player and dealer
player_hand, dealer_hand = deal_cards()

# Deal 13 cards to player and print the player's hand
print("Player's hand:", player_hand)
print("Dealer's hand:", dealer_hand)