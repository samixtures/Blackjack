import random
#Rules of game:
 #Player hand
player_hand = []
 #Dealer hand
dealer_hand = []



player_hand.append(random.randint(1,11))
player_hand.append(random.randint(1,11))

dealer_hand.append(random.randint(1,11))
dealer_hand.append(random.randint(1,11))

print("The dealer's hand is x and", dealer_hand[1])
print("Your hand is", player_hand)
if sum(dealer_hand) == 21:
    print("Blackjack! The dealer has reached the number 21 and has won!")
elif sum(player_hand) == 21:
    print("Blackjack! The player has reached the number 21 and has won!")
elif sum(dealer_hand) > 21:
    print("Bust! The dealer has gone over 21. The player wins!")
elif sum(player_hand) > 21:
    print("Bust! The player has gone over 21. The dealer wins!")