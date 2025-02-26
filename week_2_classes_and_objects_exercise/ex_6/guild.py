from typing import List
from player import Player


class Guild:
    def __init__(self, name: str, ):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        found_player = next((x for x in self.players if x.name == player_name), None)
        if found_player:
            self.players.remove(found_player)
            player.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + '\n'.join(x.player_info() for x in self.players)


