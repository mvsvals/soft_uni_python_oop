class dictionary_iter:
    def __init__(self, my_dict: dict):
        self.my_dict = tuple(my_dict.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= len(self.my_dict) - 1:
            i = self.i
            self.i += 1
            return self.my_dict[i]
        raise StopIteration()
