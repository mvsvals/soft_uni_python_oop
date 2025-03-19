def genrange(start: int, end: int):
    index = start
    while index <= end:
        yield index
        index += 1

