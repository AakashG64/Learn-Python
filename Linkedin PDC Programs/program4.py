lst = [1, 2, 3, 3]
s = set(lst)
d = {k:v for k, v in zip(s, s)}
print(d)