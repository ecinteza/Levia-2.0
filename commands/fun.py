import random
from wordhoard import Definitions

async def penis(ctx):
    peen = "8"
    
    if ctx.author.id == 246213412059611136 and not ctx.message.mentions:
        await ctx.send("Girlboss, we know you have no peen.", reference = ctx.message)
        return
    
    bigchance = random.randint(0, 10000)
    
    if bigchance == 0:
        random.randint(35, 40)
    if bigchance >= 1 and bigchance <= 3:
        length = random.randint(30, 35)
    elif bigchance >=4 and bigchance <= 200:
        length = random.randint(20, 29)
    elif bigchance >= 210 and bigchance <= 500:
        length = random.randint(10, 19)
    else:
        length = random.randint(0, 9)
    
    for i in range(length):
        peen += "="
    else:
        peen += "D (" + str(length) + " cm)"
    
    mesaj = ""
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        mesaj = mentioned.name + "'s penis is "
        
        if mentioned.id == 246213412059611136:
            await ctx.send("She has no penis, bestie, get over it.", reference = ctx.message)
            return
    else:
        mesaj = "Your peen (" + ctx.author.name + ") is "
        
    if (length == 0):
        if ctx.message.mentions:
            mesaj = mentioned.name + " has no penis. Probably has a pussy."
        else:
            mesaj = "You don't have a penis. Are you sure you don't have a pussy?"
        peen = ""
    
    await ctx.send(mesaj + peen)
    
async def love(ctx, *args):
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        if str(mentioned.id) != '413335791272460288':
            love = random.randint(0, 100)
            lovemsg = ctx.author.name + " & " + mentioned.name + " > " + str(love) + "% ❤️"
            await ctx.channel.send(lovemsg)
        else:
            await ctx.channel.send("I only love k4tz losers.")
    else:
        if len(args) > 0:
            arguments = " ".join(args)
            love = random.randint(0, 100)
            lovemsg = ctx.author.name + " & " + arguments + " > " + str(love) + "% ❤️"
            await ctx.channel.send(lovemsg)
        else:
            await ctx.channel.send("Are you that lonely?")
            
async def dict(ctx, args):
    try:
        definition = Definitions(args)
        defs = definition.find_definitions()
        defs = str(defs).replace("[", "").replace("]", "").replace("'", "")
        await ctx.send(defs)
    except:
        await ctx.send("Are you this stupid that you can't use a command this simple?")
        
        
async def rps(ctx, arg):
    choices = ["rock", "paper", "scissors"]
    arg = arg.lower()
    
    choice = random.choice(choices)
    
    draw = ["Aw man, it's a draw",
            "It's a draw but we know at least I'm winning at life",
            "This is not the type of 'tied up' I was thinking of",
            "The game is a draw, but you could draw me like one of ur french girls"]
    
    win = ["YAS! Loser",
           "Better luck next time ;D",
           "I know you wish you were me",
           "How could you lose against a discord bot lol",
           "You are such a loser that you would be #2 in a Loser championship, BECAUSE UR A LOSER"]
    
    lose = ["You'll pay for this next time",
            "Damn... You're lucky ig",
            "Aw man, how dare you?",
            "If I were you I'd sleep with one eye open"]
    
    if arg=="rock":
        if choice=="rock":
            await ctx.send("Rock! " + random.choice(draw))
        elif choice=="paper":
            await ctx.send("Paper! " + random.choice(win))
        elif choice=="scissors":
            await ctx.send("Scissors... " + random.choice(lose))
    elif arg=="paper":
        if choice=="rock":
            lose.append("You may win the game, we know my rock is stronger than ur paper")
            await ctx.send("Rock! " + random.choice(lose))
        elif choice=="paper":
            await ctx.send("Paper! " + random.choice(draw))
        elif choice=="scissors":
            win.append("YES! Let's see how you protect yourself from my scissors with your little paper")
            await ctx.send("Scissors! " + random.choice(win))
    elif arg=="scissors":
        if choice=="rock":
            win.append("First your scissors, then your head")
            await ctx.send("Rock! " + random.choice(win))
        elif choice=="paper":
            await ctx.send("Paper! " + random.choice(lose))
        elif choice=="scissors":
            draw.append("If you'd be a lesbian this'd be spicier...")
            await ctx.send("Scissors! " + random.choice(draw))