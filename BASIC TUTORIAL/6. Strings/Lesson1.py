
# STRING
"""
Besides numbers, Python can also manipulate strings, which can be expressed in several ways. 
They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 
2. \ can be used to escape quotes:
"""

"""
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'
"""

print('spam eggs')   # single quotes
print('doesn\'t')    # use \' to escape the single quote...
print("doesn't")     # ...or use double quotes instead
print('"Yes," they said.')
print('"Isn\'t," they said.')




name = "Bello"    # ==> String
age = "25"       # ==> String
height = "70.5"  # == > String

# Accessing Values in Strings

print(name[2])
print(type(name))
print(type(age))
print(type(height))


# String Formatting Operator
"""
One of Python's coolest features is the string format operator %. This operator is unique
to strings and makes up for the pack of having functions from C's printf() family. Following
is a simple example −
"""

print ("My name is %s and age is %d years" % ('Bello', 25))


# more on string
str = "this is string example....wow!!!"
print ("str.capitalize() : ", str.capitalize())

