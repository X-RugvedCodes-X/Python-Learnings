my_list = [4, 5, 8, 9, 1, 3, 2, 7, 6, 0]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 

# ^ syntax of list: list[start:end:step] : step = 1 is by default
# print(my_list[-1])    # * 0 -> last   element
# print(my_list[-10])   # * 4 -> first  element

# print(my_list[1:5:2])   # * [5, 9]
# print(my_list[1:8:2])   # * [5, 9, 3, 7]
# print(my_list[::2])     # * [4, 8, 1, 2, 6]
# print(my_list[1:-2])    # * [5, 8, 9, 1, 3, 2, 7]
# print(my_list[1:-2:2])  # * [5, 9, 3, 7]

# print(my_list[1:])  # ^ For Printing all numbers from index 1
# print(my_list[:8])  # * [4, 5, 8, 9, 1, 3, 2, 7] -> upto 8 index

# print(my_list[::-1])  # * [0, 6, 7, 2, 3, 1, 9, 8, 5, 4] -> Reverse
# print(my_list[::1])   # * [4, 5, 8, 9, 1, 3, 2, 7, 6, 0]

# * Similarly Slicing can be done for Strings as well

# * Some other slicing technique and memory reference management of Python
# list_1 = [1, 2, 3]
# list_2 = list_1
# print(list_1 == list_2) # * True -> as expected

# ^ But now if we do something like this
# list_1 = [1, 2, 3]
# list_2 = list_1[:]
# print(list_1) # * [1, 2, 3]
# print(list_2) # * [1, 2, 3]

# # * Now if we check
# print(list_1 == list_2) # * This is True, But
# print(list_1 is list_2) # ! False. Because two different references are created in the Memory, Python is Garbage language and does not reuse the memory like String Constant Pool in Java

# * Even if we do 
# list_1 = [1, 2, 3]
# list_2 = [1, 2, 3]
# print(list_1 == list_2) # * True
# print(list_1 is list_2) # ! False, Same Reason as Earlier

# * Some more Gotcha's in Python
list_1 = [1, 2, 3]
list_2 = list_1
print(list_1, list_2) # * [1, 2, 3] [1, 2, 3]
list_1[0] = 10
print(list_1, list_2) # * [10, 2, 3] [10, 2, 3]
list_2[-1] = 20
print(list_1, list_2) # * [10, 2, 20] [10, 2, 20]

# * But this won't work the same if references are different
