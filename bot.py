from discord.ext import commansd

bot = command.Bot(command_prefix="wtf?")

@bot.event
async def on_ready():
  print("Ready!")


bot.run("TOKEN")
