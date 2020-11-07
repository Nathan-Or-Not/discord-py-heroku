import os
from discord.ext import commands

bot = commands.Bot(command_prefix="n!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def roll(ctx):
    await ctx.send(f"{ctx.message.author.mention} rolled {random.randrange(1,101)}!")

if __name__ == "__main__":
    bot.run(TOKEN)
