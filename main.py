import discord
from discord.ext import commands

lines = []
channel = ""

with open("./Token.txt") as f :
    token = f.read()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready() :
    print(f"Connected to discord as {client.user}")

@client.command(aliases = [ "PAIN", "Pain" ])
async def pain(ctx) :
    if channel == "" :
        channel = ctx.channel
        await ctx.send(" * * * PAINFUL BASIC ALPHA 2 * * *\rA SHITTON BYTES FREE\rNO COPYRIGHT 2022")
        return
    await ctx.send("Already being used elsewhere.")

#@client.command(aliases = [ "PRINT\"", "$\"" ])
#async def print(ctx, ) :
    

client.run(token)