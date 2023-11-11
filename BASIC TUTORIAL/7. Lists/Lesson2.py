

# First Steps Towards Programming

"""
Of course, we can use Python for more complicated tasks than adding two and two together.
For instance, we can write an initial sub-sequence of the Fibonacci series as follows:
"""

# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

"""
LETS BREAK IT DOWN 
First we defined our variable a and b 
a = 0
b = 1
 
while a < 10     ==> which is true
print(a)         ==> this would print 0
a, b = b, a + b  ==> so we assign a, b in b and plus a and b 

0   this is our a
1   this is our b 
1   so a + b = 1
2 <=  1 + 1
3 <=  2 + 1
5 <=  3 + 2
8 <=  5 + 3

"""