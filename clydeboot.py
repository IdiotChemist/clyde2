import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import json
import os


Client = discord.Client()
client = commands.Bot(command_prefix ="C.")
client.remove_command('help')




players = {}
queues = {}




@client.event
async def on_ready():
    print("WE BE READY")



def __init__(self, bot):
        self.bot = bot

@client.command()
async def hi():
    await client.say('hi')
@client.command()
async def thonk():
    await client.say(':thinking:')
@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
@client.command(pass_context=True)
async def clear(ctx, amount=20):
    await client.say('**woops! you can only delete messages that are under 14 days old**')
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted uwu')








@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'Info',
        description = 'Hello, my name is clyde2 the little brother of Cylde created by Iძɿ૦੮CҺ૯ɱɿς੮#0404 and Azy#4269',
        color = discord.Color.blue()
        )

    embed.set_footer(text='Hello!.')
    embed.set_image(url='https://s.aolcdn.com/hss/storage/midas/5b90065e72b963836a64837dee9ce7d0/204504948/IMG_0017.jpg')
    embed.set_thumbnail(url='https://static.businessinsider.com/image/5b7050cd8ea82f94598b4da6-750.jpg')
    embed.set_author(name ='Thank you for choosing clyde2!',
    icon_url='https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjq8Pz4ptXfAhVJaq0KHT5GBwkQjRx6BAgBEAU&url=http%3A%2F%2Fsendflowers4.info%2Fmod%25C3%25A9ration-bot-a904dd9%2F&psig=AOvVaw1D_6o0ENP8Mvn-0T_rY5pN&ust=1546730214745960')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)


    await client.say(embed=embed)






@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author


    embed = discord.Embed(
        color = discord.Color.orange()
    )


    embed.set_author(name='help')
    embed.add_field(name='f?hi', value='Say hi to me!', inline=False)
    embed.add_field(name='f?thonk', value='**B I G  T H O N K**', inline=False)
    embed.add_field(name='f?join', value='Joins the voice channel', inline=False)
    embed.add_field(name='f?leave', value='Leaves the voice channel', inline=False)
    embed.add_field(name='f?purge', value='Clears all the messages from under 14 days (**mods/admins only!!**) ', inline=False)
    embed.add_field(name='f?say', value='Echos your message', inline=False)
    




    await client.send_message(author, embed=embed)

    



    

client.run("NTMwNTcxNTc3MjY4MzcxNDgy.DxBWYQ.J61BekYqCwBWzHUwnu6AF7U6-tM")
