from fileTest import math_problem
def welcome(name):
    print("Hello",name)

def goodbye(name):
    print("Goodbye", name)

name = input("Please enter your name:")

welcome(name)
goodbye(name)

x = input("Enter first number:")
y = input("Enter second number:")

math_problem(x,y)



