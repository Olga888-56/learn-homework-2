"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

people = [
    {'name': 'Olga', 'age': 38, 'job': 'engineer'},
    {'name': 'Mary', 'age': 41, 'job': 'designer'},
    {'name': 'Natalie ', 'age': 39, 'job': 'booker'},
    {'name': 'Anna ', 'age': 37, 'job': 'teacher'}
]

file_name = 'people.csv'

with open('people.csv', 'w', encoding = 'utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for person in people:
        writer.writerow(person)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    main()
