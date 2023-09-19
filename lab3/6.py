usd = 28
euro = 32

money = int(input("Введіть суму, яку ви бажаєте обміняти: "))

try:
    currency = int(input("Вкажіть код валюти: (долар - 400, євро - 401): "))
    if currency == 400:
        print(money*usd)
    elif currency == 401:
        print(money*euro)
    else:
        print('Помилка у введенні коду валюти')
except:
    money = -1
    currency = -1
