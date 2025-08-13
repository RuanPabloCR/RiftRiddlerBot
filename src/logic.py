from models.Champion import Champion
from models.Champion import champions

async def Iniciar_Adivinhação(ctx, games):
    games[ctx.guild.id].set_started(True)