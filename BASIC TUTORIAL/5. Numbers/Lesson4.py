
# Game on choice

import random

def rand_num():
    ask = input("Enter a number morethan 100:: ")
    for i in enumerate(ask):
        print("Your choiced number is: ", random.choice(i))
        break


if __name__ =="__main__":
    rand_num()