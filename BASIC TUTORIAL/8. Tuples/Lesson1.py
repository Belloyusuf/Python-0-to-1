"""
class tuple([iterable])
    Tuples may be constructed in a number of ways:
        Using a pair of parentheses to denote the empty tuple: ()
        Using a trailing comma for a singleton tuple: a, or (a,)
        Separating items with commas: a, b, c or (a, b, c)
        Using the tuple() built-in: tuple() or tuple(iterable)
"""

# Tuples are immutable

# NOTE :: Note that it is actually the comma which makes a tuple, not the parentheses. 

nums = (1, 2, 3, 4, 5)
print(type(nums))

single_tuple = (2,)
print(type(single_tuple))


t = 'a', 'b', 'c', 'd', 'e'
print(t)
print(t[2])

# slice
print(t[1:3])

tp = tuple('lupins')
print(tp)

t[0] = 'A'
# NOTE TypeError: object doesn't support item assignment