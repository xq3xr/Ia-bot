import discord
from discord.ext import commands
import aiohttp

# Initialisation du bot
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# Fonction pour générer une image avec une intelligence artificielle
async def generate_image(ctx, input_text):
    async with aiohttp.ClientSession() as session:
        async with session.post('API_IA_IMAGE', json={'text': input_text}) as response:
            if response.status == 200:
                image_url = await response.json()
                await ctx.send(image_url)
            else:
                await ctx.send("Erreur lors de la génération de l'image.")

# Commande /imagine pour générer une image
@bot.command()
async def imagine(ctx, *, input_text):
    await generate_image(ctx, input_text)

# Fonction pour discuter avec une intelligence artificielle
async def chat_with_ai(input_text):
    async with aiohttp.ClientSession() as session:
        async with session.post('API_IA_TEXT', json={'text': input_text}) as response:
            if response.status == 200:
                ai_response = await response.text()
                return ai_response
            else:
                return "Erreur lors de la communication avec l'intelligence artificielle."

# Commande /ia pour discuter avec une intelligence artificielle
@bot.command()
async def ia(ctx, *, input_text):
    ai_response = await chat_with_ai(input_text)
    await ctx.send(ai_response)

# Lancement du bot
bot.run('TOKEN_BOT')