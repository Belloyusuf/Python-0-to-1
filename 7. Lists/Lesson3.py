#  List  comprehension,

num = ['42', '65', '12']
list_of_ints = []

for x in num:
    list_of_ints.append(int(x))
    
    
print(sum(list_of_ints))



"""
With list comprehension, the above code can be written in a more compact manner:
"""
num = ['42', '65', '12']
list_of_ints = [ int(x) for x in num ]
print(sum(list_of_ints))