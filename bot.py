from discord.ext import commands

bot = command.Bot(command_prefix="brexit ")

@bot.event
async def on_ready():
  print("Ready for Brexit!")


bot.run("CBT")
