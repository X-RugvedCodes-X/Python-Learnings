
# * List Comprehensions
# ^ Problem 1: We want something like this 
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = []
# for n in nums:
#   my_list.append(n)
# print(my_list)  # * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> Fair Enough

# ^ In that Semantic Pytonic Way, we do
# my_list = [n for n in nums] # & Most Important technique
# print(my_list)  # * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = [n * n for n in nums ]
# print(my_list)  # * [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] -> As expected

# ^ Using a Map + Lambda, map is similar to javascript map (works like a function over loop) and lambda is anonymous function
# my_list = map(lambda n: n*n, nums)
# print(my_list)        # * <map object at 0x000002C037DF9A80>
# print(list(my_list))  # * [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
A map object is lazy:
  - It only computes values when you iterate over it.
  - Once consumed (e.g., by list()), it’s exhausted.
'''

# ^ Taking only even numbers using filter + lambda
# my_list = filter(lambda n: n % 2 == 0, nums)
# print(list(my_list))  # * [2, 4, 6, 8, 10]
# my_list = [n for n in nums if n % 2 == 0] # * Easy Way

# ^ Letter Number Pair from 'abcd' something like [a, 1, a, 2, a, 3, b, 1 ...]
# my_list = []
# for letter in 'abcd':
#   for num in range(1, 4):
#     # my_list.append(letter)
#     # my_list.append(num)
#     my_list.append((letter, num))
# # print(my_list)  # * ['a', 1, 'a', 2, 'a', 3, 'b', 1, 'b', 2, 'b', 3, 'c', 1, 'c', 2, 'c', 3, 'd', 1, 'd', 2, 'd', 3]
# print(my_list)  # * [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3), ('d', 1), ('d', 2), ('d', 3)]

# my_list = [(letter, num) for letter in 'abcd' for num in range(1, 4)]
# print(my_list)  # * [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3), ('d', 1), ('d', 2), ('d', 3)]

# * Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# my_dict = {}
# my_list = zip(names, heros)
# print(list(my_list))  # * [('Bruce', 'Batman'), ('Clark', 'Superman'), ('Peter', 'Spiderman'), ('Logan', 'Wolverine'), ('Wade', 'Deadpool')]
# for name, hero in zip(names, heros):  # * zip very important function
#   my_dict[name] = hero
# print(my_dict)  # * {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)  # * {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# * If we want to add certain restrictions
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)  # * {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# ^ Set Comprehensions

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# my_set = set()
# for n in nums:
#   my_set.add(n)
# print(my_set) # * {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set = {n for n in nums}
print(my_set) # * {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ^ Generator Expression
# def gen_func(nums):
#   for n in nums:
#     yield n * n
# my_gen = gen_func(nums)
# print(list(my_gen)) # * [1, 1, 4, 1, 9, 16, 9, 16, 25, 25, 36, 49, 64, 49, 81, 81]

# for i in my_gen:
#   print(i)  # * [1, 1, 4, 1, 9, 16, 9, 16, 25, 25, 36, 49, 64, 49, 81, 81]

my_gen = (n * n for n in nums)
for i in my_gen:
  print(i, end = " ")  # * 1 1 4 1 9 16 9 16 25 25 36 49 64 49 81 81

