from wordhoard import Definitions
import random
import requests

guessusedletters = []
guesstries = {}
guess_current_user = "NULL"

guesslist = {}
guessrun = 0
correct_word = "NULL"
guesschannelbind = 0
guesshardcore = 0

async def msg_wordle(message):
    global guesslist
    global guessrun
    global correct_word
    global guesschannelbind
    global guess_current_user
    global guesshardcore
    
    if guesschannelbind != 0 and message.channel.id == guesschannelbind and guess_current_user == "NULL" and not message.content.startswith("*"):
        guess_current_user = message.author.name
        guess = message.content.lower()
        if len(guess) == 1:
            guessed_letter = guess[0]
            
            if guessed_letter not in guessusedletters:
                guessusedletters.append(guessed_letter)
           
            if guessed_letter in list(correct_word):
                guesslist[guessed_letter] = guessed_letter
            
            wordconstruct = ""
            
            for letter in list(correct_word):
                wordconstruct += guesslist[letter]
            wordconstruct = wordconstruct.capitalize()
            
            whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\nUsed: " + str(guessusedletters).replace("'", "") + "\n> _" + message.author.name + "_"
            if guesshardcore == 1: whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\n> _" + message.author.name + "_"
            await message.channel.send(whattosend)
            
            if message.author.name not in guesstries:
                guesstries[message.author.name] = 1
            else:
                guesstries[message.author.name] += 1
            
            if wordconstruct.lower() == correct_word:
                await message.channel.send("Congratulations **" + message.author.name + "**! You have won the game! To start another game write the command again. ^^")
                guesschannelbind = 0
                guessrun = 0
                guesshardcore = 0
                
                definition = Definitions(correct_word)
                defs = definition.find_definitions()
                defs = str(defs).replace("[", "").replace("]", "").replace("'", "")
                await message.channel.send("Definition: **" + defs + "**")
                
                if len(guesstries)>0:
                    guesslb = ""
                    for user in guesstries.keys():
                        guesslb += "**" + user + "** tried **" + str(guesstries[user]) + "** times\n"
                    
                    await message.channel.send("**Tries leaderboard:**\n\n" + guesslb)
                    guesstries.clear()
                guesslist.clear()
                guessusedletters.clear()
        else:
            if guess == correct_word:
                await message.channel.send("Congratulations **" + message.author.name + "**! You have won the game! To start another game write the command again. ^^")
                guesschannelbind = 0
                guessrun = 0
                guesshardcore = 0
                
                definition = Definitions(correct_word)
                defs = definition.find_definitions()
                defs = str(defs).replace("[", "").replace("]", "").replace("'", "")
                await message.channel.send("Definition: **" + defs + "**")
                
                if len(guesstries)>0:
                    guesslb = ""
                    for user in guesstries.keys():
                        guesslb += "**" + user + "** tried **" + str(guesstries[user]) + "** times\n"
                    
                    await message.channel.send("**Tries leaderboard:**\n\n" + guesslb)
                    guesstries.clear()
                guesslist.clear()
                guessusedletters.clear()
            else:
                wordconstruct = ""
                for letter in list(correct_word):
                    wordconstruct += guesslist[letter]
                wordconstruct = wordconstruct.capitalize()
                
                whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\nUsed: " + str(guessusedletters).replace("'", "") + "\n> _" + message.author.name + "_"
                if guesshardcore == 1: whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\n> _" + message.author.name + "_"
                await message.channel.send(whattosend)

                if message.author.name not in guesstries:
                    guesstries[message.author.name] = 1
                else:
                    guesstries[message.author.name] += 1
        guess_current_user = "NULL"
        
async def wordle(ctx):
    global guesslist
    global guessrun
    global correct_word
    global guesschannelbind
    global guesshardcore
    
    if guessrun == 0:
        guessrun = 1
        
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        correct_word = random.choice(WORDS)
        correct_word = correct_word.decode('UTF-8')
        
        if "hardcore" in ctx.message.content.lower():
            while(len(correct_word)<10):
                correct_word = random.choice(WORDS)
                correct_word = correct_word.decode('UTF-8')
            guesshardcore = 1
    
        for letter in correct_word:
            guesslist[letter] = "-"
            
        wordconstruct = ""
        for letter in list(correct_word):
            wordconstruct += guesslist[letter]
        wordconstruct = wordconstruct.capitalize()
        
        await ctx.send("Game started and binded in <#" + str(ctx.channel.id) + ">.")
        await ctx.send("Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**")
        
        guesschannelbind = ctx.channel.id
    else:
        await ctx.send("Game commencing in <#" + str(guesschannelbind) + ">!")