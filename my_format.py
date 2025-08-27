import datetime

person = {'name': 'John', 'age': 30}

sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

lst = ['Joe', 20]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(lst)
print(sentence)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jim', 40)
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(name='Jack', age=45)
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

for i in range(1, 4):
    sentence = 'The value is {}'.format(i)
    print(sentence)

for i in range(1, 4):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to {}'.format(pi)
print(sentence)

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

sentence = '1 MB is equal to {} bytes'.format(1000**2)
print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

date = datetime.datetime(2022, 8, 15, 18, 26, 50)
print(date)

sentence = '{:%B %d, %Y}'.format(date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(date)
print(sentence)
