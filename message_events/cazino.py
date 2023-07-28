import asyncio
import random
import json
import mysql.connector
# 18 RED, 18 BLACK

bettedcolour = {}
bettednumber = {}
bindedchannel = ""
run = 0
moneybet = 0

async def roulette_thr(message):
    f = open('./json/DB.json')
    data = json.load(f)
    myconn = mysql.connector.connect(host = data["endpoint"],
                                    port = data["port"],
                                    user = data["username"],
                                    password = data["password"],
                                    database = data["database"])
    cursor = myconn.cursor()

    if not message.author.id in bettedcolour and message.channel.id == bindedchannel:
        try:
            args = message.content.lower().split(" ")
            if args[0] == "bet":
                cursor.execute(f"SELECT coins FROM users WHERE id = {message.author.id}")
                result = cursor.fetchone()
                coins = int(result[0])
                if coins < moneybet:
                    await message.channel.send("You do not have enough money to bet.")
                    return
                number = args[1]
                colour = args[2]
                bettednumber[message.author.id] = int(number)
                bettedcolour[message.author.id] = colour
                cursor.execute(f"UPDATE users SET coins = {coins-moneybet} WHERE id = {message.author.id}")
                await message.channel.send(f"**{message.author.name}** placed on **{number} {colour}**")
                await message.delete()
        except Exception as e:
            await message.channel.send(f"Error occured```{e}```")

    myconn.commit()
    cursor.close()
    myconn.close()
    f.close()
    
async def roulette(ctx, betmoney):
    global bindedchannel
    global run
    global moneybet
    
    if run == 0:

        f = open('./json/DB.json')
        data = json.load(f)
        myconn = mysql.connector.connect(host = data["endpoint"],
                                        port = data["port"],
                                        user = data["username"],
                                        password = data["password"],
                                        database = data["database"])
        cursor = myconn.cursor()
        moneybet = int(betmoney)
        
        if moneybet <= 0:
            await ctx.send("Really?", reference = ctx.message)
            return
        
        run = 1
        seclefts = 15
        msg = await ctx.send(f"Place your bets folks, hopefully you have **{moneybet} Levicoins**!\nYou have **{seclefts}** seconds.\n`bet [1-36] [red/black]`")
        bindedchannel = ctx.channel.id
        
        wincolour = random.choice(["black", "red"])
        wininterval = random.randint(1, 31)
        
        for i in range(3):
            await asyncio.sleep(5)
            seclefts -= 5
            await msg.edit(content=f"Place your bets folks! You have **{seclefts}** seconds.")
        await msg.edit(content="No more bets allowed.")
            
        
        winnercolour = [k for k, v in bettedcolour.items() if v == wincolour]
        winnernumber = [k for k, v in bettednumber.items() if v >= wininterval and v<=wininterval+5]
        winners = []
        winnersids = []
        for userid in bettednumber:
            if userid in winnercolour and userid in winnernumber:
                winners.append(ctx.message.guild.get_member(userid).name)
                winnersids.append(userid)
        win_message = f"Won: **[{wininterval}-{wininterval+5}] {wincolour}**\n**Winners:** {', '.join(winners) if len(winners)>0 else 'no winners'}"
        await ctx.send(win_message)
        if len(winnersids) > 0:
            for id in winnersids:
                cursor.execute(f"SELECT coins FROM users WHERE id = {id}")
                result = cursor.fetchone()
                coins = int(result[0])
                cursor.execute(f"UPDATE users SET coins = {coins+moneybet*10} WHERE id = {id}")
        bettedcolour.clear()
        bettednumber.clear()
        bindedchannel = ""
        run = 0

        myconn.commit()
        cursor.close()
        myconn.close()
        f.close()
    else:
        await ctx.send("Game already commencing.")
    