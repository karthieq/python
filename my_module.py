def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


# item = ['a','b','c']
# print(find_index(item,'c'))


def list_even(*args):
    values = []
    for item in args:
        if item%2 == 0:
            values.append(item)
    return values

# itm = list_even(1,2,3,4,5,6)
# print(itm)

def print_even_odd(string):
    x = ''
    for idx,itm in enumerate(string,start=0):
        if idx%2 == 0:
            x += itm.upper()
        else:
            x += itm.lower()
    return x

# print(print_even_odd('Anthropomorphism'))
