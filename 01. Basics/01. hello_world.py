# Print Welcome Message
# message = 'hello, world'
# message = 'bobby\'s world'
# message = "bobby's world"
# message = """Bobby is a nice boy
# Bobby Madarchod"""

# print("message:", message)
# print("Length of message:", len(message))

# Accessing Characters through Index
# message = 'hello, world'
# print(message[0:5]) # hello, 0 included 5 excluded
# print(message[:5])  # hello, defualt start by 0

# print(message[7:])  # Similar Analogy, goes till end from 7, This is called Slicing

# String Methods
# print(message.upper())  # HELLO, WORLD
# print(message.count("l"))  # 3, Counts Number of Occurences
# print(message.find("world"))  # 7, finds a string in a string

# new_message = message.replace("world", "universe")  # Returns a new string
# print(new_message)


########################################################################################
###############################   String Concatenation   ###############################
########################################################################################

greeting = 'hello'
name = 'dada'
# message = greeting + ' ' + name # hello dada

# Formatted Strings
# message = '{}, {}. Welcome!'.format(greeting, name) # hello, dada. Welcome!

# f Strings
# message = f'{greeting}, {name}. Welcome!' # Best Method
message = f'{greeting}, {name.upper()}. Welcome!' # On the Fly Function Usage, More Convenient
# print(message)

# Some Useful Function
# 1. dir()

# print(dir(name)) # Shows all attributes and methods available to us
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# print(help(str))  # Like docs
# print(help(str.lower))  # Works even for specific functions