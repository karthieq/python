students = {
    'name': 'Karthik',
    'age': 37,
    'courses': [
        'maths',
        'physics',
        'chemistry',
        'compsc'
    ]
}
print(students)
# students.update({'name': 'Kani', 'age': 30, 'courses': ['extra']})
# print(students)

for key in students:
    print(f'{key}=>{students[key]}')
for key, val in students.items():
    print(key, val)
