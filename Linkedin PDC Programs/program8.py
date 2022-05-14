import os
path = os.getcwd()
print(path)

for i in range(1, 3):
    os.rmdir(path + f"\\{i}")
    # os.mkdir(path + f"\\{i}")