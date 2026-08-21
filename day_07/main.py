# 1. Conditional statements = allows your program to make decisions based
#                             on whether something is true or false

# is_raining = True

# if is_raining:
#     print("Take an umbrella")

# temperature = 30

# if temperature > 25:
#     print("It's hot")

# else statement

# age = 15

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# elif statement

# score = 75

# if score >= 90:
#     print("Excellent")
# elif score >=70:
#     print("Good")
# elif score >=50:
#     print("Pass")
# else:
#     print("Fail")


# 2. Combining conditions (and, or)

# age = 25
# has_id = True

# if age >= 18 and has_id:
#     print("Access granted")
# else:
#     print("Access denied")


# 3. Nested if statements = if statement inside another if statement

# age = 17
# has_id = True

# if age >=18:
#     if has_id:
#         print("Access granted")
#     else:
#         print("ID required")
# else:
#     print("You must be 18 or older")


# 4. Conditions with strings

# environment = "production"

# if environment == "production":
#     print("Running production")
# else:
#     print("Not production")


# 5. Conditions with membership, prctical DevOps e.g

environment = "production"
port = 443
https_enabled = True

if environment == "production" and port == 443 and https_enabled:
    print("Production server is securely configured")
elif environment == "production":
    print("Production server needs security config")
else:
    print("Development orstaging environment")

