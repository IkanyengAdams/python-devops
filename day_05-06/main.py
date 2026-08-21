# 1. Operators = a symbol or keyword that tells python to perform an operation on one or more values

# x = 10
# y = 5

# print(x + y)


# 2. Arithmetic operators = used for mathematical calculations

# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# practical example for modulus(remainder)

# number = 11

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")


# 3. Comparison / Realtional operators = compare values andreturn either true or false

# age = 25

# print(age == 25)
# print(age != 25)
# print(age > 25)
# print(age < 25)
# print(age >= 25)
# print(age <= 25)


# 4. Logical oprators = (and, or, not)

# and

# age = 24
# has_id = True

# if age >= 18 and has_id:
#     print("Access granted")


# or

# is_admin = True
# is_owner = False

# if is_admin or is_owner:
#     print("Access granted")


# not

# server_running = True

# if not server_running:
#     print("Server is offline")


# 5. Identity operators (is, is not)

# a = None

# if a is None:
#     print("No value assigned")

# a = None

# if a is not None:
#     print(a)


# 6. Memebership operators = check whether something exists inside a collection or sequence (in, not in)

# servers = ["web-01", "web-02", "database-01"]

# print("web-01" in servers)
# print("web-03" not in servers)

# allowed_regions = ["eu-west-1", "us-east-1"]

# region = "eu-west-1"

# if region in allowed_regions:
#     print("Region is allowed")


# 7. Bitwise operators = work directly with the individual bits of integers

# a = 5
# b = 3

# print(a & b)


# 8. Operator precedence

# general order

# ()
# **
# *, /, //, %
# +, -
# comparisons
# not
# and
# or

# result = 10 + 5 * 2

# print(result)


 # Practical DevOps e.g

# environment = "production"
# port = 443
# https_enabled = True

# if environment == "production" and port == 80 and https_enabled:
#     print("Secure production configuration")
# else:
#     print("Configuration needs attention")

# environments = ["development", "staging", "production"]

# environment = "development"

# if environment in environments:
#     print("Environment is allowed!")