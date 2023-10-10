numbers = input().split()
for n in range(0, len(numbers)):
   numbers[n] = int(numbers[n])
largest = 0
for n in numbers:
    if n > largest:
        largest = n
print(largest)
