import discord
from discord.ext import commands
from use_api import CatApi

# client (our bot)
client = commands.Bot(command_prefix='meow-')
ob = CatApi()

@client.command(name='image')
async def image(context):
    url = ob.get_url()['url']
    msg_embd = discord.Embed(title="Purr...", description="Keep purring", color=0xFFC0CB)
    msg_embd.set_image(url=url)
    await context.message.channel.send(embed=msg_embd)

@client.command(name='gif')
async def gif(context):
    url = ob.get_url(search="?mime_types=gif")['url']
    msg_embd = discord.Embed(title="Purr...", description="Keep purring", color=0xFFC0CB)
    msg_embd.set_image(url=url)
    await context.message.channel.send(embed=msg_embd)

@client.command(name='info')
async def info(context):
    url = ob.get_info()
    print(url)
    msg_embd = discord.Embed(title="Purr...", description="Keep purring", color=0xFFC0CB)
    # msg_embd.set_image(url=url)
    await context.message.channel.send(embed=msg_embd)

@client.command(name='save')
async def save(context):
    response = ob.save_image()
    if(response=='saved'):
        await context.message.channel.send("Saved!!")

@client.command(name='command')
async def help(context):
    msg_embd = discord.Embed(title="Helper Cat", description="Consists of all commands available", color=0xFFC0CB)
    # msg_embd.set_image(url=url)
    msg_embd.add_field(name="meow-image", value="shows random image of cat", inline=False)
    msg_embd.add_field(name="meow-gif", value="shows random gif of cat", inline=False)
    msg_embd.add_field(name="meow-save", value="saves the previous image/gif in your desktop", inline=False)
    msg_embd.add_field(name="meow-command", value="shows all commands availiable for the bot", inline=False)
    await context.message.channel.send(embed=msg_embd)
# Run the client on the server
client.run('OTM0NzI5NzY3MzUyMTY4NDc4.Ye0U7g.SNlvuJb33ZlVAi22dKtPd3cANbc')