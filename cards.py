import random

#defines the cards and names them
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def name_card(self):
        if self.value == 11:
            value = "Jack"
        elif self.value == 12:
            value = "Queen"
        elif self.value == 13:
            value = "King"
        elif self.value == 1:
            value = "Ace"
        else:
            value = self.value
        print(f"{value} of {self.suit}")

#creates a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
    
    #create a deck with all cards 
    def make_deck(self):
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for i in range(1, 14):
                self.cards.append(Card(suit,i))
    
    #shuffle the deck
    def shuffle(self):
        length = len(self.cards)
        #go through each card one by one and swap places with a random card 
        for each in range(length-1, 0, -1):
            pick = random.randint(0, each)
            if pick == each:
                continue
            self.cards[each], self.cards[pick] = self.cards[pick], self.cards[each]
    
    #display deck of cards
    def show(self):
        for i in self.cards:
            i.name_card()
    
    #take a card out of deck
    def take(self):
        return self.cards.pop()

#creates a player who introduces, picks and shows a hand, and has a score
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def greeting(self):
        print(f"Hello, my name is {self.name}!")
    
    #picks a card from deck as many times as you want
    def pick_hand(self, Deck, num=1):
        for _ in range(num):
            choice = Deck.take() #use take func from above
            self.hand.append(choice) #add it to player's hand
    
    #shows the players hand
    def show(self):
        for i in self.hand:
            i.name_card() #uses name_card from above to display each card in hand  
    
    #calculate a score for each players hand
    def score(self):
        score = 0
        for i in self.hand:
            score += i.value
        return score
            

#here we play a game that makes a deck, shuffles it.
the_deck = Deck()
the_deck.make_deck()
#the_deck.show()

the_deck.shuffle()
#the_deck.show()

#then player A greets, picks a hand of 5, and displays it.
mahika = Player("Mahika")
mahika.greeting()
mahika.pick_hand(the_deck, 5)
mahika.show()

#then player B greets, picks a hand of 5, and displays it.
rahul = Player("Rahul")
rahul.greeting()
rahul.pick_hand(the_deck, 5)
rahul.show() 

#then the two players compete by comparing their hand scores to see whos is higher and wins.
if mahika.score() > rahul.score():
    print("Mahika Won")
else:
    print("Rahul Won")