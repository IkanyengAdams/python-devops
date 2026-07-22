# num1 = 10
# num2 = 5

# def add():
#     add = num1 + num2
#     print(add)

# def sub():
#     sub = num1 - num2
#     print(sub)

# def mul():
#     mul = num1 * num2
#     print(mul)

# add()
# sub()

# using the return keyword and adding outputs to the function


def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

print(add(5, 10))
print(sub(10, 5))
print(mul(2, 3))