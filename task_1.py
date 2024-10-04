"""Програма, яка імітує приймання та обробку заявок"""


import queue
import time
import random

def generate_request(r_queue, r_id):
    """
    Генерує нову заявку та додає її до черги.

    Args:
        r_queue (queue.Queue): Черга для додавання заявок.
        r_id (int): Унікальний ідентифікатор заявки.

    Returns:
        bool: True, якщо заявка успішно додана, False - якщо черга заповнена.
    """
    request_data = f'Заявка № {r_id}'
    try:
        r_queue.put_nowait(request_data)
        print(f'Згенеровано нову заявку {request_data}')
        return True
    except queue.Full:
        print(f'Черга заповнена. Не вдалося додати {request_data}')
        return False

def process_request(r_queue):
    """
    Обробляє заявку з черги, якщо черга не пуста.

    Випадковим чином вирішує, чи обробляти заявку.
    Якщо заявка обробляється, вона видаляється з черги.

    Args:
        r_queue (queue.Queue): Черга з заявками для обробки.
    """
    if not r_queue.empty():
        if random.choice([True, False]):
            request_data = r_queue.get_nowait()
            print(f'Обробка заявки: {request_data}...')
            time.sleep(random.uniform(1.0, 3.0))  # Імітація часу обробки
            print(f'{request_data} успішно оброблена')
        else:
            print('Пропуск обробки заявки')
    else:
        print('Черга пуста. Немає заявок для обробки')

def main():
    """
    Головна функція програми.

    Створює чергу, генерує та обробляє заявки у нескінченному циклі,
    доки користувач не перерве виконання програми ([control] + [c]).
    """
    # Встановлення випадкового максимального розміру черги
    max_size = random.randint(5, 10)

    # Створення черги
    request_queue = queue.Queue(maxsize=max_size)

    # Встановлення початкового значення номеру заявки
    request_id = 0

    print(f'Створено чергу максимальним розміром {max_size}')

    try:
        while True:
            time.sleep(1)# Пауза між ітераціями

            # Спроба генерації нової заявки
            if generate_request(request_queue, request_id + 1):
                request_id += 1

            time.sleep(random.uniform(1.0, 3.0))  # Випадкова затримка

            # Спроба обробки заявки
            process_request(request_queue)

            # Виведення поточного розміру черги
            print(f'Поточний розмір черги: {request_queue.qsize()}')
    except KeyboardInterrupt:
        print('\nПрограма завершена користувачем')

if __name__ == '__main__':
    main()
