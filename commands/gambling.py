import random

async def slots(ctx):
    fruits = ['🍎', '🍊', '🍋',
              '🍌', '🍓', '🍒',
              '🍑', '🍍', '🥥']
    
    slots = []
    for i in range(3):
        slots.append(random.choice(fruits))
        
    if slots[0] == slots[1] and slots[1] == slots[2]:
        await ctx.send(f"🎰: {' '.join(slots)}\n**Congratulations**", reference=ctx.message)
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        await ctx.send(f"🎰: {' '.join(slots)}\n**You were so close**", reference=ctx.message)
    else:
        await ctx.send(f"🎰: {' '.join(slots)}\n**Maybe next time**", reference=ctx.message)