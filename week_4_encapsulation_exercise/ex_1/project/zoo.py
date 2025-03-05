class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > 0:
            if price <= self.__budget:
                self.__animal_capacity -= 1
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker_obj in self.workers:
            if worker_obj.name == worker_name:
                self.workers.remove(worker_obj)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_sum = sum(x.salary for x in self.workers)
        if salaries_sum <= self.__budget:
            self.__budget -= salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return  "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_sum = sum(x.money_for_care for x in self.animals)
        if tending_sum <= self.__budget:
            self.__budget -= tending_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return  "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)
        return f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n" +'\n'.join(animal.__repr__() for animal in lions) + f"\n----- {len(tigers)} Tigers:\n" +'\n'.join(animal.__repr__() for animal in tigers) + f"\n----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(animal.__repr__() for animal in cheetahs)

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)
        return f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n" + '\n'.join(animal.__repr__() for animal in keepers) + f"\n----- {len(caretakers)} Caretakers:\n" + '\n'.join(animal.__repr__() for animal in caretakers) + f"\n----- {len(vets)} Vets:\n" + '\n'.join(animal.__repr__() for animal in vets)