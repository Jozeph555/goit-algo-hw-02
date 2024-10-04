"""
Цей модуль містить реалізацію стеку та функцію для перевірки симетричності дужок у рядку.

Модуль демонструє використання структури даних стек для вирішення задачі
перевірки правильності розташування дужок різних типів у виразі.
"""


class Stack:
    """
    Клас, що реалізує структуру даних стек.
    """

    def __init__(self):
        """Ініціалізує порожній стек."""
        self.stack = []

    def push(self, item):
        """
        Додає елемент до вершини стеку.

        Args:
            item: Елемент для додавання до стеку.
        """
        self.stack.append(item)

    def pop(self):
        """
        Видаляє та повертає елемент з вершини стеку.

        Returns:
            Елемент з вершини стеку або None, якщо стек порожній.
        """
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def is_empty(self):
        """
        Перевіряє, чи стек порожній.

        Returns:
            bool: True, якщо стек порожній, False - якщо ні.
        """
        return len(self.stack) == 0

    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        """
        Повертає верхній елемент стеку без його видалення.

        Returns:
            Верхній елемент стеку або None, якщо стек порожній.
        """
        if not self.is_empty():
            return self.stack[-1]


def are_brackets_symmetric(some_string: str) -> bool:
    """
    Перевіряє, чи симетрично розташовані дужки у вхідному рядку.

    Args:
        some_string (str): Рядок для перевірки.

    Returns:
        bool: True, якщо всі дужки правильно закриті, False - якщо ні.
    """
    stack = Stack()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in some_string:
        if char in brackets:  # Якщо символ є відкриваючою дужкою
            stack.push(char)
        elif char in brackets.values():  # Якщо символ є закриваючою дужкою
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False  # Неправильна послідовність дужок

    return stack.is_empty()  # Перевіряємо, чи всі дужки закриті


# Тестові випадки
test_cases = [
    '(){[ 1 ]( 1 + 3 )( ){ }}',
    '( 23 ( 2 - 3);',
    '( 11 }',
    '((()))',
    '((())',
    '({[]})',
    '({[}])'
]

# Перевірка кожного тестового випадку
for case in test_cases:
    # Виведення результату перевірки
    print(f"'{case}' is symmetric: {are_brackets_symmetric(case)}")
