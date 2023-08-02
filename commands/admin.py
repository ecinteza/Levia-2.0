import discord
from datetime import datetime

async def fm(ctx, bot, *args):
    if ctx.message.author.id != 255432828668477441:
        await ctx.send("You wish you could use this, don't u?")
        return
    try:
        channel = bot.get_channel(int(args[0]))
        messages = ""
        i = 0
        async for message in channel.history(limit=int(args[2])):
            if message.author.id == int(args[1]):
                messages += message.author.name + ": " + message.content + "\n"
                if i==5:
                    await ctx.channel.send(messages)
                    messages=""
                    i = 0
                i += 1
        if i != 0:
            await ctx.channel.send(messages)
    except Exception as e:
        await ctx.send(f"Well, for some reason it did not work. ```{e}```")
        
async def ticket(ctx, bot, *args):
    if ctx.message.author.id != 255432828668477441:
        await ctx.send("You wish you could use this, don't u?")
        return
    response = " ".join(args)
    if ctx.message.reference is not None:
        msg = await ctx.fetch_message(ctx.message.reference.message_id)
        
        date = str(datetime.now()).split(".")[0]
        
        if "fixed" in response.lower() or "implemented" in response.lower():
            done = bot.get_channel(1087036132937715842)
            embed = discord.Embed(title = msg.embeds[0].title,
                          description = f"{msg.embeds[0].description}\n**{ctx.author.name}** at **{date}** `>>` **{response}**",
                          color = discord.Color.dark_green())
            await ctx.message.delete()
            await msg.delete()
            await done.send(embed=embed)
            return
        elif "approved" in response.lower():
            embed = discord.Embed(title = msg.embeds[0].title,
                          description = f"{msg.embeds[0].description}\n**{ctx.author.name}** at **{date}** `>>` **{response}**",
                          color = discord.Color.brand_green())
        elif "denied" in response.lower():
            rejected = bot.get_channel(1087037594505838702)
            embed = discord.Embed(title = msg.embeds[0].title,
                          description = f"{msg.embeds[0].description}\n**{ctx.author.name}** at **{date}** `>>` **{response}**",
                          color = discord.Color.dark_red())
            await ctx.message.delete()
            await msg.delete()
            await rejected.send(embed=embed)
            return
        else:
            embed = discord.Embed(title = msg.embeds[0].title,
                          description = f"{msg.embeds[0].description}\n**{ctx.author.name}** at **{date}** `>>` **{response}**",
                          color = discord.Color.dark_gold())
        
        await ctx.message.delete()
        await msg.delete()
        await ctx.send(embed=embed)
        
async def givemoney(ctx, cursor, *args):

    if ctx.message.author.id != 255432828668477441:
        await ctx.send("You wish you could use this, don't u?")
        return
    
    try:
        userid = args[0]
        money = int(args[1])
        
        cursor.execute(f"SELECT coins FROM users WHERE id = {userid}")
        result = cursor.fetchone()
        coins = int(result[0])
        
        cursor.execute(f"UPDATE users SET coins = {coins+money} WHERE id = {userid}")
    except Exception as e:
        await ctx.send(f"Error occured. ```{e}```")