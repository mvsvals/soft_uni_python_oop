from abc import abstractmethod

from project.animals.animal import Bird
from project.food import Food

class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def allowed_food(self):
        return ["Meat"]

    @property
    def weight_coefficient(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return 'Cluck'

    @property
    def allowed_food(self):
        return ["Meat", 'Vegetable', 'Fruit', 'Seed']

    @property
    def weight_coefficient(self):
        return 0.35
