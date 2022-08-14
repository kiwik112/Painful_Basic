import discord
from discord.ext import commands

channels = []

with open("./Token.txt") as f :
    token = f.read()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready() :
    print(f"Connected to discord as {client.user}")

@client.command(aliases = [ "PAIN", "Pain" ])
async def pain(ctx) :
    if (not channels.contains(ctx.channel)) :
        channels.Append(ctx.channel)
        ctx.send(" * * * PAINFUL BASIC ALPHA 1 * * *\rA SHITTON BYTES FREE\rNO COPYRIGHT 2022")