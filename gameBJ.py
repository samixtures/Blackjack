import random

class BJ_player:
    def __init__(self, name):
        self.name = name
        self.hand = [random.randint(1,11), random.randint(1,11)]

    def speak(self):
        print("wuddup")
    
    def hit(self):
        self.hand.append(random.randint(1,11))

    def display_hand(self):
        print(f"{self.name}'s hand sum: {self.sumHand()} with cards {str(self.hand)[1:-1]}")

    def sumHand(self):
        return sum(self.hand)

class BJ_dealer(BJ_player):
    def __init__(self,name):
        super().__init__(name)
    def dealer_display_hand(self):
        print(f"{self.name}'s hand has x and {self.hand[1]}")


