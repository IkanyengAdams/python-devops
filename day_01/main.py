# a simple print statement

# print("hello world")

# 1. String Concatenation, A string is text enclosed in quotes.

# first_name = "Jack"
# last_name = "Smith"

# full_name = first_name + " " + last_name

# print(full_name)

# N.B you cannot concatenat a string with an integer, to do so you must convert the interger into a string

# age = 25

# print("I am" + " " + str(age))

# 2. Length = getting string length 

# name = "Jacobs"

# print(len(name))

# (spaces counts as characters too)

# message = "Hello World"

# print(len(message))

# You might use len() to validate user input

# password = "python123"

# if len(password) >= 8:
#     print("password is long enough")


# 3. .lower() = converting every letter in a string to lowercase

# name = "RAYMOND"

# print(name.lower())


# practical example is handling user input

# answer = input("Do you want to continue?: ")

# if answer.lower() == "yes":
#     print("continuing...")
# else:
#     print("stopping")


# 4. .replace = replaces part of a string with something else

# message = "I love Python"

# new_message = message.replace("Python", "AWS")
# print(new_message)

# # You can also replace individual characters

# phone = "123-456-789"

# phone = phone.replace("-", " ")

# print(phone)

# 5. .split = takes one string and turns it into a list of smaller strings

# sentence = "Python is powerful"

# words = sentence.split()

# print(words)

# you can specify what to split on

# data = "Python,Linux,AWS,Docker"

# skills = data.split(",")

# print(skills)


# 6. .strip = removes whitespace from the beginning and end of a string

# name = "    Joseph   "

# print(name.strip())


# username = input("Enter you name: ")

# print(username.strip())

# N.B strip() does not remove spaces in the middle

# name = "Eli zaberth"

# print(name.strip())


# 7. Substrings = a smaller portion of a string

# language = "Python"

# print(language[0:3]) # end index is not inclusive


# 8. Integers = int is a whole number

# age = 25
# quantity = 10
# temperature = -5

# you can perform mathematical operations

# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# you can also explicitly convert something to an integer

# age = "25"

# age = int(age)

# print(age)

# user input example

# age = int(input("How old are you?: "))

# age = age + 1

# print(age)


# 9. Floats = a number containing a decimal value

# price = 99.99
# temperature = 23.5
# pi = 3.14159

# price = 10.99
# quantity = 4

# total = price * quantity

# print(total)

# you can convert values to floats

# price = "99.99"

# price = float(price)

# print(price)


# 10. Regular Expressions = regex allow us to search for patterns inside text

import re

# 11. re.findall() = finds all occurrences matching a pattern

# text = "I have 123 apples and 456 oranges"

# numbers = re.findall(r"\d+", text)

# print(numbers)

# \d = means a digit
# + = means one or more


# 12. re.match() = checks whether a pattern appears at the beginning of the string

# text = "Python is awesome"

# result = re.match(r"Python", text)

# print(result)

# text = "Python is awesome"

# result = re.match(r"AWS", text)

# print(result)


# 13. re.search() = looks through the string for the first occurence of a pattern

# text = "I love Python"

# result = re.search(r"Python", text)

# print(result)


# 14. re.sub() = allows you to replace text matching a pattern

# text = "My phone number is 123456789"

# result  = re.sub(r"\d", "X", text)

# print(result)

# email = "joseph@example.com"

# masked = re.sub(r"[^@]", "*", email)

# print(masked)


# 15. re.split() = splits a string using a regex pattern

text = "Python,Linux;AWS Docker"

result = re.split(r"[,; ]", text)

print(result)
