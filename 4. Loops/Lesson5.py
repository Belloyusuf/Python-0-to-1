#! usr/bin/python3

Friends = ["Alhaji", "Sule", "Yusuf", "Mansur"]

index = 0

for  f in Friends:
    print(index, f)
    index += 1

# This would display the friend list with the index number. 
# And the index start from 0 up to n





# USING ENUMERATE 
"""
This is the simpler and more decent 
"""
for index, i in enumerate(Friends):
    print(index, i)