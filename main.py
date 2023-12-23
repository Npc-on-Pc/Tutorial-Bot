import discord
import ezcord

bot = ezcord.Bot(
    intents=discord.Intents.default()
)

bot.run("TOKEN")