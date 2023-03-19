import json
from datetime import date
import discord

async def wishes(ctx, prefix, arg):
    msg = arg
    if msg.isnumeric():
        if int(msg)>=160:
            await ctx.send("You have **{0} wishes**.".format(round(int(msg)//160)))
        else:
            await ctx.send("You do not have any wishes.")
    else:
        await ctx.send("Correct usage: {0}wishes number_of_primogems".format(prefix))

async def cvc(ctx, prefix, *args):
    if len(args)==2:
        try:
            calc = [args[0], args[1]]
            cr = calc[0]
            cd = calc[1]
            cvcval = float(cr)*2+float(cd)
            cvctype = ""
            if cvcval >= 0 and cvcval < 10:
                cvctype = "No upgrades"
            elif cvcval >= 10 and cvcval < 20:
                cvctype = "Average"
            elif cvcval >= 20 and cvcval < 30:
                cvctype = "Decent"
            elif cvcval >= 30 and cvcval < 40:
                cvctype = "Very good"
            elif cvcval >= 40 and cvcval < 50:
                cvctype = "Jewel"
            elif cvcval >= 50:
                cvctype = "Unicorns don't exist"
            await ctx.send("The crit value is **{0} ({1})**".format(cvcval, cvctype))
        except:
            await ctx.send("Something went wrong...")
    else:
        await ctx.send("Correct usage: {0}cvc crvalue cdvalue".format(prefix))
        
async def asct(ctx):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    with open('ascension.json') as f:
        data = json.load(f)
        await ctx.send(file=discord.File(data[days[date.today().weekday()]]))