from math import sqrt

def get_primes(my_list: list[int]):
    for num in my_list:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num