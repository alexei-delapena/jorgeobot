import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='jorgeo ', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTIzNDM0OTY3NzA5NjU1MDcx.YcP91A.jCZFU_gaBynBQsKiTZjgtFtPJjE")