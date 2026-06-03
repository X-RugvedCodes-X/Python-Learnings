# Like a HashMap, Key-Value Pair
student = {'name': 'John', 'age': 25, 'courses': ['math', 'compSci']}
# print(student)
# print(student['name'])
# print(student['courses'])
# print(student['phone'])     # KeyError: 'phone'

# Using get method

# print(student.get('name'))    # John
# print(student.get('phone'))   # None
# print(student.get('phone', 'Not Found'))   # Not Found, A Default Value we use

# Adding Key-Valaue pairs to our Dictionary

student['phone'] = '555-555'
# print(student)  # {'name': 'John', 'age': 25, 'courses': ['math', 'compSci'], 'phone': '555-555'}
student['name'] = "Dave"
# print(student)    # {'name': 'Dave', 'age': 25, 'courses': ['math', 'compSci'], 'phone': '555-555'}

# Update full dictionary in one go
student.update({'name': 'Jane', 'age': 26, 'phone': '666-6666'})
# print(student)  # {'name': 'Jane', 'age': 26, 'courses': ['math', 'compSci'], 'phone': '666-6666'}

# Deleting a key
# del student['age']
# print(student)  # {'name': 'Jane', 'courses': ['math', 'compSci'], 'phone': '666-6666'}

# Deleting using pop
# age = student.pop('age')
# print(student)  # {'name': 'Jane', 'courses': ['math', 'compSci'], 'phone': '666-6666'}

# Length 
# print(student, "Length:", len(student))  # {'name': 'Jane', 'age': 26, 'courses': ['math', 'compSci'], 'phone': '666-6666'} Length: 4

# getting all keys and values
print(student.keys())   # *  dict_keys(['name', 'age', 'courses', 'phone'])
print(student.values()) # *  dict_values(['Jane', 26, ['math', 'compSci'], '666-6666'])
print(student.items())  # *  dict_items([('name', 'Jane'), ('age', 26), ('courses', ['math', 'compSci']), ('phone', '666-6666')])

for key in student:
  print(key, end=" ")   # name age courses phone 

for key, value in student.items():
  print("key:", key, "value:", value)
'''
key: age value: 26
key: courses value: ['math', 'compSci']
key: phone value: 666-6666
'''

