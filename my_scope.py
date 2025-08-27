'''
LEGB
Local, Enclosing, Global, Built-in
'''

# global x
# nonlocal x

for a in range(2): # 0,1
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3): # 0,1,2
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4): # 0,1,2,3
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)


outer()
print(x)
print(a)
