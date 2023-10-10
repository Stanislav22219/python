numbers = input().split()
for n in range(0, len(numbers)):
   numbers[n] = int(numbers[n])
product = 1
for n in numbers:
   product = product * n
print(product)
