
# Comparian tuples

print((0, 1, 2) < (0, 3, 4))
# True
print((0, 1, 2000000) < (0, 3, 4))
# True

txt = 'but soft what light in yonder window breaks'
words = txt.split()

t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)
    
    
print(res)