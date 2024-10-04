"""
Цей модуль містить функції для перевірки, чи є рядок паліндромом.

Модуль використовує структуру даних deque з колекцій Python для ефективної
перевірки паліндромів шляхом порівняння символів з обох кінців рядка.
"""


from collections import deque


def make_deque_from_string(some_string: str) -> deque:
    """
    Перетворює вхідний рядок у deque, видаляючи всі символи, крім літер.

    Args:
        some_string (str): Вхідний рядок для перетворення.

    Returns:
        deque: Об'єкт deque, що містить лише літери з вхідного рядка у нижньому регістрі.
    """
    # Створюємо новий рядок, залишаючи тільки літери у нижньому регістрі
    new_string = "".join(ch.lower() for ch in some_string if ch.isalpha())
    # Повертаємо deque, створений з отриманого рядка
    return deque(new_string)


def is_palindrome(queue: deque) -> bool:
    """
    Рекурсивно перевіряє, чи є послідовність символів у deque паліндромом.

    Args:
        queue (deque): Об'єкт deque для перевірки.

    Returns:
        bool: True, якщо послідовність є паліндромом, False - якщо ні.
    """
    # Базовий випадок: якщо в черзі 0 або 1 символ, це паліндром
    if len(queue) <= 1:
        return True

    # Порівнюємо перший і останній символи
    left_char = queue.popleft()
    right_char = queue.pop()
    if left_char != right_char:
        return False

    # Рекурсивно перевіряємо решту символів
    return is_palindrome(queue)


# Тестові випадки
test_cases = [
    'Козак з казок',
    'Я несу гусеня',
    'Аргентина манить негра',
    'Пилип піп пілі пилип',
    'І що сало? Ласощі!',
    'Не паліндром'
]

# Перевірка кожного тестового випадку
for case in test_cases:
    # Виведення результату перевірки
    print(f"'{case}' is palindrome: {is_palindrome(make_deque_from_string(case))}")
