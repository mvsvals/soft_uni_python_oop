from abc import ABC, abstractmethod

class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value  < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self._budget = value

    @property
    @abstractmethod
    def sponsor_rewards(self):
        pass

    @property
    @abstractmethod
    def expenses_per_race(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        money_won = 0
        for sponsor in self.sponsor_rewards:
            for place, reward_amount in self.sponsor_rewards[sponsor].items():
                if race_pos <= place:
                    sponsor_money_won = reward_amount
                    break
            else:
                sponsor_money_won = 0
            money_won += sponsor_money_won
        revenue = money_won - self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
