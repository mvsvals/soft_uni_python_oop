def read_next(*args):
    for collection in args:
        yield from collection
