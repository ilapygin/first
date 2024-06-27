"""
Спочатку потрібно визначити, який день тижня відповідає start_date.
У Python це можна зробити за допомогою методу weekday(), де понеділок = 0, вівторок = 1, і так далі до неділі = 6.
"""
from datetime import datetime, timedelta  # Імпорт необхідних класів datetime і timedelta з бібліотеки datetime

# Функція для перетворення рядкового представлення дати в об'єкт datetime.date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

# Функція для знаходження наступного цільового дня тижня
def find_next_weekday(start_date, target_weekday):
    start_weekday = start_date.weekday()  # Визначення числового представлення поточного дня тижня
    days_ahead = target_weekday - start_weekday  # Обчислення різниці в днях до цільового дня тижня
    if days_ahead <= 0:  # Перевірка, чи потрібно перейти до наступного тижня
        days_ahead += 7
    next_weekday = start_date + timedelta(days=days_ahead)  # Додавання вирахуваних днів(days_ahead) до поточної дати 
    return next_weekday  # Повернення результату

# Початкова дата у рядковому форматі
start_date_str = "2020-01-01"

# Перетворення рядкової дати у об'єкт datetime.date
start_date = string_to_date(start_date_str)

# Знаходження наступного понеділка
next_monday = find_next_weekday(start_date, 0)
print(f"Наступний понеділок: {next_monday}")

# Знаходження наступної п'ятниці
next_friday = find_next_weekday(start_date, 4)
print(f"Наступна п'ятниця: {next_friday}")