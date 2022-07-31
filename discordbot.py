import discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands
import blackjack as b
import os
from keep_alive import keep_alive
import tools as tl

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
bot = commands.Bot(command_prefix='bj:')


@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("BarryJack is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
        g = None
        for game in b.games:
                if  message.author == game.player.name:
                        g = game
                        break
                
        if message.author != bot.user and g != None:
                msg = "```" + str(message.author.display_name) + " is betting " + str(g.player.bet) + " moneys!\n"
                message2 = message.content.lower()
                if message2 == "bj:g":
                        b.games.remove(g)
                        await message.channel.send("```GAME ENDED```")
                        tl.modMON(message.guild, message.author,-1 * g.player.bet)
                        return
                
                if message2 == "h":
                        g.player.hits()
                        if checkBust(g) == False:
                                msg += g.player.showCardsR() + "\n"
                                msg += g.player.showScoreR() + "\n"
                                msg += "Hit or Stand (h/s)" + "\n"
                                
                        else:
                                msg += "You busted!" + "\n"
                                g.dealerTurn(g.dealer, g.player)
                                msg += g.player.showCardsR() + "\n"
                                msg += g.player.showScoreR() + "\n"
                                msg += g.dealer.showCardsR() + "\n"
                                msg += g.dealer.showScoreR() + "\n"
                                if g.dealer.score == g.player.score:
                                       msg += "\nYOU TIED \n" 

                                elif  g.player.score > 21 or (g.dealer.score > g.player.score and g.dealer.score < 22):
                                        msg += "\nDEALER WON, YOU LOST \n"
                                        tl.modMON(message.guild, message.author,-1 * g.player.bet)

                                else:
                                        msg += "\nYOU WON, DEALER LOST \n"
                                        tl.modMON(message.guild, message.author, g.player.bet)
                        
                                b.games.remove(g)

                elif message2 == "s":
                        #b.g.player.stands()
                        g.dealerTurn(g.dealer, g.player)
                        msg += g.player.showCardsR() + "\n"
                        msg += g.player.showScoreR() + "\n"
                        msg += g.dealer.showCardsR() + "\n"
                        msg += g.dealer.showScoreR() + "\n"
                        if g.dealer.score == g.player.score:
                               msg += "\nYOU TIED \n" 

                        elif  g.player.score > 21 or (g.dealer.score > g.player.score and g.dealer.score < 22):
                                msg += "\nDEALER WON, YOU LOST \n"
                                tl.modMON(message.guild, message.author,-1 * g.player.bet)
                        else:
                                msg += "\nYOU WON, DEALER LOST \n"
                                tl.modMON(message.guild, message.author, g.player.bet)
                
                        b.games.remove(g)

                msg += "```"
                await message.channel.send(msg)

        await bot.process_commands(message)

@bot.command()
async def g(ctx, mon: int):
        if tl.getMON(str(ctx.guild.id), ctx.author) <= 0:
                tl.modMON(ctx.guild, ctx.author, 5)
                await ctx.channel.send("You had no money so we gave you 5")
        
        if tl.getMON(str(ctx.guild.id), ctx.author) >= mon:
                g = b.Game(b.Player(), b.Dealer())
                g.player.bet = mon
                b.games.append(g)
                
                #limit amount of games
                if len(b.games) > 50:
                        b.games.pop(0)

                g.player.setName(ctx.author)
                setup(g)
                msg = "```" + str(ctx.author.display_name) + " is betting " + str(g.player.bet) + " moneys!\n"
                msg += g.player.showCardsR() + "\n"
                msg += g.player.showScoreR() + "\n"
                msg += g.dealer.showStartCardsR() + "\n"
                msg += g.dealer.showStartScoreR() + "\n"
                msg += "Hit or Stand (h/s)" + "\n"
                msg += "```"
                await ctx.channel.send(msg)
        else:
                await ctx.message.reply(f'{ctx.author.display_name}, you can not bet that much money.')



@bot.command()
async def giveMON(ctx, user: discord.Member, MON: int):
        if user == ctx.author:
                    return

        if MON < 1:
                await ctx.message.reply(f'{ctx.author.display_name}, you must give at least 1 MON with your thanks.')
                return

        guild = ctx.channel.guild
        if MON > tl.getMON(str(guild.id), ctx.author):
                await ctx.message.reply(f'{ctx.author.display_name}, you do not have enough MON to give so much thanks.')
                return
        else:
                tl.modMON(guild, ctx.author,-1 * MON)
                tl.modMON(guild, user, MON)
                await ctx.send(f"You gave {user} {MON} moneys.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"{ctx.author.mention}\nInvalid command for Barry Jack!")
        return
    return error

@bot.command()
async def money(ctx):
        await ctx.channel.send(str(tl.getMON(ctx.guild.id, ctx.author)))

def setup(g):
        g.player.hits()
        g.player.hits()
        g.dealer.hits()
        g.dealer.hits()


def checkBust(g): #check if player busts
        if g.player.score > 21:
            return True
        else:
            return False
  
# EXECUTES THE BOT.
keep_alive()
bot.run(DISCORD_TOKEN)
