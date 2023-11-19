#! usr/bin/python3

# Python Logical Operators

"""
The following logical operators are supported by Python language. Assume variable a holds
True and variable b holds False.

We have 3 types of logical operators in python which are:

1. AND ==> If both the operands are true then condition becomes true.
2. OR  ==> If any of the two operands are non-zero then condition becomes true.
3. NOT ==> Used to reverse the logical state of its operand.

"""

# Python Membership Operators

"""
Python’s membership operators test for membership in a sequence, such as strings, lists,
or tuples. There are two membership operators as explained below-

1 - in
2 - not in
"""

a = 10
b = 20

list = [1, 2, 3, 4, 5 ]

if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")
if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")


c=b/a
if ( c in list ):
    print ("Line 3 - a is available in the given list")
else:
    print ("Line 3 - a is not available in the given list")

