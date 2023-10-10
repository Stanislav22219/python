a = input("Введіть чотиризначне число: ")
k = 0
sum = 0
while k < 4:
    sum += int(str(a)[k])
    k+=1
print(sum)
