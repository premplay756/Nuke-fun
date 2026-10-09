import os
from colorama import Fore

class Funcs:
    @staticmethod
    def get_input(prompt, validator=None):
        env_token = os.getenv("DISCORD_BOT_TOKEN")
        if env_token:
            return env_token
        return "RENDER_AUTOMATED_BYPASS"
