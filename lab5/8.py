amount = int(input('amount: '))
percent = int(input('percent: '))
period = int(input('period: '))
amount_start = amount
for i in range(0, period):
    amount += amount * percent*0.01
profit = int(amount - amount_start)
print(profit)
