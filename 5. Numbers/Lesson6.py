

# random
import random
# First random number
print ("random() : ", random.random())
# Second random number
print ("random() : ", random.random())


# Seed
random.seed()
print ("random number with default seed", random.random())
random.seed(10)
print ("random number with int seed", random.random())
random.seed("hello",2)
print ("random number with string seed", random.random())

# shuffle 
list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ",
 list)
random.shuffle(list)
print ("Reshuffled list : ",
 list)