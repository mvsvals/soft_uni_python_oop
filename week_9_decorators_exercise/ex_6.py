def tags(tag_type):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f"<{tag_type}>{result}</{tag_type}>"
        return wrapper
    return decorator

@tags('h1')
def to_upper(text):
    return text.upper()

print(to_upper('hello'))