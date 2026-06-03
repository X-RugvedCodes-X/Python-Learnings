# def hello_func():
#   pass  # * we dont want to do anything with this for now, just to avoid errors
# print(hello_func) # * <function hello_func at 0x0000019E9C2237F0>
# print(hello_func()) # * None

# def hello_func():
#   print('hello_function')
# # hello_func()  # * hello_function

# for i in range(4):
#   hello_func()
'''
hello_function
hello_function
hello_function
hello_function
'''

# def hello_func():
#   return 'hello_function !'
# print(hello_func()) # *hello_function !

# * Chaining methods 
# print(hello_func().upper()) # HELLO_FUNCTION !

# def greeting(name) -> str:  # * Specifying return type of the function, more specific good practice
#   # return 'hello ' + name  
#   # * better version we know f strings
#   return f'hello {name}'

# print(greeting('rugved')) # * hello rugved

# def greeting(name, gender = 'male') -> str:  # default parameter
#   return f'hello {name}, Your gender is {gender}'
# print(greeting('rugved'))
# print(greeting('rugved', gender='rather not say'))  #* hello rugved, Your gender is rather not say, Another way of passing parameters

# * Some Special types of functions in Python

def student_info(*args, **kwargs): # & This allow us to expect an arbitary number of arguments, args and kwargs is naming convention
  print(args, kwargs)
student_info()  # * () {}
# student_info('Math', 'Art', name = "John", age = 22)
# * ('Math', 'Art') {'name': 'John', 'age': 22}, args is tuple and kwargs is dictionary

# ! Another Case
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(courses, info)     # ^ (['Math', 'Art'], {'name': 'John', 'age': 22}) {}, Doesnot work as we expected it to
student_info(*courses, **info)  # * ('Math', 'Art') {'name': 'John', 'age': 22}

# * Practice Question for Leap Year and Days in a month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year) -> bool:
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month) -> str | int:
  if not 1 <= month <= 12:
    return 'Invalid Month'
  
  if month == 2 and is_leap_year(year):
    return 29
  
  return month_days[month]

print(days_in_month(2017, 2)) # * 28