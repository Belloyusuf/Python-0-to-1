#! usr/bin/python3

# Python Identity Operators

"""
Identity operators compare the memory locations of two objects. There are two Identity
operators as explained below:

1 - is
2 - is not

"""

a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

# id()  ==> Identity

if ( a is b ):
    print ("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
    print ("Line 3 - a and b have same identity")
else:
    print ("Line 3 - a and b do not have same identity")


b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is not b ):
    print ("Line 5 - a and b do not have same identity")
else:
    print ("Line 5 - a and b have same identity")