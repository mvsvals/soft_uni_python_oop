
def logged(function):
    def wrapper(*args):
        results = function(*args)
        return f'you called {function.__name__}{args}\nit returned {results}'
    return wrapper

