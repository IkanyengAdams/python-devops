# print("project-xyz-instance")

ec2_instance_name = "project-xyz-instance"

print(ec2_instance_name)

# local variables vs global variables

a = 5 # global variable
b = 10 # global variable

def add():
    c = 5 # local variable
    print(a + b + c)

def sub():
    print(a - b)

add()
sub() 