from itertools import permutations


def possible_permutations(my_list):
    for perm in permutations(my_list):
        yield list(perm)