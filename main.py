import os
import sys
from colorama import Fore, init
from render_server import keep_alive

init(autoreset=True)

# 1. Fire up the Flask background keep-alive check structure 
keep_alive()

# 2. Extract your discord authentication string via backend settings
token = os.getenv("DISCORD_BOT_TOKEN")

if not token or token.strip() == "":
    print(f"{Fore.RED}[!] CRITICAL ERROR: 'DISCORD_BOT_TOKEN' environment setting missing on Render.")
    sys.exit(1)

print(f"{Fore.GREEN}[+] Access Key compiled successfully. Launching client workflows...")

# Add your remaining bot client startup routines here
print("Bot running...")
while True:
    pass
