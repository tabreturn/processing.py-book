student = ['Sam', 24]
student = {'name':'Sam', 'age':24}

# accessing dictionaries

print(student['age'])   # displays: 24
print(student['name'])  # displays: Sam
print(student)          # {'name': 'Sam', 'age': 24}

if 'age' in student:
    print(student['age'])

# modifying dictionaries

student['age'] = 25
print(student)          # {'name': 'Sam', 'age': 25}

student['id'] = 19950501
print(student)          # {'name': 'Sam', 'id': 19950501, 'age': 25}

del student['age']
print(student)          # {'name': 'Sam', 'id': 19950501}

# nesting dictionaries and lists

students = {
  'names': ['Sam', 'Lee'],
  'ids': [19950501, 19991114]
}
print( students['names'][1] ) # Lee

students = [
  {'name':'Sam', 'id':19950501},
  {'name':'Lee', 'id':19991114}
]
print( students[1]['name'] )  # Lee

# combining loops and dictionaries

courses = {
  'game development': 'Prof. Smith',
  'web design': 'Prof. Ncube',
  'code art': 'Prof. Sato'
}

# iterating keys

#for course in courses:
for course in sorted(courses):
    print(course)

print( sorted(courses.keys()) ) # ['code art', 'game development', 'web design']

# iterating values

for prof in courses.values():
    print(prof)

# iterating items

print( courses.items() )

for kv in courses.items():
    print(kv)

#for course, prof in sorted(courses.items()):
for course, prof in reversed(sorted(courses.items())):
    print('{} teaches the {} course.'.format(prof, course))
