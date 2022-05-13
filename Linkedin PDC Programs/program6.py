import string

d = {x:y for x,y in enumerate(list(string.ascii_lowercase), 1)}
print(d)