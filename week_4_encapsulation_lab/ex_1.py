class Person:
    def __init__(self, name: str, age: int):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
