#! usr/bin/python3


"""
Python variables do not need explicit declaration to reserve memory space. The declaration
happens automatically when you assign a value to a variable. The equal sign (=) is used
to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to
the right of the = operator is the value stored in the variable.
"""

amount = 1000  # An integer Assignment 
miles = 200.0  # An Float Point Assignment
name = "Bello" # A String 

print(amount)
print(miles)
print(name)


# Multiple Assignment
"""
Python allows you to assign a single value to several variables simultaneously.
"""
a = b = c = 1 

print(a)  # The result would be 1
print(b)  # The result would be 1
print(c)  # The result would be 1


# Assign Multiple Objects to Multiple Variables.
a, b, c = 1, 2, "Bello"

print(a)  # The result would be 1
print(b)  # The result would be 2
print(c)  # The result would be Bello