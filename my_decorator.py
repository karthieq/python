def decorator_function(original_function):
    def wrapper_function():
        print('Inside wrapper function')
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print('Inside display function')


display()
