from wordhoard import Definitions
import random
import requests
import commands.fun
import json

guessusedletters = []
guesstries = {}
guess_current_user = "NULL"

guesslist = {}
guessrun = 0
correct_word = "NULL"
guesschannelbind = 0
guesshard = 0

guesshardcore = 0
guesshardcore_letters = {}

def checkword(strin):
    for letter in strin:
        if not letter.isalpha():
            return 0
    return 1

async def msg_wordle(message):
    global guesslist
    global guessrun
    global correct_word
    global guesschannelbind
    global guess_current_user
    global guesshard
    global guesshardcore
    
    if guesschannelbind != 0 and message.channel.id == guesschannelbind and guess_current_user == "NULL":
        guess_current_user = message.author.name
        guess = message.content.lower()
        if len(guess) == 1 and guess[0].isalpha():
            guessed_letter = guess[0]
            
            if guesshard == 0 and guesshardcore == 0:
                if guessed_letter not in guessusedletters:
                    guessusedletters.append(guessed_letter)
           
            if guessed_letter in list(correct_word):
                if guesshardcore == 0:
                    guesslist[guessed_letter] = guessed_letter
                else:
                    if guessed_letter not in guesshardcore_letters:
                        guesshardcore_letters[guessed_letter] = 0
                        for letter in list(correct_word):
                            if letter == guessed_letter:
                                guesshardcore_letters[guessed_letter] += 1
                        
            
            
            wordconstruct = ""
            
            for letter in list(correct_word):
                if guesshardcore == 0:
                    wordconstruct += guesslist[letter]
                else:
                    wordconstruct += "-"
            
            wordconstruct = wordconstruct.capitalize()
            
            whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\nUsed: " + str(guessusedletters).replace("'", "") + "\n> _" + message.author.name + "_"
            if guesshard == 1: whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\n> _" + message.author.name + "_"
            elif guesshardcore == 1:
                used = ""
                for i in guesshardcore_letters.keys():
                    used += f" {i} ({guesshardcore_letters[i]}) "
                whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\nUsed: " + used + "\n> _" + message.author.name + "_"
            await message.channel.send(whattosend)
            
            if message.author.name not in guesstries:
                guesstries[message.author.name] = 1
            else:
                guesstries[message.author.name] += 1
            
            if wordconstruct.lower() == correct_word:
                the_message = "**" + message.author.name + "** won! ^^" + '\n\n'

                guesschannelbind = 0
                guessrun = 0
                guesshard = 0
                guesshardcore = 0
                
                
                if len(guesstries)>0:
                    guesslb = ""
                    for user in guesstries.keys():
                        guesslb += "**" + user + "** tried **" + str(guesstries[user]) + "** times\n"
                    
                    the_message += "**Tries leaderboard:**\n\n" + guesslb
                    guesstries.clear()
                await message.channel.send(the_message)
                guesslist.clear()
                guessusedletters.clear()
                guesshardcore_letters.clear()
        elif checkword(guess)==1:
            if guess == correct_word:
                the_message = "**" + message.author.name + "** won! ^^" + '\n\n'

                guesschannelbind = 0
                guessrun = 0
                guesshard = 0
                guesshardcore = 0
                
                if len(guesstries)>0:
                    guesslb = ""
                    for user in guesstries.keys():
                        guesslb += "**" + user + "** tried **" + str(guesstries[user]) + "** times\n"
                    
                    the_message += "**Tries leaderboard:**\n\n" + guesslb
                    guesstries.clear()
                    
                await message.channel.send(the_message)
                    
                guesslist.clear()
                guessusedletters.clear()
                guesshardcore_letters.clear()
            else:
                wordconstruct = ""
            
                for letter in list(correct_word):
                    if guesshardcore == 0:
                        wordconstruct += guesslist[letter]
                    else:
                        wordconstruct += "-"
                
                wordconstruct = wordconstruct.capitalize()
                
                whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\nUsed: " + str(guessusedletters).replace("'", "") + "\n> _" + message.author.name + "_"
                if guesshard == 1: whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\n> _" + message.author.name + "_"
                elif guesshardcore == 1:
                    used = ""
                    for i in guesshardcore_letters.keys():
                        used += f" {i} ({guesshardcore_letters[i]}) "
                    whattosend = "Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**\nUsed: " + used + "\n> _" + message.author.name + "_"
                await message.channel.send(whattosend)

                if message.author.name not in guesstries:
                    guesstries[message.author.name] = 1
                else:
                    guesstries[message.author.name] += 1
        guess_current_user = "NULL"

