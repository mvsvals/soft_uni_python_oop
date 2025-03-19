

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self):
        return self
    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.iterable[self.index]

