def outer():
    msg = 'Hello'

    def inner(cnt):
        print(f'{msg}, {cnt}!')

    return inner

f = outer()
f('World')
f('Universe')
