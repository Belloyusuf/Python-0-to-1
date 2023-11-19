

#  Random Number Functions

"""
Random numbers are used for games, simulations, testing, security, and privacy
applications. Python includes the following functions that are commonly used.

choice(seq)                        A random item from a list, tuple, or string.
randrange ([start,] stop [,step])  A randomly selected element from range(start, stop, step).
random()                           A random float r, such that 0 is less than or equal to r and r is less than 1.

seed([x])                          Sets the integer starting value used in generating random numbers. 
                                   Call this function before calling any other random module function. Returns None.
shuffle(lst)                       Randomizes the items of a list in place. Returns None.
uniform(x,y)                       A random float r, such that x is less than or equal to r and r is less than y.
 
"""

import random

# # random.choice()
# print ("returns a random number from range(100) : ",random.choice(range(100)))
# print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
# print("returns random character from string 'Hello World' :", random.choice('Hello World'))



def rand_num():
    ask = input("Enter a number morethan 100:: ")
    for i in enumerate(ask):
        print("Your choiced number is: ", random.choice(i))
        break


rand_num()
