import os
import sys

class Funcs:
    @staticmethod
    def get_input(prompt_text, validator=None):
        """Bypasses standard interactive terminal pauses cleanly on the cloud."""
        if "Enter Bot Token" in prompt_text or "Token" in prompt_text:
            token = os.getenv("DISCORD_BOT_TOKEN")
            if token:
                return token.strip()
            sys.exit(1)
            
        if "Prefix" in prompt_text:
            return os.getenv("BOT_PREFIX", "!")
            
        return "RAILWAY_AUTOMATED_BYPASS"

    @staticmethod
    def clear():
        pass
