class SteamUser:
    def __init__(self, username, games):
        self.played_hours = 0
        self.username = username
        self.games = games

    def play(self, game, hours):
        if game not in self.games:
            return  f"{game} is not in library"
        else:
            self.played_hours += hours
            return f"{self.username} is playing {game}"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return  f"{game} is already in your library"

    def status(self):
        return  f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"