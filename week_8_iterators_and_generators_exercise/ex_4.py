class sequence_repeat:
    def __init__(self, sequence, number):
        self.number = number
        self.sequence = sequence
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            index = self.i % len(self.sequence)
            self.i += 1
            return self.sequence[index]
        raise StopIteration()

