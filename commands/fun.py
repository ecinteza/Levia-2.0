import random
from wordhoard import Definitions
import requests
import json

def get_gif(searchTerm):  
    f = open('./json/TOKENS.json')
    Tokens = json.load(f)
    f.close()

    response = requests.get(f"https://g.tenor.com/v2/search?q={searchTerm}&key={Tokens['tenorapi']}&client_key=Levia&limit=50")
    data = response.json()
        
    gif = random.choice(data["results"])
    return gif['media_formats']['gif']['url']

async def jail(ctx):
    ref = ctx.message.reference

    if ref:
        refmsg = await ctx.fetch_message(ref.message_id)
        refauthor = refmsg.author

        if (refauthor.id == ctx.message.author.id):
            await ctx.send("You can't jail yourself, silly!", reference=ctx.message)
            return
        
        if (refauthor.bot):
            await ctx.send("Bots don't do jailtime, that's for stupid humans, like you, that just tried to jail a bot.", reference=ctx.message)
            return
        
        if (refmsg.content == ""):
            await ctx.send("You can't jail someone for not saying anything, stupid.", reference=ctx.message)
            return
        
        await ctx.message.delete()
        await ctx.send(f"{refauthor.mention} is now in jail for **{random.randint(1, 76)} months** for saying **{refmsg.content}**.\nCrime reported by {ctx.author.mention}.")
        await ctx.send(get_gif("jail"))
    else:
        await ctx.send("Hm?", reference=ctx.message)

async def mock(ctx, *args):
    if len(args) < 1:
        await ctx.send("Mock what? lol")
        return
    msg = " ".join(args)
    mockmsg = ""
    for i in range(0, len(msg)):
        if i%2==0:
            mockmsg += msg[i].upper()
        else:
            mockmsg += msg[i].lower()
    mockmsg += f"\n*(mocked by {ctx.author.name})*"
    await ctx.send(mockmsg)

async def penis(ctx):
    peen = "8"
    
    if ctx.author.id == 246213412059611136 and not ctx.message.mentions:
        await ctx.send("Girlboss, we know you have no peen.", reference = ctx.message)
        return
    
    bigchance = random.randint(1, 100)
    
    if bigchance > 0 and bigchance <= 2:
        length = random.randint(36, 40)
    elif bigchance > 2 and bigchance <= 10:
        length = random.randint(30, 35)
    elif bigchance >10 and bigchance <= 30:
        length = random.randint(20, 29)
    elif bigchance >30 and bigchance <= 60:
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
    
async def pussy(ctx):
    pusay = "({"
    
    bigchance = random.randint(1, 100)
    
    if bigchance > 0 and bigchance <= 2:
        length = random.randint(0, 9)
    elif bigchance > 2 and bigchance <= 10:
        length = random.randint(10, 19)
    elif bigchance >10 and bigchance <= 30:
        length = random.randint(20, 29)
    elif bigchance >30 and bigchance <= 60:
        length = random.randint(30, 35)
    else:
        length = random.randint(36, 40)
    
    for i in range(length):
        pusay += " "
    else:
        pusay += "}) (" + str(length) + " cm)"
    
    mesaj = ""
    if ctx.message.mentions:
        mentioned = ctx.message.mentions[0]
        mesaj = mentioned.name + "'s pusay is "
    else:
        mesaj = "Your pusay (" + ctx.author.name + ") is "
        
    if (length == 0):
        if ctx.message.mentions:
            mesaj = mentioned.name + " isn't dilated. Hah, Virgin."
        else:
            mesaj = "You aren't dilated, you virgin."
        pusay = ""
    
    await ctx.send(mesaj + pusay)

loveurself = [
    "Do that in your bed, not in public",
    "Wow, you're so narcissistic..."
]

async def love(ctx, *args):
    gif = ""
    if len(ctx.message.mentions) == 1:
        mentioned = ctx.message.mentions[0]
        if str(mentioned.id) != '413335791272460288':
            if mentioned.id == ctx.author.id:
                await ctx.channel.send(random.choice(loveurself), reference=ctx.message)
            else:
                love = random.randint(0, 100)
                lovemsg = ctx.author.name + " & " + mentioned.name + " > " + str(love) + "% ❤️"
                if (love > 50):
                    gif = get_gif("love")
                else:
                    gif = get_gif("hate")
                await ctx.channel.send(lovemsg)
        else:
            await ctx.channel.send("I only love k4tz losers.")
    elif len(ctx.message.mentions) == 2:
        mentioned = ctx.message.mentions[0]
        mentioned_inlove = ctx.message.mentions[1]
        
        love = random.randint(0, 100)
        lovemsg = mentioned.name + " & " + mentioned_inlove.name + " > " + str(love) + "% ❤️"
        if (love > 50):
            gif = get_gif("love")
        else:
            gif = get_gif("hate")
        await ctx.channel.send(lovemsg)
    else:
        if len(args) > 0:
            arguments = " ".join(args)
            love = random.randint(0, 100)
            lovemsg = ctx.author.name + " & " + arguments + " > " + str(love) + "% ❤️"
            if (love > 50):
                gif = get_gif("love")
            else:
                gif = get_gif("hate")
            await ctx.channel.send(lovemsg)
        else:
            await ctx.channel.send("Are you that lonely?")
            gif = get_gif("lonely")
    await ctx.channel.send(gif)

