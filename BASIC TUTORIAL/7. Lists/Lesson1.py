

# List

squares = [1, 4, 9, 16, 25]
print(squares, type(squares))


add_more = squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


print(add_more)
print(squares)

# slice 
print(squares[:])

"""
You can also add new items at the end of the list, 
by using the append() method (we will see more about methods later):

"""

cubes = [1, 8, 27, 65, 125]
print(cubes)

cubes.append(216)
print(cubes)


"""
Assignment to slices is also possible, and this can even change 
the size of the list or clear it entirely:

"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

# The built-in function len() also applies to lists: to know the length of the list

letters = ['a', 'b', 'c', 'd']
print(len(letters))


# You can nest the list to form another list 
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)
print(x[0][1])  # In this what we want is display content of `a` and print index 1 which is b
                # So the result would be `b`