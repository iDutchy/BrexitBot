from discord.ext import commands

bot = command.Bot(command_prefix="wtf?")

@bot.event
async def on_ready():
  print("Ready for Brexit!")


bot.run("CBT")
