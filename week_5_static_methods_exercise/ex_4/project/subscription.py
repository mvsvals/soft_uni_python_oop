class Subscription:
    id = 1
    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.exercise_id = exercise_id
        self.trainer_id = trainer_id
        self.customer_id = customer_id
        self.date = date
        self.id = Subscription.id
        Subscription.id += 1

    @staticmethod
    def get_next_id():
        return Subscription.id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"