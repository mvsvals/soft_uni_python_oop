class  take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count - 1:
            self.counter += 1
            return self.step * self.counter
        raise StopIteration()


