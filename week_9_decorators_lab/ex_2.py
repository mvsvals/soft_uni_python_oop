from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        return [x for x in result if x.lower() in 'aeiou']
    return wrapper