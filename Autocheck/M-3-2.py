"""
Напишіть функцію prepare_user_list, яка приймає список імен користувачів та їх дат народження у рядковому форматі,
і повертає список словників у форматі {"name": <name>, "birthday": <birthday>}, де <birthday> - це об'єкт datetime.date
"""

from datetime import datetime
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def prepare_user_list(user_data):
    user_list = []
    for user in user_data:
        user_name = user["name"]
        user_birthday = user["birthday"]
        birthday = string_to_date(user_birthday)
        user_dict = {"name": user_name, "birthday": birthday}
        user_list.append(user_dict)
    return user_list

prepared_users = prepare_user_list(users)
print(prepared_users)



"""
def get_upcoming_birthdays(users, days=7):
   upcoming_birthdays = []
   today = date.today()
   for user in users:
       birthday_this_year = user["birthday"].replace(year=today.year)
       if birthday_this_year < today:
           birthday_this_year = user['birthday'].replace(year= today.year+1)
       if 0 <= (birthday_this_year - today).days <= days:
           week_birthday = adjust_for_weekend(birthday_this_year)  
           congratulation_date_str = date_to_string(week_birthday)
           upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
   return upcoming_birthdays
"""