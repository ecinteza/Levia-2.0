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