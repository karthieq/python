def func(string, value=9999):
    return string, value


def func1(string='', value=0):
    return string, value


def func2(*args, **kwargs):
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))
    print(type(kwargs['list']))
    print(type(kwargs['tuple']))
    print(type(kwargs['set']))
    print(type(kwargs['dict']))
    print(args[0], args[0][1])
    print(args[1])
    print(kwargs['list'][0], kwargs['list'][1])
    print(kwargs['tuple'][0], kwargs['tuple'][1])
    print(200 in kwargs['set'], 50 in kwargs['set'])
    print(kwargs['dict']['name'], kwargs['dict']['age'])


print(func('a'))
print(func(value=999, string='a'))

print(func1())
print(func1('x', 1))
print(func1(value=2, string='xx'))

itms = ['a', 'b']

func2(
    itms,
    'string',
    100,
    list=['list', 100],
    tuple=('tuple', 200),
    set={100, 200, 500, 2000},
    dict={'name': 'xyz', 'age': 99}
)
