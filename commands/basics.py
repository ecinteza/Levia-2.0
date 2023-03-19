import os
from PIL import Image
from colorthief import ColorThief
import requests
import discord
import random
import aiohttp
from discord import Webhook
from datetime import datetime

from . import utils

async def ping(ctx, bot):
    await ctx.send(f'My ping is {bot.latency}!')
    
async def pfphex(ctx):
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        
        img_url = mentioned.avatar
        img = Image.open(requests.get(img_url, stream = True).raw)
        pic = str(mentioned.id) + 'leviapfphex.png'
        img.save(pic)
    
        color_thief = ColorThief(pic)
        dominant_color = color_thief.get_color(quality=1)

        embed = discord.Embed(title = '#' + utils.rgb_to_hex(dominant_color),
                              color = int(utils.rgb_to_hex(dominant_color), 16))

        await ctx.channel.send(embed=embed)
    
        os.remove(pic)
    else:
        img_url = ctx.message.author.avatar
        img = Image.open(requests.get(img_url, stream = True).raw)
        pic = str(ctx.author.id) + 'leviapfphex.png'
        img.save(pic)
    
        color_thief = ColorThief(pic)
        dominant_color = color_thief.get_color(quality=1)
    
        embed = discord.Embed(title = '#' + utils.rgb_to_hex(dominant_color),
                              color = int(utils.rgb_to_hex(dominant_color), 16))
    
        await ctx.channel.send(embed=embed)
    
        os.remove(pic)
        
async def poll(ctx, *args):
    if len(args)==0:
        await ctx.send("No poll specified")
        return
    
    titlu = " ".join(args)
    titlu = utils.remove_mentions(titlu)
    
    if len(titlu)==0:
        await ctx.send("No poll specified")
        return
    
    embed = discord.Embed(title = titlu,
                          description = "Started by " + ctx.message.author.name + " / " + str(ctx.message.author.id),
                          color = int("%06x" % random.randint(0, 0xFFFFFF), 16))
    
    await ctx.message.delete()
    msg = await ctx.send(embed=embed)
    agree = discord.utils.get(ctx.guild.emojis, id = 709744862722785360)
    disagree = discord.utils.get(ctx.guild.emojis, id = 709744862458806353)
    await msg.add_reaction(agree)
    await msg.add_reaction(disagree)
    
async def suggest(ctx, bot, *args):
    if len(args)==0:
        await ctx.send("No suggestion specified")
        return
    
    suggestion = " ".join(args)
    suggestion = utils.remove_mentions(suggestion)
    user = ctx.author.name + " (" + str(ctx.author.id) + ")"
    
    date = str(datetime.now()).split(".")[0]
    embed = discord.Embed(title = user,
                          description = f"Suggestion: **{suggestion}**\nSuggested at: **{date}**",
                          color = discord.Color.blue())
    
    await ctx.message.delete()
    
    channel = bot.get_channel(720019874726019073)
    msg = await channel.send(embed=embed)
    agree = discord.utils.get(ctx.guild.emojis, id = 709744862722785360)
    disagree = discord.utils.get(ctx.guild.emojis, id = 709744862458806353)
    await msg.add_reaction(agree)
    await msg.add_reaction(disagree)
    
async def hex(ctx, *args):
    if len(args)==0:
        await ctx.send("No hex specified")
        return
    try:
        titlu = "".join(args)
        titlu = titlu.replace("#", "")
    
        embed = discord.Embed(title = "#" + titlu,
                          color = int(titlu, 16))
    
        await ctx.send(embed = embed)
    
    except:
        await ctx.send("Either I'm dumb (not likely) or you haven't used the command properly (most probably)")

async def pfphexpal(ctx):
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        
        img_url = mentioned.avatar
        img = Image.open(requests.get(img_url, stream = True).raw)
        pic = str(mentioned.id) + 'leviapfphexpal.png'
        img.save(pic)

        color_thief = ColorThief(pic)
        palette = color_thief.get_palette(color_count=5)
        embeds = []
        for i in range(5):
            embed = discord.Embed(title = '#' + utils.rgb_to_hex(palette[i]),
                              color = int(utils.rgb_to_hex(palette[i]), 16))
            embeds.append(embed)
        
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/1081724666240045207/7rhpOhmBMUtcwHbN9Rhs0Jfw3xbgOKY50STYXn8FJSDK1GAAjxYX0T6Qwi6I65aYMZUR', session=session)
            await webhook.send("**" + ctx.message.author.name + "** requested **" + mentioned.name + "'s** colour palette in <#" + str(ctx.channel.id) + ">", username="Levia's Assistant", embeds=embeds)
            if ctx.channel.id != 719967026461802516:
                await ctx.send("Check <#719967026461802516>")
            
        os.remove(pic)
    else:
        img_url = ctx.message.author.avatar
        img = Image.open(requests.get(img_url, stream = True).raw)
        pic = str(ctx.author.id) + 'leviapfphexpal.png'
        img.save(pic)
    
        color_thief = ColorThief(pic)
        palette = color_thief.get_palette(color_count=5)
        embeds = []
        for i in range(5):
            embed = discord.Embed(title = '#' + utils.rgb_to_hex(palette[i]),
                              color = int(utils.rgb_to_hex(palette[i]), 16))
            embeds.append(embed)
        
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/1081724666240045207/7rhpOhmBMUtcwHbN9Rhs0Jfw3xbgOKY50STYXn8FJSDK1GAAjxYX0T6Qwi6I65aYMZUR', session=session)
            await webhook.send("**" + ctx.message.author.name + "** requested their colour palette in <#" + str(ctx.channel.id) + ">", username="Levia's Assistant", embeds=embeds)
            if ctx.channel.id != 719967026461802516:
                await ctx.send("Check <#719967026461802516>")
            
        os.remove(pic)
        
async def avatar(ctx):
    img_url = ctx.message.author.avatar
    name = ctx.message.author.name + "'s Avatar"
    colour = ctx.message.author.accent_color
    
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        
        img_url = mentioned.avatar
        name = mentioned.name
        colour = mentioned.accent_color
    
    embed = discord.Embed(title = name,
                          color = colour)
    embed.set_image(url=img_url)

    await ctx.channel.send(embed=embed)
    
async def report(ctx, bot, *args):
    if len(args)==0:
        await ctx.send("No report specified")
        return
    
    bug = " ".join(args)
    bug = utils.remove_mentions(bug)
    user = ctx.author.name + " (" + str(ctx.author.id) + ")"
    
    if len(bug)==0:
        await ctx.send("No report specified")
        return
    
    date = str(datetime.now()).split(".")[0]
    embed = discord.Embed(title = user,
                          description = f"Bug description: **{bug}**\nFound at: **{date}**",
                          color = discord.Color.red())
    
    await ctx.message.delete()
    
    channel = bot.get_channel(1085305466009161738)
    await channel.send(embed=embed)