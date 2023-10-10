import random

a = random.random() * 100
b = random.random() * 100
a = int(a)
b = int(b)
print(a, b)
if a < b:
    for i in range(a, b+1):
        print(i)
elif a > b:
    for i in range(a, b+1, -1):
        print(i)
