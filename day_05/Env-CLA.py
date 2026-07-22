# Environment variables and command line arguments

# import sys
import os

# def add(num1, num2):
#     add = num1 + num2
#     return add

# def sub(num1, num2):
#     sub = num1 - num2
#     return sub

# def mul(num1, num2):
#     mul = num1 * num2
#     return mul

# num1 = float(sys.argv[1])
# operator = sys.argv[2]
# num2 = float(sys.argv[3])

# if operator == "add":
#     output = add(num1, num2)
#     print(output)

# if operator == "sub":
#     output = sub(num1, num2)
#     print(output)

print(os.getenv("password"))
print(os.getenv("apitoken"))