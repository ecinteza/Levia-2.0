import random

guaranteedWin = random.randint(10, 30)
untilGuaranteed = 0
fruits = ['🍎', '🍊', '🍋',
          '🍌', '🍓', '🍒',
          '🍑', '🍍', '🥥']

async def slots(ctx, betmoney, cursor):
    global guaranteedWin
    global untilGuaranteed
    
    try:
        cursor.execute(f"SELECT coins FROM users WHERE id = {ctx.author.id}")
        result = cursor.fetchone()
        coins = int(result[0])
        
        if coins < int(betmoney):
            await ctx.send("You do not have enough money to bet.")
            return
        
        if int(betmoney) <= 0:
            await ctx.send("Omaga, you're not like other girls, are you?", reference = ctx.message)
            return
        
        cursor.execute(f"UPDATE users SET coins = {coins-int(betmoney)} WHERE id = {ctx.author.id}")
        
        untilGuaranteed += 1
    
        slots = []
        if untilGuaranteed < guaranteedWin:
            untilGuaranteed = 0
            for i in range(3):
                slots.append(random.choice(fruits))
        else:
            fru = random.choice(fruits)
            for i in range(3):
                slots.append(fru)
            
        if slots[0] == slots[1] and slots[1] == slots[2]:
            await ctx.send(f"🎰: {' '.join(slots)}\n**Congratulations**", reference=ctx.message)
            guaranteedWin = random.randint(10, 30)
            untilGuaranteed = 0
            cursor.execute(f"UPDATE users SET coins = {coins+int(betmoney)*10} WHERE id = {ctx.author.id}")
        elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
            await ctx.send(f"🎰: {' '.join(slots)}\n**You were so close**", reference=ctx.message)
        else:
            await ctx.send(f"🎰: {' '.join(slots)}\n**Maybe next time**", reference=ctx.message)
    except Exception as e:
        await ctx.send(f"Error occured. ```{e}```")