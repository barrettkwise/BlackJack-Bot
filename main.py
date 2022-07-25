import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

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
    'Ace': 11, #NEED TO FIX ACE TO CHANGE IF OVER 21
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

    def hits(self): #Dealer generate a card
        card, score = draw_card() #Generate card

        self.cards.append(card)
        self.score += score
  
    def showStartCards(self):
        print(f"Dealer card: {self.cards[1]}")

    def showCards(self):
        print(f"Dealer cards: {self.cards}")

    def showStartScore(self):
        print(f"Dealer score: {points[self.cards[1]]}")

    def showScore(self):
        print(f"Dealer score: {self.score}")

#Player Class with Player functions
class Player:
    def __init__(self):
        self.score = 0
        self.cards = []
        self.turnOver = False

    def hits(self): #Player generates a card
        card, score = draw_card() #Generate card

        self.cards.append(card)
        self.score += score

        if player.score > 21:
          game.player.WinFlag = False #DOES THIS WORK ??

    def stands(self): #Players ends turn
        pass

    def showCards(self):
        print(f"Player cards: {self.cards}") #NEEDS TO PRINT AS A STRING 

    def showScore(self):
        print(f"Player score: {self.score}")

#Manages Game and controls dealer/player moves
class Game (Player, Dealer):
    def __init__(self, Player, Dealer):
        self.playerWinFlag = False
        self.dealerWinFlag = False
        self.tieFlag = False 

    def runGame(self):
        while (self.playerWinFlag != True or self.dealerWinFlag != True) or self.tieFlag == True:
            Player.hits(p) #player gains a card
            Dealer.hits(d) #dealer gains a card
            Player.hits(p) #player gains a card
            Dealer.hits(d) #dealer gains a card
            Dealer.showStartCards(d) #displays dealer 2nd card
            Dealer.showStartScore(d) #displays dealer 2nd card score
            Player.showCards(p) #displays all of the player cards (in a array currently)
            Player.showScore(p) #displays total player score
            break #add check status here

        print("Game Over!")

    def checkStatus(self): #Determines result of match
        if Dealer.score == 21:
          if Player.score == 21:
            self.tieFlag = True
          else:
            self.dealerWinFlag = True
        
        elif Player.turnOver == True and Dealer.turnOver == True:
          if Player.score > 
            
    def dealerTurn(Dealer, Player): ##Dealer AI
      while Dealer.turnOver == False:
        if Dealer.score < 17 and Player.score > Dealer.score:
          Dealer.hits(p)
        elif:
          Dealer.turnOver = True
        


p = Player()
d = Dealer()
g = Game(p, d)
print(g.runGame())
'''
# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = "token"

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
  
# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.content == "!blackjack":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)'''
