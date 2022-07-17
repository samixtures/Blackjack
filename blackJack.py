import random
#Rules of game:
 #Player hand
player_hand = []
 #Dealer hand
dealer_hand = []
#"Hit" function
# def p_options(o):
#     if o == "hit"




player_hand.append(random.randint(1,11))
player_hand.append(random.randint(1,11))

dealer_hand.append(random.randint(1,11))
dealer_hand.append(random.randint(1,11))

print("The dealer's hand is x and", dealer_hand[1])
print("Your hand's sum is", sum(player_hand), "with the cards", player_hand)
p_option = input("Hit or Stand? ")
if p_option == "H":
    player_hand.append(random.randint(1,11))
    print("Your hand's sum is", sum(player_hand), "with the cards", player_hand)
while sum(player_hand) <= 21 and p_option == "H":
    p_option = input("Hit or Stand? ")
    if p_option == "H":
        player_hand.append(random.randint(1,11))
    print("Your hand's sum is", sum(player_hand), "with the cards", player_hand)

print("")

if sum(dealer_hand) == 21:
    print("Blackjack! The dealer has reached the number 21 and has won!")
elif sum(player_hand) == 21:
    print("Blackjack! The player has reached the number 21 and has won!")
elif sum(dealer_hand) > 21:
    print("Bust! The dealer has gone over 21. The player wins!")
elif sum(player_hand) > 21:
    print("Bust! The player has gone over 21. The dealer wins!")
else:
    print("Dealer's hand:", sum(dealer_hand), "with the cards", dealer_hand)
    print("Player's hand:", sum(player_hand), "with the cards", player_hand)
    print("")   
    if sum(dealer_hand) > sum(player_hand):
        print("Unfortunately the dealer has won..")
    if sum(player_hand) > sum(dealer_hand):
        print("The player has won!")