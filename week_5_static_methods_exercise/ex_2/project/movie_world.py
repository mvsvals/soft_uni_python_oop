from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next(customer for customer in self.customers if customer.id == customer_id)
        found_dvd = next(dvd for dvd in self.dvds if dvd.id == dvd_id)
        if found_dvd.is_rented:
            renting_person = next(x for x in self.customers if found_dvd in x.rented_dvds)
            if renting_person.id != customer_id:
                return  "DVD is already rented"
            return f"{customer.name} has already rented {found_dvd.name}"
        if found_dvd.age_restriction > customer.age:
            return  f"{customer.name} should be at least {found_dvd.age_restriction} to rent this movie"
        found_dvd.is_rented = True
        customer.rented_dvds.append(found_dvd)
        return f"{customer.name} has successfully rented {found_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        found_dvd = next(dvd for dvd in self.dvds if dvd.id == dvd_id)
        customer = next(customer for customer in self.customers if customer.id == customer_id)
        if found_dvd in customer.rented_dvds:
            found_dvd.is_rented = False
            customer.rented_dvds.remove(found_dvd)
            return f"{customer.name} has successfully returned {found_dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        output_list = []
        for customer in self.customers:
            output_list.append(customer.__repr__())
        for dvd in self.dvds:
            output_list.append(dvd.__repr__())
        return '\n'.join(output_list)


c1 = Customer("John", 16, 1)

c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)

d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)

movie_world.add_customer(c2)

movie_world.add_dvd(d1)

movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))

print(movie_world.rent_dvd(2, 1))

print(movie_world.rent_dvd(1, 2))

print(movie_world)