class Stack:
    def __init__(self, ):
        self.data: list = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return bool(not self.data)

    def __str__(self):
        # "[{element(N)}, {element(N-1)} ... {element(0)}]"
        return '['+ ", ".join(reversed(self.data)) + ']'

