
# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
sqrt = {x: x**2 for x in (2, 4, 6)}
print(sqrt)

dict(sape=4139, guido=4127, jack=4098)