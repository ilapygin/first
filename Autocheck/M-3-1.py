"""
На першому кроці ми виконаємо роботу з датами. Мета кроку це ознайомлення з базовими операціями над датами 
які нам знадобляться для цієї задачі.

Напишіть функцію string_to_date, яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" 
і перетворює його на об'єкт datetime.date.
"""


from datetime import datetime

date_string = "2024.01.01"

#date = converted_date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()
    

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

date = string_to_date(date_string)
print(date.strftime('%Y-%m-%d'))
converted_date = string_to_date(date_string)
print(date_to_string(converted_date))

