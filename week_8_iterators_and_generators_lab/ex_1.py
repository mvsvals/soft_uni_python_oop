class custom_range:
    def __init__(self, start: int, end: int):
        self.end = end
        self.start = start - 1
        self.index = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.end:
            raise StopIteration
        return self.index



one_to_ten = custom_range(1, 10)

for num in one_to_ten:
    print(num)