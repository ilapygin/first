#імпортуємо модуль символів та рендом
import random
import string

passwd_length = int(input("Введіть кількість символів для паролю: "))

#Створюємо ф-цію для генерації пароля відповідної довжини
def generate_passwd(passwd_length):
    password = ''
    allowed_char = string.ascii_letters + string.digits*4 + string.punctuation #обєднуємо букви, цифри, спец. символи
    
    for i in range(passwd_length): #проходимо по довжині діапазону який задали
        password += random.choice(allowed_char) #створюємо пароль з рандомних значень
    print(password)

generate_passwd(passwd_length)

        

