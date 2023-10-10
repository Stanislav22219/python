numbers = input().split()
for n in range(0, len(numbers)):
   numbers[n] = int(numbers[n])
for n in numbers:
    if (n % 2) == 0:
        print(n, end=', ')
