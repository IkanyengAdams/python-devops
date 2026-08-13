# Data Types = In programming, a data type is a classification or categorization that specifies which
#              type of value a variable can hold. Data types are essential because they determine how
#              data is stored in memory and what operations can be performed on that data. Python, like
#              many programming languages, supports several built-in data types. Here are some of the common data types in Python:

# string concatenation

# str1 = "Hello"
# str2 = "World"
# result = str1 + " " + str2
# print(result)

# length keyword

# text = "Python is awesome"
# length = len(text)
# print(f"Lenth of {text} is: {length}")

# upper keyword

# text = "Python is awesome"
# uppercase = text.upper()
# lowercase = text.lower()
# print(f"uppercase: {uppercase}")
# print(f"lowercase: {lowercase}")

# replace keyword

# text = "Python is awesome"
# new_text = text.replace("awesome", "great")
# print(f"Modified text: {new_text}")

# split keyword

# text = "Python is awesome"
# words = text.split()
# print("Words:", words)

# removes space around a text

# text = "        Some spaces around     "
# stripped_text = text.strip()
# print("Stripped_text:", stripped_text)

# checks for a particular word for example in line

# text = "Python is awesome"
# substring = "is"
# if substring in text:
#     print(substring, "found in the text")

# float variables

# num1 = 5.0
# num2 = 2.5

# # Basic Arithmetic
# result1 = num1 + num2
# print("Addition:", result1)

# result2 = num1 - num2
# print("Subtraction:", result2)

# result3 = num1 * num2
# print("Multiplication:", result3)

# result4 = num1 / num2
# print("Division:", result4)

# # Rounding
# result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
# print("Rounded:", result5)


# Integer variables
# num1 = 10
# num2 = 5

# # Integer Division
# result1 = num1 // num2
# print("Integer Division:", result1)

# # Modulus (Remainder)
# result2 = num1 % num2
# print("Modulus (Remainder):", result2)

# Absolute Value
# result3 = abs(-7)
# print("Absolute Value:", result3)

import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")