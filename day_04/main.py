# 1. Function = a reusable block of code that performs a particular task, 
# instead of writing the same code repeatedly, 
# you put it inside a function and call that function whenever you need it

# without a function

# print("Hello, Jack")
# print("Hello, Sarah")
# print("Hello, Python")

# Instead

# def greet(name): # parameter (variable defined in the function)
#     print(f"Hello, {name}!")

# greet("Jack") #arguments (actual value passed into the function)
# greet("Sarah")
# greet("Python")

# def add(a, b):
#     print(a + b)

# add(2, 3)


# 2. Returning values = a function deos not always need to print something, 
# sometimes we want it to give us a value back, that is what return is for

# def add(a, b):
#     return(a + b)

# result = add(5, 6)

# print(result)


# 3. Importance of functions = reusability (write once, use many times), organization, maintainability

# def calculate_total(price,quantity):
#     return price * quantity

# total = calculate_total(109.99, 8)

# print(total)


# 4. Modules = a python file containing python code

# import my_module

# result = my_module.square(5)

# print(result)
# print(my_module.pi)


# 5.Giving modules an alias (as)

# import math as m

# print(m.sqrt(25))


# 6. Packages = a way of organizing related python modules into a directory structure

# my_package/
# │
# ├── networking.py
# │       ├── connect()
# │       └── disconnect()
# │
# └── storage.py
#         ├── upload()
#         └── download()

# connect()     → function
# networking.py → module
# my_package    → package


# 7. Python workspaces = the environment where you are developing and running your python project


# 8. Virtual environment = creates an isolated python environment for a project, command to activate is python -m venv myenv

