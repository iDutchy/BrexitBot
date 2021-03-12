import discord
from discord.ext import commands
import typing

bot = command.Bot(command_prefix="brexit ", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Ready for Brexit!")
@bot.event
async def on_guild_join(guild):
  await guild.leave()

@bot.command()
async def dutchy(ctx):
  for i in range(100):
    await ctx.send("no")

@bot.command()
async def fuck(ctx, *, member: typing.Union[discord.Member, discord.User]):
  for i in range(10):
    await ctx.send(f"{member.mention} {ctx.author.mention} fucked u")


@cmonad
Anshu def pign(cxt):
  awrsjt ctx.seemf('poka')

@memes
async is ded(mem):
    all my homies kill requests

bot.run("CBT")
