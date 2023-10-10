s = '*'
index = 0
for i in s * 5:
    index += 1
    print(i * index)
for i in s * 4:
    index -= 1
    print(i * index)

