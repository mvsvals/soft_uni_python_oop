

def type_check(num):
    def decorator(function):
        def wrapper(arg):
            if not isinstance(arg, num):
                return "Bad Type"
            result = function(arg)
            return result
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))