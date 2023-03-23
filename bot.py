import discord
from discord.ext import commands
from discord import app_commands
import json
from threading import Thread
import asyncio
from datetime import datetime

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

# RUN RUN RUN RUN RUN
whotorun = "beta"
# beta / bot

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

prefix = '?'
botactivity = "ur mom"

if whotorun == "bot":
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
    
@bot.event
async def on_message_edit(before, after):
    if before.author.bot: return
    
    embed = discord.Embed(title = f"Message edited in #{before.channel.name} ({before.id})",
                          description = f"Before: **{before.content}** \n\nAfter: **{after.content}**",
                          color = discord.Color.blurple())
    embed.set_footer(text=f"{before.author.name}#{before.author.discriminator } ({before.author.id}) | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    Logchannel = bot.get_channel(484331277164740620)
    await Logchannel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    
    embed = discord.Embed(title = f"Message deleted in #{message.channel.name} ({message.id})",
                          description = f"**{message.content}**",
                          color = discord.Color.blurple())
    embed.set_footer(text=f"{message.author.name}#{message.author.discriminator } ({message.author.id}) | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    Logchannel = bot.get_channel(484331277164740620)
    await Logchannel.send(embed=embed)
                                     
                                     
############################################################################################################
                             
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
    await ctx.send("xLevia v2.1.5")

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
        
# FOR EACH CHANNEL
#
#    for channel in ctx.guild.text_channels:
#        await channel.set_permissions(ctx.guild.get_role(1088420997226565652), view_channel=False)