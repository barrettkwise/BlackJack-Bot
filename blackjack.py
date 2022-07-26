import discord as dis
from discord.ext import commands
import random as r

##holds cards
cards = {
    1: 'Ace',  #1 or 11
    2: '2',  #2
    3: '3',  #3
    4: '4',  #4
    5: '5',  #5
    6: '6',  #6
    7: '7',  #7
    8: '8',  #8
    9: '9',  #9
    10: '10',  #10
    11: 'Jack',  #10
    12: 'Queen',  #10
    13: 'King'  #10
}

##holds points to cards conversion
points = {
    'Ace': 11,  #NEED TO FIX ACE TO CHANGE IF OVER 21
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

def draw_card():
    global cards
    global points
    random_index = r.randint(1, 13)
    counter = 0
    for i in cards.values():
        counter += 1
        if counter == random_index:
            return [i, points[i]]

    


#Dealer Class with Dealer functions
class Dealer:
    def __init__(self):
        self.score = 0
        self.cards = []
        self.turnOver = False
        self.aceCount = 0
        self.ace1Count = 0

    def hits(self):  #Dealer generate a card
        card, score = draw_card()  #Generate card
        lastcard = len(self.cards)
        self.cards.append(card) 
        if self.cards[lastcard - 1] == "Ace":
          self.aceCount += 1
        self.score += score
        if "Ace" in self.cards and self.score > 21 and self.aceCount != self.ace1Count:
          self.score -= 10
          self.ace1Count += 1

    def showStartCards(self):
        print(f"Dealer card: {self.cards[1]}")
        
    def showStartCardsR(self):
        return(f"Dealer card: {self.cards[1]}")

    def showCards(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        print(f"Dealer cards: {tempstring}")

    def showCardsR(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        return(f"Dealer cards: {tempstring}")

    def showStartScore(self):
        print(f"Dealer score: {points[self.cards[1]]}")

    def showScore(self):
        print(f"Dealer score: {self.score}")

    def showStartScoreR(self):
        return(f"Dealer score: {points[self.cards[1]]}")

    def showScoreR(self):
        return(f"Dealer score: {self.score}")

 
#Player Class with Player functions
class Player:
    def __init__(self):
        self.score = 0
        self.cards = []
        self.turnOver = False
        self.aceCount = 0
        self.ace1Count = 0
        self.name = ""

    def setName(self, name):
        self.name = name

    def hits(self):  #Player generates a card
        card, score = draw_card()  #Generate card
        lastcard = len(self.cards)
        self.cards.append(card)
        if self.cards[lastcard - 1] == "Ace":
          self.aceCount += 1
        self.score += score
        if "Ace" in self.cards and self.score > 21 and self.aceCount != self.ace1Count:
          self.score -= 10
          self.ace1Count += 1 

    def stands(self):  #Players ends turn
        self.turnOver = True

    def showCards(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        print(f"Player cards: {tempstring}")

    def showScore(self):
        print(f"Player score: {self.score}")

    def showCardsR(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        return(f"Player cards: {tempstring}")

    def showScoreR(self):
        return(f"Player score: {self.score}")


#Manages Game and controls dealer/player moves
class Game(Player, Dealer):
    def __init__(self, Player, Dealer):
        self.playerWinFlag = False
        self.dealerWinFlag = False
        self.tieFlag = False
        self.playerChoice = ""

    def makeInput(self): #Make input
        while self.playerChoice != "s" and self.playerChoice != "h" and p.turnOver == False:

            if self.checkBust():
                self.playerWinFlag = False
                p.turnOver = True
                self.stands()
                return 

            else:
                self.playerChoice = str(input("Hit or Stand? (H/S)"))
                self.playerChoice = self.playerChoice.lower()

            if self.playerChoice == "s":
                p.turnOver = True
                return

            elif self.playerChoice == "h":
                Player.hits(p)
                Player.showCards(p)
                Player.showScore(p)
                self.playerChoice = ""
                return

    def runGame(self): #Runs game
        while (self.playerWinFlag != True
               and self.dealerWinFlag != True) and self.tieFlag != True:
            if p.turnOver == False:
                p.hits()  #player gains a card
                d.hits()  #dealer gains a card
                p.hits()  #player gains a card
                d.hits()  #dealer gains a card
                d.showStartCards()  #displays dealer 2nd card
                d.showStartScore()  #displays dealer 2nd card score
                p.showCards()  #displays all of the player cards (in a array currently)
                p.showScore()  #displays total player score
                p.turnOver = False

            #Game loops here
            while p.turnOver == False:
                self.makeInput()
                self.checkStatus(d, p)
                            
            self.dealerTurn(d, p)
            self.checkStatus(d, p)

        ##Print who won
        if self.playerWinFlag == True:
            print(f"Player wins! \nPlayer Score: {p.score} \nDealer Score: {d.score}")
        
        elif self.dealerWinFlag == True:
            print(f"Dealer wins! \nDealer Score: {d.score} \nPlayer Score: {p.score}")
        
        else:
            print(f"Tie! \nPlayer Score: {p.score} \nDealer Score: {d.score}")

    def checkBust(self): #check if player busts
        if p.score > 21:
            self.dealerWinFlag = True
            self.playerWinFlag = False
            return True
        else:
            return False

    def checkStatus(self, dealer, player):  #Determines result of match
        if dealer.score == player.score:
            self.tieFlag = True
            return

        if p.turnOver == True and d.turnOver == True:
            if d.score > p.score or p.score > 21:
                self.dealerWinFlag = True
                return
            else:
                self.playerWinFlag = True
                return

    def dealerTurn(self, dealer, player):  ##Dealer AI
        while dealer.turnOver == False:
            if dealer.score < 17 and player.score > dealer.score and player.score < 22:
                dealer.hits()
                if dealer.score > 21:
                    self.playerWinFlag = True
                    return
            else:
                dealer.turnOver = True
                return

p = Player()
d = Dealer()
g = Game(p, d)

