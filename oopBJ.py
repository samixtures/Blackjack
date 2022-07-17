import gameBJ as gbj

player = gbj.BJ_player("Player")
player.display_hand()

dealer = gbj.BJ_dealer("Dealer")
dealer.display_hand()
dealer.dealer_display_hand() #Calling a method that shows only 1 of the dealer's cards (Like in actual Blackjack)
