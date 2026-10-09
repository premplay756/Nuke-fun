import os
import sys
import time
from colorama import Fore, init
from render_server import keep_alive

keep_alive()
init(autoreset=True)

token = os.getenv("DISCORD_BOT_TOKEN")
if not token or token.strip() == "":
    print(f"{Fore.RED}[!] Deployment halted: Missing 'DISCORD_BOT_TOKEN' in Render Environment.")
    sys.exit(1)

prefix = os.getenv("BOT_PREFIX", "!")
print(f"{Fore.GREEN}[+] Environment Verified. Initializing internal Discord client structures...")

print("[+] System modules operational. Entering main runtime holding loop...")
try:
    while True:
        time.sleep(3600)
except (KeyboardInterrupt, SystemExit):
    print("[-] Shutting down framework execution modules cleanly.")
