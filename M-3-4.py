from datetime import datetime, timedelta, date

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(users):
    user_list = []
    for user in users:
        birthday = string_to_date(user['birthday'])
        user_dict = {"name": user['name'], "birthday": birthday}
        user_list.append(user_dict)
    return user_list

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()  # Отримуємо поточну дату
    print(today)
    
    for user in users:
        birthday = user['birthday']
        # Розраховуємо день народження для поточного року
        next_birthday = datetime(today.year, birthday.month, birthday.day).date()

        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        # Розраховуємо різницю в днях до наступного дня народження
        days_until_birthday = (next_birthday - today).days

        # Якщо днів до наступного дня народження менше або дорівнює days, додаємо в список
        if days_until_birthday <= days:
            congratulation_date = date_to_string(next_birthday)
            upcoming_birthdays.append({"name": user['name'], "congratulation_date": congratulation_date})

    return upcoming_birthdays

# Приклад використання:
users = [
   {"name": "Bill Gates", "birthday": "1955.3.25"},
   {"name": "Steve Jobs", "birthday": "1955.3.21"},
   {"name": "Jinny Lee", "birthday": "1956.3.22"},
   {"name": "John Doe", "birthday": "1985.01.23"},
   {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# Підготовка списку користувачів з їхніми днями народження
prepared_users = prepare_user_list(users)

# Визначення майбутніх днів народження для користувачів протягом 7 днів
upcoming_birthdays = get_upcoming_birthdays(prepared_users, days=7)

# Виведення результату
print(upcoming_birthdays)
