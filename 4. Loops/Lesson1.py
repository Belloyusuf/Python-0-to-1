#! usr/bin/python

# LOOP

"""
In general, statements are executed sequentially- The first statement in a function is
executed first, followed by the second, and so on. There may be a situation when you need
to execute a block of code several number of times.

1 - while loop     Repeats a statement or group of statements while a given
                   condition is TRUE. It tests the condition before executing the loop body.

2 - for loop       Executes a sequence of statements multiple times and
                   abbreviates the code that manages the loop variable.

3 - nested loops   You can use one or more loop inside any another while, or for loop.
"""

count = 0

while count < 9:
    print ('The count is:', count)
    count = count + 1

print ("Good bye!")




"""
The Infinite Loop
A loop becomes infinite loop if a condition never becomes FALSE. You must be cautious
when using while loops because of the possibility that this condition never resolves to a
FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop.
"""

var = 1
while var == 1 :
    # This constructs an infinite loop
    num = int(input("Enter a number:"))
    print ("You entered: ", num)

print ("Good bye!")