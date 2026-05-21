courses = ['python', 'math', 'compSci', 'history']
# print(courses)      # ['python', 'math', 'compSci', 'history']
# print(len(courses)) # 4

# Accessing in List
# print(courses[0]) # python

# print(courses[len(courses) - 1])  # history
# # Better Way
# print(courses[-1])  # history, -1 is always the last item in any list 
# print(courses[:2])  # ['python', 'math'] 
# print(courses[1:])  # ['math', 'compSci', 'history'] 

# append 

courses.append('Art') # gets added to the end -> ['python', 'math', 'compSci', 'history', 'Art']
# print(courses)

# insert 
courses.insert(0, 'Geography')  # ['Geography', 'python', 'math', 'compSci', 'history', 'Art']
# print(courses)

courses.insert(3, 'Physics')
# print(courses)  # ['Geography', 'python', 'math', 'Physics', 'compSci', 'history', 'Art']

new_courses = ['Chemistry', 'Databases', 'Operating Systems']

# Inserting a new List
# courses.insert(0, new_courses)
# print(courses)  # [['Chemistry', 'Databases', 'Operating Systems'], 'Geography', 'python', 'math', 'Physics', 'compSci', 'history', 'Art']

courses.extend(new_courses)
# print(courses)  # ['Geography', 'python', 'math', 'Physics', 'compSci', 'history', 'Art', 'Chemistry', 'Databases', 'Operating Systems']
#                                                                                             ^             ^                 ^

# courses.extend(0, new_courses)  # ! Wrong 
# print(courses)

# Remove
courses.remove('math') 
# print(courses)  #  ['Geography', 'python', 'Physics', 'compSci', 'history', 'Art', 'Chemistry', 'Databases', 'Operating Systems']

popped_course = courses.pop() # Removes last item and returns a value
# print(popped_course)  # Operating Systems
# print(courses)        # ['Geography', 'python', 'Physics', 'compSci', 'history', 'Art', 'Chemistry', 'Databases']

# courses.sort()  # -> Sorts in Alphabetical Order
# print(courses)  # ['Art', 'Chemistry', 'Databases', 'Geography', 'Physics', 'compSci', 'history', 'python']

nums = [1, 5, 3, 4, 2]
# nums.sort()
# print(nums) # [1, 2, 3, 4, 5]

# Sort and Rverse Together

# courses.sort(reverse=True)
# print(courses)  # ['python', 'history', 'compSci', 'Physics', 'Geography', 'Databases', 'Chemistry', 'Art']

# nums.sort(reverse=True)
# print(nums)   # [5, 4, 3, 2, 1]

# Sorted Function -> Returns a new Sorted List without altering Original
# sorted_courses = sorted(courses)
# print(sorted_courses) # ['Art', 'Chemistry', 'Databases', 'Geography', 'Physics', 'compSci', 'history', 'python']

# sorted_nums = sorted(nums)
# print(sorted_nums)

# min, max, sum -> Very intuitive, min(list), max(list), sum(list)

# index
# print(courses.index('Geography')) # 0
# print(courses.index('history'))   # 4
# print(courses.index('math'))      # ValueError: list.index(x): x not in list

# print('math'  in courses) # False
# print('Art'   in courses) # True

# Looping

# for item in courses:
#   print(item)

''' Output: 
Geography
python
Physics
compSci
history
Art
Chemistry
Databases
'''

# for item in courses:
#   print(item, end=" ")  # Geography python Physics compSci history Art Chemistry Databases

# Without Loop 
# print(" ".join(courses))  # Geography python Physics compSci history Art Chemistry Databases

# enumerate

# for index, course in enumerate(courses):
#   print(index, course)
'''
0 Geography
1 python
2 Physics
3 compSci
4 history
5 Art
6 Chemistry
7 Databases
'''

# for index, course in enumerate(courses, start = 1):
#   print(index, course)
'''
1 Geography
2 python
3 Physics
4 compSci
5 history
6 Art
7 Chemistry
8 Databases
'''

# join
course_string = ', '.join(courses)
# print(course_string)    # Geography, python, Physics, compSci, history, Art, Chemistry, Databases

course_string = '-'.join(courses)
# print(course_string)    # Geography-python-Physics-compSci-history-Art-Chemistry-Databases

new_course_list = course_string.split('-')
# print(new_course_list)  # ['Geography', 'python', 'Physics', 'compSci', 'history', 'Art', 'Chemistry', 'Databases']

# Mutablity in List

# list_1 = ['history', 'math', 'physics', 'compSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'art'
# print(list_1) # ['art', 'math', 'physics', 'compSci']
# print(list_2) # ['art', 'math', 'physics', 'compSci']

# This is Because list_2 just refers to same list in the memory, therefore changes in any of the one affects the other
# This is bad in most of the cases in larger programs

# Instead use a Tuple, A tuple is an immutable list, means the functionality, methods, etc are same that as of list except involving the methods which require mutation of the list

# tuple_1 = ('history', 'math', 'physics', 'compSci')
# tuple_2 = tuple_1

# tuple_1[0] = 'art'  # TypeError: 'tuple' object does not support item assignment, Not Allowed in Tuple
# print(tuple_1)
# print(tuple_2)

# cs_courses = {'history', 'math', 'physics', 'compSci'}
# print(cs_courses) # Does not care about order, can be anything at every program execution

# cs_courses = {'history', 'math', 'physics', 'compSci', 'math'}
# print(cs_courses) # Only one math
# Best For member Checking

# print('math' in cs_courses) # True -> Much more optimzied for checking

# Set methods

cs_courses  = {'history', 'math', 'physics', 'compSci'}
art_courses = {'art', 'history', 'math', 'design'} 

print(cs_courses.intersection(art_courses)) # {'math', 'history'}
print(cs_courses.difference(art_courses))   # {'physics', 'compSci'}
print(cs_courses.union(art_courses))        # {'compSci', 'art', 'design', 'history', 'math', 'physics'}

# Creation of Empty List, Tuple, Set

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = ()    # This is wrong way, This is empty dictionary
empty_set = set()
