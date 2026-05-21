# num = 3
# print(type(num))  # <class 'int'>

num = 3.14
print(type(num))  # <class 'float'>

# Arithmetic Operation

print("Division:", 3 / 2)         # 1.5
print("Floor Division:", 3 // 2)  # 1
print("Exponent:", 3 ** 2)        # 9
print("Modulus:", 3 % 2)          # 1
print("Multiplication:", 3 * 1.0) # 3.0

print("round:", round(3.75))                  # 4
print("round to one digit:", round(3.75, 1))  # 3.8

# String to Number

num_1 = '100'
num_2 = '200'
print(num_1 + num_2)  # 100200
# Typecasting
num_1 = int(num_1)
num_2 = int(num_2)
print("After Casting:", num_1 + num_2)  # 300
