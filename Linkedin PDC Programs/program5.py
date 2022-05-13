x = [x for x in range(2)]
y = [y for y in range(5) if y % 2 == 1]
z = [(x, y) for x, y in zip(x, y)]
print(z)