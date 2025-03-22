
def even_parameters(function):
    def wrapper(*args):
        invalid_args = [arg for arg in args if isinstance(arg, str) or arg % 2 != 0]
        if invalid_args:
            return  "Please use only even numbers!"
        result = function(*args)
        return result
    return wrapper



@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))