import discord

async def rolecolour(ctx, arguments, c):
    try:
        
        if arguments[0:2] == "id":
            role = ctx.guild.get_role(int(c[0][3:]))

            colour = "0x" + c[1].lstrip('#')
            await role.edit(color=int(colour, 16))
            
        elif arguments[0:4] == "name":
            role = discord.utils.get(ctx.guild.roles, name = c[0][5:])
            
            colour = "0x" + c[1].lstrip('#')
            await role.edit(color=int(colour, 16))
        else:
            await ctx.channel.send("Invalid option (Options: name, id).")
            return
            
    except Exception as e:
        await ctx.channel.send(f"Something went wrong. ```{e}``````{arguments}```")
        
    else:
        await ctx.channel.send("Changed.")
        
async def purge(ctx, arguments):
    try:
        await ctx.channel.purge(limit=int(arguments)+1)
    except Exception as e:
        await ctx.channel.send(f"Something went wrong. ```{e}``````{arguments}```")