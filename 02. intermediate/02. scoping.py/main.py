'''
LEGB Rule
Local, Enclosing, Global (most important), Built-In
'''

# x = 'global x'
# def test():
#   y = 'local y'
#   print(y)
#   print(x)
# test()
# print(x)

# x = 'global x'
# def test():
#   print(x)
# test()
# print(x)
'''
global x
global x
'''

def test() -> None: 
  global x
  x = 'local x'
  print(x)
test()
print(x)
'''
local x
local x
'''
# * Not to overuse global statement keyword as it may cause confusion among various scopes in the file

