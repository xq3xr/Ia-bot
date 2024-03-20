import discord
from discord.ext import commands
import contextlib

class CustomContextManager:
    def __init__(self):
        # Initialisation du gestionnaire de contexte
        pass

    def __enter__(self):
        # Code à exécuter au début du contexte
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # Code à exécuter à la fin du contexte
        pass

@contextlib.contextmanager
def custom_context_manager():
    # Code à exécuter au début du contexte
    try:
        yield
    finally:
        # Code à exécuter à la fin du contexte
        pass

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def test(ctx):
    # Utilisation du gestionnaire de contexte personnalisé
    with custom_context_manager():
        await ctx.send('Test du gestionnaire de contexte')

bot.run('MTIxNzE1NzU2MjUyMTA5NjIwMg.Gh8jz3.Lrg9shzfqkskAsT61LIBlJJYw3R9eCIHtnWjMQ')