wordleAdmins = [
    255432828668477441,
    246213412059611136
    ]

wordleGiveUp = []

async def wordle(ctx, *args):
    global guess_current_user
    global guesslist
    global guessrun
    global correct_word
    global guesschannelbind
    global guesshard
    global guesshardcore
    
    reset = " ".join(args)
    
    if (reset == "reset" and ctx.author.id in wordleAdmins):
        if guessrun == 1:
            guesschannelbind = 0
            guessrun = 0
            guesshard = 0
            guesshardcore = 0
            guess_current_user = "NULL"
            correct_word = ""
            guesstries.clear()
            guesslist.clear()
            guessusedletters.clear()
            guesshardcore_letters.clear()
            await ctx.send(f"Admin has canceled the game. The word was {correct_word}")
        else:
            await ctx.send("No game commencing")
        return
    
    if (reset == "give up" and ctx.author.id not in wordleGiveUp):
        wordleGiveUp.append(ctx.author.id)
        await ctx.send(ctx.author.name + " opted in for canceling the game.")
        await ctx.message.delete()
        if len(wordleGiveUp)>=len(guesstries.keys()):
            await ctx.send(f"All playing users have agreed on canceling the game. The word was {correct_word}")
            guesschannelbind = 0
            guessrun = 0
            guesshard = 0
            guesshardcore = 0
            guess_current_user = "NULL"
            correct_word = ""
            guesstries.clear()
            guesslist.clear()
            guessusedletters.clear()
            guesshardcore_letters.clear()
            wordleGiveUp.clear()
        return
    
    if guessrun == 0:
        try:
            wordleGiveUp.clear()
            guessrun = 1
            sites = [
                "https://raw.githubusercontent.com/mahsu/IndexingExercise/master/5000-words.txt",
                "https://www.mit.edu/~ecprice/wordlist.10000",
                "https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt"
            ]
            word_site = random.choice(sites)

            response = requests.get(word_site)
            WORDS = response.content.splitlines()
            correct_word = random.choice(WORDS)
            correct_word = correct_word.decode('UTF-8')
            correct_word = correct_word.lower()
            
            if "hardcore" in ctx.message.content.lower():
                guesshardcore = 1
            elif "hard" in ctx.message.content.lower():
                while(len(correct_word)<10):
                    correct_word = random.choice(WORDS)
                    correct_word = correct_word.decode('UTF-8')
                guesshard = 1
        
            for letter in correct_word:
                guesslist[letter] = "-"
                
            wordconstruct = ""
            for letter in list(correct_word):
                wordconstruct += guesslist[letter]
            wordconstruct = wordconstruct.capitalize()
            
            await ctx.send("Game started and binded in <#" + str(ctx.channel.id) + ">.")
            await ctx.send("Word: **" + wordconstruct + "**\nLetters: **" + str(len(wordconstruct)) + "**")
            if guesshardcore == 1:
                try:
                    data = json.loads(commands.fun.loadwordurban(correct_word))
                    msg = data["list"][random.randint(0, len(data["list"])-1)]['definition']
                    msg = msg.replace("[", "**[").replace("]", "]**")
                    await ctx.send(msg)
                except Exception as e:
                    await ctx.send(f"Some error occured... ```{e}```")
                
            
            guesschannelbind = ctx.channel.id
        except Exception as e:
            await ctx.send(f"Error occured.```{e}```")
    else:
        await ctx.send("Game commencing in <#" + str(guesschannelbind) + ">!")