courses = ['maths', 'physics', 'chemistry', 'compsc']
courses.append('art')
courses.insert(0, 'literature')
courses2 = ['dance', 'music']
courses2.remove('music')
print(courses2)
courses3 = []
courses4 = list()

# courses.insert(len(courses), courses2)
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[1:3])
print(courses[:2])
print(courses[1:])
print(courses[-1])
print(courses[-1][1])
courses.extend(courses2)
print(courses)
print(courses.index('dance'))
courses.sort()
print(courses)
courses.reverse()
print(courses)
num = [1, 3, 2, 5, 4]
print(sum(num))
for index, course in enumerate(courses, start=1):
    print(index, course)
str_courses = ','.join(courses)
print(str_courses)
new_courses = str_courses.split(',')
print(new_courses)
