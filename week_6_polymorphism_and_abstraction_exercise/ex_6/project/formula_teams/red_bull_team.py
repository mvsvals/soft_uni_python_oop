from project.formula_teams.formula_team import FormulaTeam

class RedBullTeam(FormulaTeam):

    @property
    def expenses_per_race(self):
        return 250_000

    @property
    def sponsor_rewards(self):
        return {"Oracle": {1: 1_500_000, 2: 800_000},
                "Honda": {8: 20_000, 10: 10_000}}