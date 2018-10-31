#Paint's Epic Bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print ("Paint's Epic Bot,ready for action!")
    print ("I am from" + bot.user.name)
    print ("With the ID:" + bot.user.id)

@bot.command(pass_context=True)
async def paint(ctx):
    await bot.say("HI HUMAN I AM A ROBOT!")
    print("Your bot works")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: LMAO GO DIE FATMAN {}".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def urthebestbotever (ctx):
    await bot.say("THANK YOU VERY MUCH FOR THAT KIND COMPLIMENT U GREAT HUMAN!")

@bot.command(pass_context=True)
async def saveme(ctx):
    await bot.say("COMMAND LIST %PAINT %INFO %KICK %urthebestbotever")
            


bot.run("NTA0MzQ5MzU4MjMwMDc3NDQx.DrpCZA.KMHAZZKEnXR5cBNwtrWrD_GLi54")
                         
