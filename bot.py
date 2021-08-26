# bot.py


import os
import easy_db

db = easy_db.DataBase('MyDB.db')

db.create_table('users', {'name': str, 'role': str})

print(db.table_names())

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def reloadRoles(ctx):
    if get(ctx.guild.roles, name="AI"):
        await ctx.send("Role AI already exists")
    else:
        await ctx.guild.create_role(name="AI", colour=discord.Colour(0x0062ff))

    if get(ctx.guild.roles, name="Finance"):
        await ctx.send("Role Finance already exists")
    else:
        await ctx.guild.create_role(name="Finance", colour=discord.Colour(0x0062ff))

@bot.command()
async def addMember(ctx, target: discord.Member):
    #Adds a new member
    guild = ctx.guild
    if guild.get_member(target.id) is not None:
        db.append('users', [{'name': 'target.id', 'role': 'member'}])
        await ctx.send('User added')
    else:
        await ctx.send('User not on server')
        print(f'User not on server')
"""

@bot.command()
async def save(ctx,key,item):
    #Creates ("saves") a new item

@bot.command()
async def load(ctx, key):
    #Loads an item
"""

bot.run(TOKEN)
