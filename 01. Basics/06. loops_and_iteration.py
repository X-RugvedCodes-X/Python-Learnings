nums = [1, 2, 3, 4, 5]

# for num in nums:
#   print(num, end=" ")   
# * 1 2 3 4 5

# for num in nums:
#   if num == 3:
#     print("Found !")
#     break
#   print(num, end=" ")
# * 1 2 Found !

# ^ continue statement, very easy, no need to write

# * Nested Loop
# for num in nums:
#   for letter in 'abc':
#     print(num, letter, end=" ")
# * 1 a 1 b 1 c 2 a 2 b 2 c 3 a 3 b 3 c 4 a 4 b 4 c 5 a 5 b 5 c

# ^ Commonly used
# for i in range(10):
#   print(i, end= " ")
# * 0 1 2 3 4 5 6 7 8 9

for i in range(1, 11):  
  print(i, end= " ")
# * 1 2 3 4 5 6 7 8 9 10

# * range has
# start: int
# stop: int
# step: int, step means how much to increament or decreament

####################################################################################################
####################################### ^ while loop ^ #############################################
####################################################################################################

# x = 0
# while x < 10:
#   print(x, end=" ")
#   x += 1
# * 0 1 2 3 4 5 6 7 8 9


