courses1 = ['maths', 'physics', 'chemistry', 'compsc']
courses2 = courses1

print(courses1)
print(courses2)
courses1[0] = 'extra'
print(courses1)
print(courses2)

courses3 = ('maths', 'physics', 'chemistry', 'compsc')
courses4 = courses3
courses5 = ()
courses6 = tuple()

print(courses3)
print(courses4)
courses3[0] = 'extra'
print(courses3)
print(courses4)
