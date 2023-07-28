import discord
from discord.ext import commands
#from discord import app_commands
import json
import time
import asyncio
from threading import Thread
from datetime import datetime
import mysql.connector
import sys
from commands.utils import detect_link
"""
intents = discord.Intents.default()
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

@tree.command(name = "hi", description = "My first application Command")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
    
with open('TOKENS.json') as f:
    data = json.load(f)
    client.run(data['bot'])
"""

# RUN RUN RUN RUN
whotorun = "bot"
# beta / bot
if len(sys.argv) == 2:
    if sys.argv[1] == "beta":
        whotorun = "beta"

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
#     EVENTS                     
import message_events.mock       
import message_events.wordle     
import message_events.cazino     
import message_events.makemoney
##################################

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(486508485844926475)
    await member.add_roles(role)
    embed = discord.Embed(title = "Member joined",
                          description = f"{member.name}#{member.discriminator } ({member.id})",
                          color = discord.Color.brand_green())
    embed.set_footer(text=datetime.now().strftime("%Y-%m-%d %H:%M"))
    
    Logchannel = bot.get_channel(484331277164740620)
    await Logchannel.send(embed=embed)
    
@bot.event
async def on_member_remove(member):
    embed = discord.Embed(title = "Member left",
                          description = f"{member.name}#{member.discriminator } ({member.id})",
                          color = discord.Color.dark_red())
    embed.set_footer(text=datetime.now().strftime("%Y-%m-%d %H:%M"))
    
    Logchannel = bot.get_channel(484331277164740620)
    await Logchannel.send(embed=embed)
    Logchannel = bot.get_channel(719961466509328406)
    await Logchannel.send(f"**{member.name}#{member.discriminator}** left us...")
    
