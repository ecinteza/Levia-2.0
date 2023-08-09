import random
from commands.utils import remove_mentions, detect_link
# ignoring warning because it actually works

replyusers = []
msg = "NULL"
msgtogoogle = "NULL"

async def wys(message):
    if " 727 " in message.content.lower() or "727 " in message.content.lower() or " 727" in message.content.lower() or message.content == "727":
        await message.channel.send("WYSI!! 👈 😱")

    if " crazy " in message.content.lower() or "crazy " in message.content.lower() or " crazy" in message.content.lower() or message.content == "crazy":
        await message.channel.send("Crazy? I was crazy once. They locked me in a room, a rubber room... a rubber room with rats... and rats make me crazy.", reference=message)

    if " gay " in message.content.lower() or "gay " in message.content.lower() or " gay" in message.content.lower() or message.content == "gay":
        await message.channel.send("Gay? I was gay once. They locked me in a room, a rainbow room... a rainbow room with person kissers... and person kissers make me gay.", reference=message)

async def reply3(message):
    global replyusers
    global msg
    global msgtogoogle
    
    msgtogoogle = message.content
    
    if message.content == msg:
        if message.author.id not in replyusers:
            replyusers.append(message.author.id)
            
        if len(replyusers) == 3:
            await message.channel.send(msg)
            replyusers.clear()
    else:
        msg = message.content
        replyusers.clear()
        replyusers.append(message.author.id)
        
async def mocking(message, mockguaranteed):
    if message.channel.id == 1089635395278475295: return
    if detect_link(message) == True: return
    
    if mockguaranteed:
        mockmsg = ""
        for i in range(0, len(message.content)):
            if i%2==0:
                mockmsg += message.content[i].upper()
            else:
                mockmsg += message.content[i].lower()
        await message.channel.send(mockmsg)
    else:
        mock = random.randint(1, 200)

        mockmsg = ""
        if mock==1:
            for i in range(0, len(message.content)):
                if i%2==0:
                    mockmsg += message.content[i].upper()
                else:
                    mockmsg += message.content[i].lower()
            await message.channel.send(mockmsg)
        

async def idk(ctx, *args):
    search = ""
    ok = 1
    if len(args) > 1:
        try:
            msg = await ctx.fetch_message(int(args[0][0]))
            mesaj = remove_mentions(msg.content)
            
            search = mesaj.replace(" ", "+")
        except Exception as e:
            ok = 0
            await ctx.send(f"Invalid ID? Idk but something went wrong.")
    else:
        if ctx.message.reference is not None:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
            mesaj = remove_mentions(msg.content)
            
            search = mesaj.replace(" ", "+")
        else:
            search = msgtogoogle.replace(" ", "+")  
    
    if ok:
        while "++" in search:
            search = search.replace("++", "+")
        await ctx.send('<https://letmegooglethat.com/?q=' + search + '>')