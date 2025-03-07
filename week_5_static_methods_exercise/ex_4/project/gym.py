from project.customer import Customer
from project.trainer import Trainer
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.subscription import Subscription

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if not customer in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if not trainer in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if not equipment in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if not plan in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)

    def  subscription_info(self, subscription_id: int):
        found_subscription = next(x for x in self.subscriptions if x.id == subscription_id)
        found_customer = next(x for x in self.customers if x.id == found_subscription.customer_id)
        found_trainer = next(x for x in self.trainers if x.id == found_subscription.trainer_id)


        found_plan =  next(x for x in self.plans if x.id == found_subscription.exercise_id)
        found_equipment = next(x for x in self.equipment if x.id == found_plan.equipment_id)
        output = [found_subscription.__repr__(), found_customer.__repr__(), found_trainer.__repr__(), found_equipment.__repr__(), found_plan.__repr__()]
        return '\n'.join(output)



