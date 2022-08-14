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
        await ctx.send(" * * * PAINFUL BASIC ALPHA 3 * * *\rA SHITTON BYTES FREE\rNO COPYRIGHT 2022")
        return
    await ctx.send("Already being used elsewhere.")

@client.command(aliases = [ "PRINT", "$" ])
async def print(ctx, *, toprint) :
    toprint += "f"
    toprint = toprint.replace("\\\"", "#!")
    printing = toprint.split("\"")
    if not printing.length == 3 :
        await ctx.send("?SYNTAX ERROR")
        return
    await ctx.send(printing[1].replace("#!", "\""))

client.run(token)