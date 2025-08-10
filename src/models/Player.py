class Player:
    def __init__(self, player_id, name: str):
        self.player_id = player_id
        self.name = name
        self.is_ready = False
        self.points = 0

    def set_ready(self, is_ready: bool):
        self.is_ready = is_ready

    def add_points(self, points: int):
        self.points += points

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.player_id == other.player_id
        return False