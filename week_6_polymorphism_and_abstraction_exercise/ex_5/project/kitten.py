from project.animal import Animal
from project.cat import Cat

class Kitten(Cat):
    def __init__(self, name: str, age: int):
        Animal.__init__(self, name, age, 'Female')

    @staticmethod
    def make_sound():
        return "Meow"