
# ^ input() function is used to take input in Python

# age = input("What is your age ?\n") # * This way everything is stored in string, or <class str>. 
# print(type(age))  # * <class 'str'>

# * Instead do this
age = int(input("What is your age ?\n")) 
print(type(age)) # * <class 'int'>
print(f'hello, your age is {age}') 
