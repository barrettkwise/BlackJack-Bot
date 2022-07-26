import discord
from discord.ext import commands
import blackjack as b
import os

from dotenv import load_dotenv

load_dotenv()


DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
bot = commands.Bot(command_prefix='BJ:')

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
	

@bot.event
async def on_message(message):
        
        if message.author == b.p.name:
                message2 = message.content.lower()
                if message2 == "h" or message2 == "s":
                        b.g.playerChoice = message2
                        print(b.g.playerChoice)
                        
        await bot.process_commands(message)

@bot.command()
async def Starts(ctx):
        b.p.setName(ctx.author)
        
        while (b.g.playerWinFlag != True
               and b.g.dealerWinFlag != True) and b.g.tieFlag != True:
            if b.p.turnOver == False:
                b.p.hits() #player gains a card
                b.d.hits() #dealer gains a card
                b.p.hits() #player gains a card
                b.d.hits() #dealer gains a card
                await ctx.send(b.d.showStartCardsR())  #displays dealer 2nd card
                await ctx.send(b.d.showStartScoreR() ) #displays dealer 2nd card score
                await ctx.send(b.p.showCardsR()  )#displays all of the player cards (in a array currently)
                await ctx.send(b.p.showScoreR()  )#displays total player score
                b.p.turnOver = False

            #Game loops here
            while b.p.turnOver == False:
                
                while b.g.playerChoice != "s" and b.g.playerChoice != "h" and b.p.turnOver == False:
                        
                        if b.g.checkBust():
                                b.g.playerWinFlag = False
                                b.p.turnOver = True
                                b.g.stands()
                                return
                                
                                
                                

                        else:
                                await ctx.send("Hit or Stand? (H/S)")

                                
                                

                        if b.g.playerChoice == "s":
                                b.p.turnOver = True
                                return

                        elif b.g.playerChoice == "h":
                                b.Player.hits(b.p)
                                await ctx.send(b.Player.showCardsR(b.p))
                                await ctx.send(b.Player.showScoreR(b.p))
                                b.Player.showCards(b.p)
                                b.Player.showScore(b.p)
                                b.g.playerChoice = ""
                                b.g.checkStatus(b.d, b.p)
                                if b.g.checkBust() == False:
                                        await ctx.send("Hit or Stand? (H/S)")
                                        print(b.g.playerChoice+"YOMOMA")
                                
                        
                b.g.dealerTurn(b.d, b.p)
                b.g.checkStatus(b.d,b.p)
                await ctx.send(b.d.showStartCardsR())  #displays dealer 2nd card
                await ctx.send(b.d.showStartScoreR() ) #displays dealer 2nd card score
                await ctx.send(b.p.showCardsR()  )#displays all of the player cards (in a array currently)
                await ctx.send(b.p.showScoreR()  )#))
                                

        ##Print who won
        if b.g.playerWinFlag == True:
            print(f"Player wins! \nPlayer Score: {b.p.score} \nDealer Score: {b.d.score}")
        
        elif b.g.dealerWinFlag == True:
            print(f"Dealer wins! \nDealer Score: {b.d.score} \nPlayer Score: {b.p.score}")
        
        else:
            print(f"Tie! \nPlayer Score: {b.p.score} \nDealer Score: {b.d.score}")

@bot.command()
async def Start(ctx):
        b.g.runGame()
        await show(ctx)

    
@bot.command()
async def Hit(ctx):
    pass

@bot.command()
async def say(ctx, msg):
    await ctx.send(msg)

async def show(ctx):
       await ctx.send(b.d.showStartCardsR())  #displays dealer 2nd card
       await ctx.send(b.d.showStartScoreR())  #displays dealer 2nd card score
       await ctx.send(b.p.showCardsR())  #displays all of the player cards (in a array currently)
       await ctx.send(b.p.showScoreR())  #displays total player score

        


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)


