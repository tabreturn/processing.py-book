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
print(student)  

# nesting dictionaries and lists

students = {
  'names': ['Sam', 'Lee'],
  'ids': [19950501, 19991114]
}
print( students['names'][1] ) # Lee

students = [
  {'name':'Sam', 'age':24},
  {'name':'Lee', 'age':18}
]
print( students[1]['name'] )  # Lee

# loops and dictionaries

courses = {
  'game development': 'Prof. Smith',
  'web design': 'Prof. Ncube',
  'code art': 'Prof. Sato'
}

print(courses.keys())
print(sorted(courses.keys())) # ['code art', 'game development', 'web design']

#for course in courses.keys():
for course in courses:
    print(course)
    
for prof in courses.values():
    print(prof)
    
#for course, prof in sorted(courses.items()):
for course, prof in reversed(sorted(courses.items())):
    print('{} teaches the {} course.'.format(prof, course))
