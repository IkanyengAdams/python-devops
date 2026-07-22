 # Arithmetic operators in Python allow you to perform basic mathematical calculations on numeric values.
 #  These operators include addition, subtraction, multiplication, division, and more.

# List of Arithmetic Operators

# 1. **Addition (+):** Adds two numbers.
# 2. **Subtraction (-):** Subtracts the right operand from the left operand.
# 3. **Multiplication (*):** Multiplies two numbers.
# 4. **Division (/):** Divides the left operand by the right operand (results in a floating-point number).
# 5. **Floor Division (//):** Divides the left operand by the right operand and rounds down to the nearest whole number.
# 6. **Modulus (%):** Returns the remainder of the division of the left operand by the right operand.
# 7. **Exponentiation (**):** Raises the left operand to the power of the right operand.

# Addition

a = 5
b = 3
result = a + b
print(result)

# Subtraction

x = 10
y = 7
result = x - y
print(result)

# Multiplication

c = 10
d = 8
result = c * d
print(result)

# Modulus

f = 20
g = 10
result = f % g
print(result)



# Assignment Operations in Python

 # Assignment operators in Python are used to assign values to variables. 
 # They include the basic assignment operator (=) and various compound assignment 
 # operators that perform an operation on the variable while assigning a value.

 # List of Assignment Operators

# 1. **Basic Assignment (=):** Assigns a value to a variable.

# 2. **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.

# 3. **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand.

# 4. **Multiplication Assignment (*=):** Multiplies the left operand by the right operand and assigns the result to the left operand.

# 5. **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand.

# 6. **Floor Division Assignment (//=):** Performs floor division on the left operand and assigns the result to the left operand.

# 7. **Modulus Assignment (%=):** Calculates the modulus of the left operand and assigns the result to the left operand.

# 8. **Exponentiation Assignment (**=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

y = 10
y += 3
print(y)


# Identity Operations in Python

# Identity operators in Python are used to compare the memory locations of two objects to determine if 
# they are the same object or not. The two identity operators are "is" and "is not."

## List of Identity Operators

# 1. **is:** Returns `True` if both operands refer to the same object.
# 2. **is not:** Returns `True` if both operands refer to different objects.

### Examples

#### is Operator


x = [1, 2, 3]
y = x  # y now refers to the same object as x
result = x is y
# result will be True

#### is not Operator


a = "hello"
b = "world"
result = a is not b
# result will be True



# Logical Operations in Python

# Logical operators in Python are used to manipulate and combine Boolean values. 
# These operators allow you to perform logical operations such as AND, OR, and NOT.

## List of Logical Operators

# 1. **AND (and):** Returns `True` if both operands are `True`.
# 2. **OR (or):** Returns `True` if at least one of the operands is `True`.
# 3. **NOT (not):** Returns the opposite Boolean value of the operand.

## Examples

### AND Operator


x = True
y = False
result = x and y
# result will be False


### OR Operator

a = True
b = False
result = a or b
# result will be True



# Relational Operations in Python

# Relational operators in Python are used to compare two values and determine the relationship between them. 
# These operators return a Boolean result, which is either `True` or `False`.

## List of Relational Operators

# 1. **Equal to (==):** Checks if two values are equal.

# 2. **Not equal to (!=):** Checks if two values are not equal.

# 3. **Greater than (>):** Checks if the left operand is greater than the right operand.

# 4. **Less than (<):** Checks if the left operand is less than the right operand.

# 5. **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.

# 6. **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

## Examples

### Equal to


a = 5
b = 5
result = a == b
# result will be True


### Not equal to


x = 10
y = 7
result = x != y
# result will be Tru