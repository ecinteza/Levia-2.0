import asyncio
from threading import Thread
import random
import time
# 18 RED, 18 BLACK

bettedcolour = {}
bettednumber = {}
bindedchannel = ""
run = 0

async def roulette_thr(message):
    if not message.author.id in bettedcolour and message.channel.id == bindedchannel:
        try:
            args = message.content.lower().split(" ")
            if args[0] == "bet":
                number = args[1]
                colour = args[2]
                bettednumber[message.author.id] = int(number)
                bettedcolour[message.author.id] = colour
                await message.channel.send(f"**{message.author.name}** placed on **{number} {colour}**")
        except Exception as e:
            await message.channel.send(f"Error occured```{e}```")
    
async def roulette(ctx):
    global bindedchannel
    global run
    
    if run == 0:
        run = 1
        seclefts = 15
        msg = await ctx.send(f"Place your bets folks! You have **{seclefts}** seconds.\n`bet [1-36] [red/black]`")
        bindedchannel = ctx.channel.id
        
        wincolour = random.choice(["black", "red"])
        wininterval = random.randint(1, 31)
        
        for i in range(3):
            await asyncio.sleep(5)
            seclefts -= 5
            await msg.edit(content=f"Place your bets folks! You have **{seclefts}** seconds.")
            
        
        winnercolour = [k for k, v in bettedcolour.items() if v == wincolour]
        winnernumber = [k for k, v in bettednumber.items() if v >= wininterval and v<=wininterval+5]
        winners = []
        for userid in bettednumber:
            if userid in winnercolour and userid in winnernumber:
                winners.append(ctx.message.guild.get_member(userid).name)
        win_message = f"Won: **[{wininterval}-{wininterval+5}] {wincolour}**\n**Winners:** {', '.join(winners) if len(winners)>0 else 'no winners'}"
        await ctx.send(win_message)
        bettedcolour.clear()
        bettednumber.clear()
        bindedchannel = ""
        run = 0
    else:
        await ctx.send("Game already commencing.")
    