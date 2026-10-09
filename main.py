import os
import sys
import asyncio
from colorama import Fore, init

# Initialize color mapping metrics
init(autoreset=True)

print(f"{Fore.CYAN}[*] Railway Production Environment successfully initialized...")

# 1. Pull your token silently from Railway's internal cloud variables
token = os.getenv("DISCORD_BOT_TOKEN")
prefix = os.getenv("BOT_PREFIX", "!")

if not token or token.strip() == "":
    print(f"{Fore.RED}[!] Deployment halted: Missing 'DISCORD_BOT_TOKEN' in Railway variables tab.")
    sys.exit(1)

# =========================================================
# ⚠️ YOUR ORIGINAL BOT LOGIN LOGIC / COMMANDS GO HERE ⚠️
# =========================================================
# Standard gateway integration layer via discord.py framework:
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Allows bot to read trigger words
intents.members = True          # Required for utility actions

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}[+] Connected to Discord Gateway as: {bot.user}")

# =========================================================
# RAILWAY RUN ENGINE
# =========================================================
async def main():
    try:
        # Railway handles keeping this execution frame alive forever natively
        await bot.start(token)
    except Exception as e:
        print(f"{Fore.RED}[!] Gateway Connection Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
