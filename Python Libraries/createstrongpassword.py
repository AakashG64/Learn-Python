import random
from string import digits, punctuation, ascii_letters
# print(ascii_letters,digits,punctuation, sep="\n")
password = ""
symbol = ascii_letters + digits + punctuation
# print(symbol)
secure_random = random.SystemRandom()
for i in range(10):
    password += "".join(secure_random.choice(symbol))

print(password)