greeting = 'Hello'
name = 'Karthik'
cat = greeting + ', ' + name
catformat = '{}, {}'.format(greeting, name.upper())
catformat2 = f'{greeting}, {name.upper()}'
message = 'Hello World'
multiline = """Line1
Line2
Line3"""
print(len(name))
print(dir(name))
print(message.lower())
print(message.upper())
print(message[0])
print(message[10])
print(message[-1])
print(message[:5])
print(message[6:])
print(message.count('l'))
print(message.find('World'))
print(message.replace('World', 'Universe'))
print(multiline)
print(cat)
print(catformat)
print(catformat2)
print(message.index('d'))
print(multiline.splitlines())
num1 = '100'
num2 = str(200)
print(num1 + num2)

# help(str.split)
print(message.split())
print(cat.split(','))
cat2 = cat + ', Keyan'
print(cat2.split(',', 1))
