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
    global channel
    if channel == "" :
        channel = ctx.channel
        await ctx.send("``` * * * PAINFUL BASIC ALPHA 6 * * *\rA SHITTON BYTES FREE\rNO COPYRIGHT 2022```")
        return
    await ctx.send("Already being used elsewhere.")

@client.command(aliases = [ "PRINT", "$" ])
async def printFn(ctx, *, toprint) :
    if toprint.isupper() :
        toprint += "f"
        toprint = toprint.replace("\\\"", "#!")
        printing = toprint.split("\"")
        if not len(printing) == 3 :
            await ctx.send("?SYNTAX ERROR")
            return
        await ctx.send(printing[1].replace("#!", "\""))
    else :
        await ctx.send("?CHARACTER ERROR")

@client.event
async def on_command_error(ctx, error) :
    if channel == ctx.channel and ctx.message.content.isupper() :
        await ctx.send("?SYNTAX ERROR")

client.run(token)