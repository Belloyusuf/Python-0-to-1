#! usr/bin/python3

# Nested IF Statements

num = int(input("Enter Number"))

if num % 2 == 0:
    if num % 3 ==0:
        print ("Divisible by 3 and 2")
    else:
        print ("Divisible by 2 not divisible by 3")
else:
    if num % 3 == 0:
        print ("Divisible by 3 not divisible by 2")
    else:
        print("Not divisible by 2 not divisible by 3")