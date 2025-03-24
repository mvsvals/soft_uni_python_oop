


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

from unittest import TestCase, main

class TestWorker(TestCase):
    def test_worker_init(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_get_info(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual('Test has saved 0 money.', worker.get_info())

    def test_work_with_no_energy(self):
        worker = Worker('Test', 100, 0)

        with self.assertRaises(Exception) as f:
            worker.work()

        self.assertEqual('Not enough energy.', str(f.exception))
        self.assertEqual(0, worker.money)
        self.assertEqual(0, worker.energy)

        # Negative energy
        worker.energy = -1
        self.assertEqual('Not enough energy.', str(f.exception))
        self.assertEqual(0, worker.money)
        self.assertEqual(-1, worker.energy)

    def test_worker_works(self):
        worker = Worker('Test', 100, 2)
        self.assertEqual(0, worker.money)
        self.assertEqual(2, worker.energy)


        worker.work()
        self.assertEqual(100, worker.money)
        self.assertEqual(1, worker.energy)

        worker.work()
        self.assertEqual(200, worker.money)
        self.assertEqual(0, worker.energy)

    def test_rest(self):
        worker = Worker('Test', 100, 2)

        worker.rest()
        self.assertEqual(3, worker.energy)

if __name__ == '__main__':
    main()