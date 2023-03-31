from googlesearch import search
async def talk(message):
    keywords = message.content.split("Hey Levia,")[1]
    search(keywords)
    message = ""
    for i in range(0,5):
        response=google.search_results()
        data=response["body"]
        message+= f"**{data['Title']}** (<{data['Link']}>)\n\n"
        google.click_next()
    message.channel.send(message)