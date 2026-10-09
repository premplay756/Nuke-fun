import os
import sys

class Funcs:
    @staticmethod
    def get_input(prompt_text, validator=None):
        if "Enter Bot Token" in prompt_text or "Token" in prompt_text:
            token = os.getenv("DISCORD_BOT_TOKEN")
            if token:
                return token.strip()
            print("[!] Critical Deployment Failure: 'DISCORD_BOT_TOKEN' environment variable is empty.")
            sys.exit(1)
            
        if "Prefix" in prompt_text:
            return os.getenv("BOT_PREFIX", "!")
            
        return "CLOUD_ENVIRONMENT_AUTOPASS"

    @staticmethod
    def clear():
        pass
