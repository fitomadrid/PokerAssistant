import itertools
import random
from collections import Counter
from enum import Enum

class HandRank(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

def create_deck():
    suits = 'HDSC'  
    values = '23456789TJQKA'
    return [value + suit for value in values for suit in suits]

def evaluate_hand(hand):
    hand = sorted(hand, key=lambda x: "23456789TJQKA".index(x[0]))  
    
    is_flush = len(set(card[1] for card in hand)) == 1
    is_straight = all("23456789TJQKA".index(hand[i][0]) - "23456789TJQKA".index(hand[i-1][0]) == 1 for i in range(1, 5))
    
    ranks = Counter([card[0] for card in hand])
    most_common = ranks.most_common()
    highest_freq = most_common[0][1]

    if is_flush and is_straight and hand[-1][0] == 'A':
        return HandRank.ROYAL_FLUSH
    elif is_flush and is_straight:
        return HandRank.STRAIGHT_FLUSH
    elif highest_freq == 4:
        return HandRank.FOUR_OF_A_KIND
    elif highest_freq == 3 and most_common[1][1] == 2:
        return HandRank.FULL_HOUSE
    elif is_flush:
        return HandRank.FLUSH
    elif is_straight:
        return HandRank.STRAIGHT
    elif highest_freq == 3:
        return HandRank.THREE_OF_A_KIND
    elif highest_freq == 2 and most_common[1][1] == 2:
        return HandRank.TWO_PAIR
    elif highest_freq == 2:
        return HandRank.ONE_PAIR
    else:
        return HandRank.HIGH_CARD

def hand_odds(hand, deck):
    hand_ranks = {rank: 0 for rank in HandRank}
    for cards in itertools.combinations(deck, 5 - len(hand)):
        test_hand = list(hand) + list(cards)
        rank = evaluate_hand(test_hand)
        hand_ranks[rank] += 1
    
    total_combinations = sum(hand_ranks.values())
    odds = {rank: combs / total_combinations for rank, combs in hand_ranks.items()}
    return odds

def strategy_advice(hand, deck):
    odds = hand_odds(hand, deck)
    sorted_odds = sorted(odds.items(), key=lambda x: x[1], reverse=True)

    advice = f"With your hand, your best chances are to aim for a {sorted_odds[0][0].name.replace('_', ' ').title()}, "
    advice += f"with a probability of {sorted_odds[0][1]:.2%}."
    return advice

if __name__ == "__main__":
    deck = create_deck()
    hand = random.sample(deck, 2)  
    remaining_deck = [card for card in deck if card not in hand]

    print(f"Your hand: {hand}")
    print(strategy_advice(hand, remaining_deck))