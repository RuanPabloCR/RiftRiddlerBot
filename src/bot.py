import discord
import os
from discord.ext import commands
import logging
from dotenv import load_dotenv
from models.Game import Game
from models.Player import Player

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../resources/.env'))
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='R!', intents=intents)

# Cada chave é o ID do servidor e o valor é um objeto Game contendo
# informações sobre a partida em andamento
# Pra simplicidade, 1 partida por servidor

games = {}
@bot.event
async def on_ready():
    print(f"ONLINE, {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")


@bot.command()
async def init(ctx):
    if(ctx.guild.id not in games):
        games[ctx.guild.id] = Game(ctx.guild.id)
    await ctx.send("Inicializando uma partida...\nDigite `R!play` para participar.")

@bot.command()
async def play(ctx):
    if games[ctx.guild.id].verify_player(Player(ctx.author.id, ctx.author.name)):
        await ctx.send(f"{ctx.author.name}, você já está participando!")
    else:
        games[ctx.guild.id].add_player(Player(ctx.author.id, ctx.author.name))
        await ctx.send(f"{ctx.author.name} entrou na partida!")

@bot.command()
async def quit(ctx):
    if games[ctx.guild.id].verify_player(Player(ctx.author.id, ctx.author.name)):
        games[ctx.guild.id].remove_player(Player(ctx.author.id, ctx.author.name))
        await ctx.send(f"{ctx.author.name} saiu da partida!")
    else:
        await ctx.send(f"{ctx.author.name}, você não está participando da partida!")

@bot.command()
async def close(ctx):
    if ctx.guild.id in games:
        del games[ctx.guild.id]
        await ctx.send("Partida encerrada.")
    else:
        await ctx.send("Não há partida em andamento.")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)