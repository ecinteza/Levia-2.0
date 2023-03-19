import discord
from discord.ext import commands
import json
from threading import Thread
import asyncio

whotorun = "beta"
# beta / bot

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

prefix = '?'
botactivity = "ur mom"

if whotorun == "beta":
    prefix = "."
    botactivity = "ur dad"

bot = commands.Bot(command_prefix=prefix,
                   intents=intents,
                   activity=discord.Activity(type=discord.ActivityType.listening, name=botactivity))

##################################
#     EVENTS                     #
import message_events.mock       #
import message_events.wordle     #
import message_events.cazino     #
##################################

 ####### #     #                #     # #######  #####   #####     #     #####  ####### 
 #     # ##    #                ##   ## #       #     # #     #   # #   #     # #       
 #     # # #   #                # # # # #       #       #        #   #  #       #       
 #     # #  #  #                #  #  # #####    #####   #####  #     # #  #### #####   
 #     # #   # #                #     # #             #       # ####### #     # #       
 #     # #    ##                #     # #       #     # #     # #     # #     # #       
 ####### #     #                #     # #######  #####   #####  #     #  #####  ####### 
                                                                  
@bot.event  
async def on_message(message):
    if message.author.bot or len(message.content) == 0:
        return
    
    # PROCESS COMMANDS
    if message.content.startswith(prefix):
        process = message.content.split(" ")[0].lower()
        process += message.content[len(process):len(message.content)]
        message.content = process
        await bot.process_commands(message)
        return
    
    if message.content.lower() == "im bacc":
        await message.channel.send("better than ever", reference=message)
        
    await message_events.mock.mocking(message)
    await message_events.mock.reply3(message)
    await message_events.wordle.msg_wordle(message)
    await message_events.mock.wys(message)
    await message_events.cazino.roulette_thr(message)

###########
# CAZINO
###########

@bot.command(brief = "Roulette")
async def roulette(ctx):
    asyncio.get_event_loop().create_task(message_events.cazino.roulette(ctx))
    
import commands.gambling

@bot.command(brief = "Slots")
async def slots(ctx):
    await commands.gambling.slots(ctx)

#######################################################
#   IDK                                               #
@bot.command(brief = "Let me google that for you")    #
async def idk(ctx, *args):                            #
    await message_events.mock.idk(ctx, args)          #
#######################################################
#   WORDLE                                            #
@bot.command(brief = "Spanzuratoarea but in english") #
async def wordle(ctx, *args):                         #
    await message_events.wordle.wordle(ctx, *args)    #
#######################################################

###################################################################

 #####    ##    ####  #  ####   ####  
 #    #  #  #  #      # #    # #      
 #####  #    #  ####  # #       ####  
 #    # ######      # # #           # 
 #    # #    # #    # # #    # #    # 
 #####  #    #  ####  #  ####   ####  
 
###################################################################    
@bot.command(brief = "Client Version")
async def version(ctx):
    await ctx.send("xLevia v2.1.1")

import commands.basics                                            
@bot.command(brief = "Pong")                                      
async def ping(ctx):                                              
    await commands.basics.ping(ctx, bot)                          
                                                                                                                          
@bot.command(brief = "Get the dominant hex of ur profile pic",
             aliases = ['phex'])    
async def pfphex(ctx):                                            
    await commands.basics.pfphex(ctx)                             

@bot.command(brief = "Start a poll")
async def poll(ctx, *args):
    await commands.basics.poll(ctx, *args)
    
@bot.command(brief = "Send a suggestion",
             aliases = ["suggestion"])
async def suggest(ctx, *args):
    await commands.basics.suggest(ctx, bot, *args)
    
@bot.command(brief = "Check what colour a hex is")
async def hex(ctx, *args):
    await commands.basics.hex(ctx, *args)
    
@bot.command(brief = "Get the dominant hex palette of ur profile pic",
             aliases = ['phexpal', 'phexp'])
