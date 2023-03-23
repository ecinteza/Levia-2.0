import random

guaranteedWin = random.randint(10, 30)
untilGuaranteed = 0

async def slots(ctx):
    global guaranteedWin
    global untilGuaranteed
    
    fruits = ['🍎', '🍊', '🍋',
              '🍌', '🍓', '🍒',
              '🍑', '🍍', '🥥']
    
    untilGuaranteed += 1
    
    slots = []
    if untilGuaranteed < guaranteedWin:
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
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        await ctx.send(f"🎰: {' '.join(slots)}\n**You were so close**", reference=ctx.message)
    else:
        await ctx.send(f"🎰: {' '.join(slots)}\n**Maybe next time**", reference=ctx.message)