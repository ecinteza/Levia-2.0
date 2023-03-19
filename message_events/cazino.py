import asyncio
from threading import Thread
import random
import time
# 18 RED, 18 BLACK

betted = {}
bindedchannel = ""

async def roulette_thr(message):
    if not message.author.id in betted and message.channel.id == bindedchannel:
        if (message.content.lower() == "red"):
            betted[message.author.id] = "red"
            await message.channel.send("**" + message.author.name + "** bet placed on red.")
        elif (message.content.lower() == "black"):
            betted[message.author.id] = "black"
            await message.channel.send("**" + message.author.name + "** bet placed on black.")
    
async def roulette(ctx):
    global bindedchannel
    
    await ctx.send("Place your bets folks! You have 60 seconds. [**red**/**black**]")
    bindedchannel = ctx.channel.id
    win = random.choice(["black", "red"])
    await asyncio.sleep(60)
    
    winnersids = [k for k, v in betted.items() if v == win]
    winners = []
    for userid in winnersids:
        winners.append(ctx.message.guild.get_member(userid).name)
    win_message = f"Lucky colour: **{win}**\n**Winners:** {', '.join(winners) if len(winners)>0 else 'no winners'}"
    await ctx.send(win_message)
    betted.clear()
    bindedchannel = ""
    