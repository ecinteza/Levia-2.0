import random

guaranteedWin = random.randint(25, 50)
untilGuaranteed = 0
fruits = ['🍏', '🍎', '🍐', '🍊', '🍋',
          '🍌', '🍉', '🍇', '🫐', '🍅',
          '🥝', '🥥', '🍍', '🥭', '🍑',
          '🍒', '🍈', '🍓', '🌶️', '🌽',
          '⭐', '🍆', '🥑', '🥦', '🥬']

def find_duplicates(lst):
    multiplier = 0
    count_dict = {}
    
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

        if item == '⭐':
            multiplier += 1

    duplicates = []
    
    for item, count in count_dict.items():
        if count > 1:
            duplicates.append((item, count))

    for item in count_dict:
        if count_dict[item] == 2:
            multiplier += 2
        elif count_dict[item] == 3:
            multiplier += 5
        elif count_dict[item] == 5:
            multiplier += 10
            break
    
    return multiplier

async def slots(ctx, betmoney, cursor):

    global guaranteedWin
    global untilGuaranteed
    
    try:
        cursor.execute(f"SELECT coins FROM users WHERE id = {ctx.author.id}")
        result = cursor.fetchone()
        coins = int(result[0])

        if betmoney.lower() == "all":
            betmoney = coins
        
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
            for i in range(5):
                slots.append(random.choice(fruits))
        else:
            untilGuaranteed = 0
            fru = random.choice(fruits)
            for i in range(5):
                slots.append(fru)
            
        multiplier = find_duplicates(slots)

        if multiplier == 0:
            await ctx.send(f"🎰: {' '.join(slots)}\n**No win**", reference=ctx.message)
            return
        else:
            await ctx.send(f"🎰: {' '.join(slots)}\n**Win (x{multiplier})**", reference=ctx.message)
            cursor.execute(f"UPDATE users SET coins = {coins+(int(betmoney)*multiplier)} WHERE id = {ctx.author.id}")
    except Exception as e:
        await ctx.send(f"Error occured. ```{e}```")