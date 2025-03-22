

def cache(func):
    log = dict()
    def wrapper(arg):
        if arg in log:
            return log[arg]
        result = func(arg)
        log[arg] = result
        return result
    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(3)
print(fibonacci.log)