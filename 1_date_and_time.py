"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
#    print(date.today())
    print(date.today() - timedelta(days=1))
    print(date.today() - timedelta(days=30))
    

#    pass


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    
    """
    from datetime import datetime
    date_string = "01/01/20 12:10:03.234567"
    date_format = "%d/%m/%y %H:%M:%S.%f"
    object_date = datetime.strptime(date_string, date_format)
    print(object_date)

#    pass

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
