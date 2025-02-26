class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills = dict()
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        return f"Name: {self.name}\n" + f"Guild: {self.guild}\n" + f"HP: {self.hp}\n" + f"MP: {self.mp}\n" + "\n".join(f'==={skill} - {mana}' for skill, mana in self.skills.items())