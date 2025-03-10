class Mammal:
    __kingdom = 'animals'
    def __init__(self, name: str, type: str, sound: str):
        self.sound = sound
        self.type = type
        self.name = name

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"