async def smash(ctx, *args):
    whatkind = ["smash", "smashing", "sex", "boner", "ass", "butt",
                "orgy", "hentai", "gay", "yaoi", "yuri",
                "lesbian", "hitting", "punching", "kick",
                "kiss", "lick", "touch", "throw", "anger"]
    gif = get_gif(random.choice(whatkind))

    if len(ctx.message.mentions) == 1:
        mentioned = ctx.message.mentions[0]
        if str(mentioned.id) != '413335791272460288':
            if mentioned.id == ctx.author.id:
                await ctx.channel.send("If you're THIS lonely, I'll pity smash you ig", reference=ctx.message)
                await ctx.channel.send(get_gif("pity"))
            else:
                smashmsg = "**" + ctx.author.name + "** smashed **" + mentioned.name + "**"
                await ctx.channel.send(smashmsg)
                await ctx.channel.send(gif)
        else:
            await ctx.channel.send("Nu-huh.")
    elif len(ctx.message.mentions) == 2:
        mentioned = ctx.message.mentions[0]
        mentioned_inlove = ctx.message.mentions[1]
        
        smashmsg = "**" + mentioned.name + "** smashed **" + mentioned_inlove.name + "**"
        await ctx.channel.send(smashmsg)
        await ctx.channel.send(gif)
    else:
        if len(args) > 0:
            arguments = " ".join(args)
            smashmsg = "**" + ctx.author.name + "** smashed **" + arguments + "**"
            await ctx.channel.send(smashmsg)
            await ctx.channel.send(gif)
        else:
            await ctx.channel.send("Really?")
            
hateurself = [
    "Wow, you should see a therapist...",
    "Why would you hate yourself?"
]
async def hate(ctx, *args):
    gif = ""
    if len(ctx.message.mentions) == 1:
        mentioned = ctx.message.mentions[0]
        if str(mentioned.id) != '413335791272460288':
            if mentioned.id == ctx.author.id:
                await ctx.channel.send(random.choice(hateurself), reference=ctx.message)
            else:
                hate = random.randint(0, 100)
                hatemsg = ctx.author.name + " & " + mentioned.name + " > " + str(hate) + "% 💔"
                if (hate > 50):
                    gif = get_gif("hate")
                else:
                    gif = get_gif("friend")
                await ctx.channel.send(hatemsg)
        else:
            await ctx.channel.send("I hate you very much, yes.")
    elif len(ctx.message.mentions) == 2:
        mentioned = ctx.message.mentions[0]
        mentioned_inhate = ctx.message.mentions[1]
        
        hate = random.randint(0, 100)
        hatemsg = mentioned.name + " & " + mentioned_inhate.name + " > " + str(hate) + "% 💔"
        if (hate > 50):
            gif = get_gif("hate")
        else:
            gif = get_gif("friend")
        await ctx.channel.send(hatemsg)
    else:
        if len(args) > 0:
            arguments = " ".join(args)
            hate = random.randint(0, 100)
            hatemsg = ctx.author.name + " & " + arguments + " > " + str(hate) + "% 💔"
            if (hate > 50):
                gif = get_gif("hate")
            else:
                gif = get_gif("friend")
            await ctx.channel.send(hatemsg)
        else:
            await ctx.channel.send("Hm?")
            gif = get_gif("stupid")
    await ctx.channel.send(gif)
            
async def dict(ctx, *args):
    try:
        search = " ".join(args)
        definition = Definitions(search)
        defs = definition.find_definitions()
        defs = str(defs).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace("38;2;255;255;255m", "").replace("38;2;255;0;255m", "") #lazy
        await ctx.send(defs, reference=ctx.message)
    except:
        await ctx.send("Are you this stupid that you can't use a command this simple?")

def loadwordurban(term):
    url = f"https://api.urbandictionary.com/v0/define?term={term}"
    response = requests.get(url)
    return response.text

async def urban(ctx, *args):
    try:
        term = " ".join(args)
        
        data = json.loads(loadwordurban(term))
        msg = data["list"][random.randint(0, len(data["list"])-1)]['definition']
        msg = msg.replace("[", "**[").replace("]", "]**")
        await ctx.send(msg, reference=ctx.message)
    except Exception as e:
        await ctx.send(f"Error occured. ```{e}```")
        
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