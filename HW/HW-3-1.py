"""
Створити функцію що приймає дату(рядок), перетворити в тип даних datetime.datetime.strptime(%,-%,-%).date, 
знайти кількість днів від заданої до поточної datetime.datetime.now(), віднімаємо та отримаємо timedelta, атрибут timedelta.days
і покаже кількість днів від заданої до поточної.
"""
#Імпорт класа datetime з модуля datetime
from datetime import datetime

#Отримання дати в рядок за шаблоном
date_string = input("Введіть дату в форматі '2020-10-09': " )

# Функція для конвертації рядка у об'єкт datetime.date з обробкою винятків
def get_days_from_today(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        print(f"Неправильний формат дати: {date_string}. Очікуваний формат: YYYY-MM-DD.")
        return None

# Отримання об'єкта дати з рядка
date_input = get_days_from_today(date_string)
if date_input:
    print("Дата з рядка:", date_input)

    # Отримання сьогоднішньої дати
    date_today = datetime.now().date()
    print("Сьогоднішня дата:", date_today)

    # Обчислення різниці між сьогоднішньою датою і заданою датою
    delta = date_today - date_input
    print("Різниця в днях:", delta.days)
else:
    print("Не вдалося обчислити різницю через неправильний формат дати.")