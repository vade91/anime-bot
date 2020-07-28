import discord
from discord.ext import commands
import config
import random
import os
from discord.utils import get
import youtube_dl

#TOKEN = 'NjgwNzg5NTU0NjI5ODM2ODE0.XlFA0A.cpyaVGpDYI1fzoMFTJfgLKt_6sQ' #мой токен
bot = commands.Bot(command_prefix='!')

#события
@bot.event
async def on_ready():
    print('BOT connected')

@bot.event
async def on_message( message ):
    await bot.process_commands( message )

    msg = message.content.lower()
    badwords = open('badwords.txt', 'r', encoding='utf-8').read().split(', ')
    syms = ['.', ',', '?', '!', ':', ';', '`']
    bad = False
    for sym in syms:
        msg = msg.replace(sym, '')
        msg_words = msg.split()
    for w in msg_words:
        if w in badwords:
            bad = True
            break
    if bad == True:
        await message.delete()
        await message.author.send('Ругаться на сервере нельзя!')
        

#команды
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

@bot.command(pass_context=True)    
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f' { author.mention }Welcome to the club, buddy! :peach: :wave:')

@bot.command(pass_context=True)
async def biba(ctx):
    author = ctx.message.author
    await  ctx.send('У ' + author.mention + ' биба ' + str(random.randrange(10, 25, 1)) + ' см')

@bot.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()    

@bot.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()  

bot.run(config.TOKEN)