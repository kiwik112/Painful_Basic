import discord
from discord.ext import commands

lines = {}
channel = ""
suppress = False

with open("./Token.txt") as f :
    token = f.read()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready() :
    print(f"Connected to discord as {client.user}")

@client.event
async def on_message(message) :
    global suppress
    global lines
    if message.channel == channel :
        suppress = False
        index = message.content.split(" ")[0]
        if index.isdigit() :
            suppress = True
            lines[str(index)] = message.content[len(index) + 1:]
    await client.process_commands(message)

@client.command(aliases = [ "PAIN", "Pain" ])
async def pain(ctx) :
    global channel
    if channel == "" :
        channel = ctx.channel
        await ctx.send("``` * * * PAINFUL BASIC ALPHA 8 * * *\rA SHITTON BYTES FREE\rNO COPYRIGHT 2022```")
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

@client.command(aliases = [ "EXIT" ])
async def exitFn(ctx) :
    global channel
    await ctx.send("DISCONNECTED")
    channel = ""

@client.event
async def on_command_error(ctx, error) :
    if channel == ctx.channel and ctx.message.content.isupper() and not suppress :
        await ctx.send("?SYNTAX ERROR")

client.run(token)