import discord
from datetime import datetime
import json
import mysql.connector

async def balance(ctx, myconn, cursor):
    cursor.execute(f"SELECT * FROM users WHERE id = {ctx.author.id}")
    result = cursor.fetchall()
    if (len(result)==0):
        cursor.execute(f"INSERT INTO users (id, coins) VALUES ({ctx.author.id}, 0)")
        await ctx.send("You weren't in my Levicoins database. I have added you now", reference = ctx.message)
    else:
        cursor.execute(f"SELECT coins FROM users WHERE id = {ctx.author.id}")
        result = cursor.fetchone()
        await ctx.send("You have exactly **" + str(result[0]) + " Levicoins**.", reference = ctx.message)
    myconn.commit()
    
async def donate(ctx, howmuch, myconn, cursor):
    try:
        cursor.execute(f"SELECT coins FROM users WHERE id = {ctx.author.id}")
        result = cursor.fetchone()
        yourcoins = int(result[0])
        howmuch = int(howmuch)
        
        if yourcoins < howmuch:
            await ctx.send("You don't have that much money, poor you lol")
            return
        
        if howmuch <= 0:
            await ctx.send("Haha, you're in debt?")
            return
        
        if len(ctx.message.mentions) == 1:
            mentioned = ctx.message.mentions[0]
            if mentioned.id == ctx.author.id:
                await ctx.send("Are you venin to be trying this?")
            else:
                cursor.execute(f"SELECT coins FROM users WHERE id = {mentioned.id}")
                result = cursor.fetchone()
                theircoins = int(result[0])
                cursor.execute(f"UPDATE users SET coins = {theircoins+howmuch} WHERE id = {mentioned.id}")
                cursor.execute(f"UPDATE users SET coins = {yourcoins-howmuch} WHERE id = {ctx.author.id}")
                myconn.commit()
                await ctx.send(f"Donated **{howmuch}** levicoins to **{mentioned.name}**")
        else:
            await ctx.send("Donate to who? me?")
    except Exception as e:
        await ctx.send(f"This went horribly... ```{e}```")