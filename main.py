import os
import sys
from colorama import Fore, init
from render_server import keep_alive
from Plugins.funcs import Funcs

init(autoreset=True)
keep_alive()

print(f"{Fore.CYAN}[*] Cloud Environment initialization sequence started...")

token = os.getenv("DISCORD_BOT_TOKEN")
if not token or token.strip() == "":
    print(f"{Fore.RED}[!] Deployment halted: Missing mandatory 'DISCORD_BOT_TOKEN' variable in environment tab.")
    sys.exit(1)

prefix = os.getenv("BOT_PREFIX", "!")
print(f"{Fore.GREEN}[+] Environment Verified. Initializing internal Discord client structures...")
print(f"{Fore.YELLOW}[!] Remember to append your core bot connection loops right below this line.")
