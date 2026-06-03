# from utils import search
# courses = ['history', 'math', 'physics', 'compSci']
# result = search.find_index(courses, 'math')
# print(result)
# '''
# Imported search module ... 
# 1
# '''
# print(search.find_index([1, 2, 3, 4, 5], 4))  # * 3

## * OR

# from utils.search import find_index
# print(find_index([10, 20, 30], 20)) # * 1

## * Some Semantics

# from utils.search import find_index as fi, test # * We also have access to test variable, If want to import everything use import *, but not good
# print(fi([10, 20, 30], 20))
# print(test) # test string

## * sys module

# import sys
# print(sys.path)
# * ['C:\\Users\\ASUS\\Documents\\Study\\Placement Preparation\\Language\\Python\\corey_schafer_python_tutorials\\02. intermediate\\01. modules', 'C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.14-64\\python314.zip', 'C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.14-64\\DLLs', 'C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib', 'C:\\Users\\ASUS\\AppData\\Local\\Python\\bin', 'C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.14-64', 'C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages']
# These are paths where python looks for module

# * We can also append paths to this list
# sys.path.append('')

# import random
# courses = ['history', 'math', 'physics', 'compSci']
# random_course = random.choice(courses)
# print(random_course)  # * eveytime gives random course

# import datetime, calendar
# today = datetime.date.today()
# print(today)                  # * 2026-06-04
# print(calendar.isleap(2017))  # * False

import os
print(os.getcwd())  # * Prints path of our current directory in which this script is located
print(os.__file__)  # * C:\Users\ASUS\AppData\Local\Python\pythoncore-3.14-64\Lib\os.py

