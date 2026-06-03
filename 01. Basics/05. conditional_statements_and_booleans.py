# language = 'java'

# Syntax is if... elif ... else...
# if language == 'python':
#   print(f'language is {language}')
# elif language == 'java':
#   print(f'language is {language}')
# else:
#   print('No Match')
# Python does not have switch statements

## Booleans
### and, or, not

# user = 'admin'
# logged_in = True

# if user == 'admin' and logged_in:
#   print('admin page')
# else:
#   print('bad credentials')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a is b) # False, As these are two diffrent objects
# This can be proven by checking their ids
print(id(a))  # 2031913449856
print(id(b))  # 2031913332608

# But if we do 
b = a
print(a is b) # This gives True, as now ids are same as both variable refer to one single object in memory

# ^ False Values: 
# * - False
# * - None
# * - Zero of any numeric type
# * - Any empty sequence, for example '', (), []
# * - Any empty mapping, for exmaple {}
