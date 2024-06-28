"""
Наступне завдання буде суто теоретичним, і ми потренуємося створювати функції в Python, 
які можуть приймати довільну кількість позиційних або ключових аргументів.

Створіть функцію first, яка приймає один обов'язковий аргумент size та довільну кількість позиційних аргументів. 
Функція має повертати суму: size + кількість позиційних аргументів.

Створіть функцію second, яка також приймає один обов'язковий аргумент size та довільну кількість ключових аргументів. 
Функція має повертати суму: size + кількість ключових аргументів.


"""
def first(size, *args):
    count_args = len(args)
    return size + count_args


def second(size, **kwargs):
    count_kwargs = len(kwargs)
    return size + count_kwargs

print(first(5, "first", "second", "third")) #8
print(first(1, "Alex", "Boris"))             # Результат: 3
print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12
