import discord
import ezcord
import os
from dotenv import load_dotenv


bot = ezcord.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("TOKEN"))
