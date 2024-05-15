import re
import csv


def add(i):
    with open('data.csv', 'a+', newline='') as file:
        write = csv.writer(file, delimiter=";")
        write.writerow(i)


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            data.append(row)
    print(data)
    return data


def remove(i):
    def save(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(j)

    new_list = []
    telephone = i
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            new_list.append(row)
            if re.search(telephone.replace("+", "\+"), row[1]):
                new_list.remove(row)
    save(new_list)


def update(i):
    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(j)

    new_list = []
    telephone = i[0]
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if not re.search(str(telephone).replace("+", "\+"), str(row[1])):
                new_list.append(row)
            else:
                name = i[1]
                telephone = i[2]
                email = i[3]
                address = i[4]
                data = [name, telephone, email, address]
                new_list.append(data)
    update_newlist(new_list)


def search(i):
    data = []
    telephone = i.replace("+", "\+")
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if re.search(telephone, row[1]):
                data.append(row)
            elif re.search(telephone, row[0]):
                data.append(row)
    return data
