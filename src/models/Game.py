from models.Player import Player
from models.Champion import Champion
from models.Champion import champions
import random
class Game():
    def __init__(self, guild_id):
        self.guild_id = guild_id
        self.players = set()
        self.started = False
        self.champion = None
    def add_player(self, player_id):
        self.players.add(player_id)

    def remove_player(self, player_id):
        self.players.discard(player_id)

    def start(self):
        if len(self.players) < 2:
            return "Jogadores insuficientes pra começar a partida."
        return "Partida iniciada com os jogadores: " + ", ".join(map(str, self.players))
    
    def choose_champion(self):
        self.champion = random.choice(list(champions.values()))
        return self.champion

    def verify_player(self, player: Player):
        return player in self.players
    
    def set_started(self, condition):
        self.started = condition