# 1. Variable = a name that refers to a value stored in your program.

# name = "Jonas"
# age = 25

# print(name)
# print(age)

# 2. check the type of the vulue

# name = "Jonas"
# age = 25
# is_learning = True

# print(type(name))
# print(type(age))
# print(type(is_learning))


# 3. changig the value of a variable (variable can be reassigned)

# port = 80

# print(port)

# port = 443

# print(port)


# 4. variables can be used in calculations

# price = 100.99
# quantity = 3

# total = price * quantity

# print(total)

# update a variable

# counter = 10

# # counter = counter + 1
# counter += 1

# print(counter)


# 5. variables can reference other variables

# first_name = "Jonas"
# last_name = "Smith"

# full_name = first_name + " " + last_name

# print(full_name)


# 6. variable naming (meaningful names)

# sever_name = "web-server"
# port = 443
# https_enabled = True


# 7. python's snake_case convention

# first_name = "Jonas"
# last_name = "Smith"
# https_enabled = True


# .8 rules for variable names (e.g you cannot start a variable with a number, spaces aren't allowed)

# server1 = "web-server"


# 9. don't use python kewords (use descriptive alternatives, not, class, if, for, while or return)

# server_class = "web"


# 10. variable scope (local vs global scope)

# def my_function():
#     x = 10 # locally scoped not globally
#     print(x)

# my_function()


# 11. global variables

# server_name = "web-server"

# def show_server():
#     print(server_name)

# show_server()

# print(server_name)


# 12. variable lifetime

# scope = where the variable can be accessed
# lifetime = how long the variable exists

# 12. the global keyword = python provides the global keyword when you specifically want to modify a global variable from inside a function.

# counter = 0

# def increment():
#     global counter
#     counter += 1

# increment()

# print(counter)


# 13. variables in a DevOps context = where variables become particularly relevant to cloud

# server_name = "web-server-01"
# port = 80
# is_https_enabled = False
# max_connections = 1000

# print(f"Server Name: {server_name}")
# print(f"Port: {port}")
# print(f"HTTPS Enabled : {is_https_enabled}")
# print(f"Max Connections: {max_connections}")

