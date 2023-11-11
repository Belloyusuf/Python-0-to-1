
# DICTIONARIES

d = {'b':1, 'a':10, 'c':22}
t = list(d.items())
print(t)

# [('b', 1), ('a', 10), ('c', 22)]


d = {'b':1, 'a':10, 'c':22}
t = list(d.items())
print(t)
# [('b', 1), ('a', 10), ('c', 22)]
t.sort()   # ==> means to arange the dict as list
print(t)

# [('a', 10), ('b', 1), ('c', 22)]