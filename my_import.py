import datetime
import os
import random
import sys

import my_module
# from my_module import find_index

print(sys.executable)

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Physics')
print(index)

print(os.getcwd())
print(os.__file__)

print(random.choice(courses))

today = datetime.date.today()
print(today)

print(my_module.list_even(1,2,3,4,5,6))
print(my_module.print_even_odd('Anthropomorphism'))