@bot.event
async def on_message_edit(before, after):
    if before.author.bot or before.content == after.content: return
    if before.content.startswith(prefix): return
    
    embed = discord.Embed(title = f"Message edited in #{before.channel.name} ({before.id})",
                          description = f"Before: **{before.content}** \n\nAfter: **{after.content}**",
                          color = discord.Color.blurple())
    embed.set_footer(text=f"{before.author.name}#{before.author.discriminator } ({before.author.id}) | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    Logchannel = bot.get_channel(484331277164740620)
    await Logchannel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    if message.content.startswith(prefix): return
    if message.content.startswith("bet"): return
    
    embed = discord.Embed(title = f"Message deleted in #{message.channel.name} ({message.id})",
                          description = f"**{message.content}**",
                          color = discord.Color.blurple())
    embed.set_footer(text=f"{message.author.name}#{message.author.discriminator } ({message.author.id}) | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    Logchannel = bot.get_channel(484331277164740620)
    await Logchannel.send(embed=embed)
                                     
                                     
############################################################################################################
                      
@bot.event  
async def on_message(message):
    global dbconnected
    global myconn
    global cursor
    
    if message.author.bot or len(message.content) == 0:
        return

    asyncio.get_event_loop().create_task(message_events.makemoney.makemoney(message, bot))
    
    role = discord.utils.get(message.guild.roles, id=579691573135147020)
    if role not in message.author.roles and detect_link(message) == True:
        await message.delete()
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
    
    asyncio.get_event_loop().create_task(message_events.mock.mocking(message))
    asyncio.get_event_loop().create_task(message_events.mock.reply3(message))
    asyncio.get_event_loop().create_task(message_events.wordle.msg_wordle(message))
    asyncio.get_event_loop().create_task(message_events.mock.wys(message))
    asyncio.get_event_loop().create_task(message_events.cazino.roulette_thr(message))
    

###########
# CAZINO
###########

@bot.command(brief = "Roulette")
async def roulette(ctx, betmoney):
    asyncio.get_event_loop().create_task(message_events.cazino.roulette(ctx, betmoney))
    
import commands.gambling

@bot.command(brief = "Slots")
async def slots(ctx, betmoney):
    asyncio.get_event_loop().create_task(commands.gambling.slots(ctx, betmoney))

#######################################################
#   IDK                                               
@bot.command(brief = "Let me google that for you")    
async def idk(ctx, *args):                            
    asyncio.get_event_loop().create_task(message_events.mock.idk(ctx, args))
#######################################################
#   WORDLE                                            
@bot.command(brief = "Spanzuratoarea but in english") 
async def wordle(ctx, *args):                         
    asyncio.get_event_loop().create_task(message_events.wordle.wordle(ctx, *args))    
#######################################################

###################################################################
# COINS

import commands.coins
@bot.command(brief = "See how much levicoins you have", aliases = ["bal"])
async def balance(ctx):
    asyncio.get_event_loop().create_task(commands.coins.balance(ctx))
    
@bot.command(brief = "Donate money to someone")
async def donate(ctx, arg):
    asyncio.get_event_loop().create_task(commands.coins.donate(ctx, arg))
###################################################################

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
    await ctx.send("xLevia v2.5")

import commands.basics                                            
@bot.command(brief = "Pong")                                      
async def ping(ctx):                                              
    asyncio.get_event_loop().create_task(commands.basics.ping(ctx, bot))                          
                                                                                                                          
@bot.command(brief = "Get the dominant hex of ur profile pic",
             aliases = ['phex'])    
async def pfphex(ctx):                                            
    asyncio.get_event_loop().create_task(commands.basics.pfphex(ctx))                             

@bot.command(brief = "Start a poll")
async def poll(ctx, *args):
    asyncio.get_event_loop().create_task(commands.basics.poll(ctx, *args))
    
@bot.command(brief = "Send a suggestion",
             aliases = ["suggestion"])
async def suggest(ctx, *args):
    asyncio.get_event_loop().create_task(commands.basics.suggest(ctx, bot, *args))
    
@bot.command(brief = "Check what colour a hex is")
async def hex(ctx, *args):
    asyncio.get_event_loop().create_task(commands.basics.hex(ctx, *args))
    
@bot.command(brief = "Get the dominant hex palette of ur profile pic",
             aliases = ['phexpal', 'phexp'])
async def pfphexpal(ctx):
    asyncio.get_event_loop().create_task(commands.basics.pfphexpal(ctx))
    
@bot.command(brief = "Get your or mentioned user's avatar")
async def avatar(ctx):
    asyncio.get_event_loop().create_task(commands.basics.avatar(ctx))
    
@bot.command(brief = "Report a bug")
async def report(ctx, *args):
    asyncio.get_event_loop().create_task(commands.basics.report(ctx, bot, *args))
    
    
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
    asyncio.get_event_loop().create_task(commands.fun.penis(ctx))
    
@bot.command(brief = "Let's see how dilated you are",
             aliases = ["pusay", "pizda"])
async def pussy(ctx):
    asyncio.get_event_loop().create_task(commands.fun.pussy(ctx))
    
@bot.command(brief = "see how much u are compatible w someone")
async def love(ctx, *args):
    asyncio.get_event_loop().create_task(commands.fun.love(ctx, *args))
    
@bot.command(brief = "See a message how it'd look mocked")
async def mock(ctx, *args):
    asyncio.get_event_loop().create_task(commands.fun.mock(ctx, *args))

@bot.command(brief = "see how much u hate someone")
async def hate(ctx, *args):
    asyncio.get_event_loop().create_task(commands.fun.hate(ctx, *args))

@bot.command(brief = "Search for words in the dictionary")
async def dict(ctx, *args):
    asyncio.get_event_loop().create_task(commands.fun.dict(ctx, *args))
    
@bot.command(brief = "Search for words in the urban dictionary")
async def urban(ctx, *args):
    asyncio.get_event_loop().create_task(commands.fun.urban(ctx, *args))
    
@bot.command(brief = "Rock Paper & Scissors")
async def rps(ctx, arg):
    asyncio.get_event_loop().create_task(commands.fun.rps(ctx, arg))
    
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
    asyncio.get_event_loop().create_task(commands.genshin.wishes(ctx, prefix, arg))

@bot.command(brief = "Crit Value Calculator [crit rate * 2 + crit damage]")
async def cvc(ctx, *args):
    asyncio.get_event_loop().create_task(commands.genshin.cvc(ctx, prefix, *args))
    
@bot.command(brief = "Ascension Mats Today")
async def asct(ctx):
    asyncio.get_event_loop().create_task(commands.genshin.asct(ctx))
    
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
    asyncio.get_event_loop().create_task(commands.mods.rolecolour(ctx, arguments, c))
    
@bot.command(brief = "Purge a number of messages from the current text channel [MODS ONLY]",
             description="purge [number of messages: default is 10]",
             aliases=["clear"])
@discord.ext.commands.has_role(719954439078936619)
async def purge(ctx, arguments = 11):
    asyncio.get_event_loop().create_task(commands.mods.purge(ctx, arguments))
    
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
    asyncio.get_event_loop().create_task(commands.admin.fm(ctx, bot, *args))

@bot.command(brief = "Mark the status of the ticket [ADMIN ONLY]")
async def ticket(ctx, *args):
    asyncio.get_event_loop().create_task(commands.admin.ticket(ctx, bot, *args))
    
@bot.command(brief = "Give Levicoins [ADMIN ONLY]")
async def givemoney(ctx, *args):
    asyncio.get_event_loop().create_task(commands.admin.givemoney(ctx, *args))
    
with open('./json/TOKENS.json') as f:
        data = json.load(f)
        bot.run(data[whotorun])
        
# FOR EACH CHANNEL
#
#    for channel in ctx.guild.text_channels:
#        await channel.set_permissions(ctx.guild.get_role(1088420997226565652), view_channel=False)