async def pfphexpal(ctx):
    await commands.basics.pfphexpal(ctx)
    
@bot.command(brief = "Get your or mentioned user's avatar")
async def avatar(ctx):
    await commands.basics.avatar(ctx)
    
@bot.command(brief = "Report a bug")
async def report(ctx, *args):
    await commands.basics.report(ctx, bot, *args)
    
    
###################################################################
                      
 ###### #    # #    # 
 #      #    # ##   # 
 #####  #    # # #  # 
 #      #    # #  # # 
 #      #    # #   ## 
 #       ####  #    # 
                      
###################################################################

import commands.fun
@bot.command(brief = "Let's see how big ur peen is",
             aliases = ["pula"])
async def penis(ctx):
    await commands.fun.penis(ctx)
    
@bot.command(brief = "see how much u are compatible w someone")
async def love(ctx, *args):
    await commands.fun.love(ctx, *args)

@bot.command(brief = "see how much u hate someone")
async def hate(ctx, *args):
    await commands.fun.hate(ctx, *args)

@bot.command(brief = "Search for words in the dictionary")
async def dict(ctx, *args):
    await commands.fun.dict(ctx, *args)
    
@bot.command(brief = "Search for words in the urban dictionary")
async def urban(ctx, *args):
    await commands.fun.urban(ctx, *args)
    
@bot.command(brief = "Rock Paper & Scissors")
async def rps(ctx, arg):
    await commands.fun.rps(ctx, arg)
    
###################################################################
                                                 
  ####  ###### #    #  ####  #    # # #    # 
 #    # #      ##   # #      #    # # ##   # 
 #      #####  # #  #  ####  ###### # # #  # 
 #  ### #      #  # #      # #    # # #  # # 
 #    # #      #   ## #    # #    # # #   ## 
  ####  ###### #    #  ####  #    # # #    # 
                                             
###################################################################
    
import commands.genshin
@bot.command(brief = "See how many wishes you have")
async def wishes(ctx, arg):
    await commands.genshin.wishes(ctx, prefix, arg)

@bot.command(brief = "Crit Value Calculator [crit rate * 2 + crit damage]")
async def cvc(ctx, *args):
    await commands.genshin.cvc(ctx, prefix, *args)
    
@bot.command(brief = "Ascension Mats Today")
async def asct(ctx):
    await commands.genshin.asct(ctx)
    
###################################################################

 #    #  ####  #####   ####  
 ##  ## #    # #    # #      
 # ## # #    # #    #  ####  
 #    # #    # #    #      # 
 #    # #    # #    # #    # 
 #    #  ####  #####   ####  

###################################################################

import commands.mods
@bot.command(brief = "Change a role's colour [MODS ONLY]",
             description="rolecolour id:ID / #hex\nrolecolour name:NAME / hex",
             aliases=["rolecolor"])
@discord.ext.commands.has_role(719954439078936619)
async def rolecolour(ctx, *args):
    arguments = " ".join(args)
    c = arguments.split(" / ")
    await commands.mods.rolecolour(ctx, arguments, c)
    
###################################################################
                               
   ##   #####  #    # # #    # 
  #  #  #    # ##  ## # ##   # 
 #    # #    # # ## # # # #  # 
 ###### #    # #    # # #  # # 
 #    # #    # #    # # #   ## 
 #    # #####  #    # # #    # 
                               
###################################################################

import commands.admin
@bot.command(brief = "Fetch messages [ADMIN ONLY]",
             description="fm [channel id] [user id] [number of messages to search through]")
async def fm(ctx, *args):
    await commands.admin.fm(ctx, bot, *args)


@bot.command(brief = "Mark the status of the ticket [ADMIN ONLY]")
async def ticket(ctx, *args):
    await commands.admin.ticket(ctx, bot, *args)
    
with open('TOKENS.json') as f:
        data = json.load(f)
        bot.run(data[whotorun])