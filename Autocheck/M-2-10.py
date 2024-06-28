"""
Напишіть функцію get_fullname на Python, яка приймає ім'я, прізвище та, опціонально, друге ім'я (або по батькові) 
та повертає рядок з повним іменем користувача.
"""
# Отримуємо імена користувача

# Функція для отримання повного імені
def get_fullname(first_name, last_name, middle_name: str=""):
    if middle_name:
        return f'{first_name} {middle_name} {last_name}'
    
    return f'{first_name} {last_name}'

# Викликаємо функцію з введеними значеннями
full_name = get_fullname(first_name, middle_name, last_name)
print(f'{full_name}')

