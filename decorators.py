""" Модуль декораторов"""
import time
import datetime
from functools import wraps


def logging_data(func):
    """ Декоратор записывает входные и выходные данные функции. """
    input_data = []
    output_data = []

    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        input_data.append(*args)
        output_data.append(result)
        print(f'Входные данные функции - {func.__name__}: {input_data}')
        print(f'Везультат функции - {func.__name__}: {output_data}\n')
    return wrapper


def test_time(func):
    """ Отмечает затраченное время выполнения функции. """
    @wraps(func)
    def wrapper(*args):
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        print(f'Время начала: {current_time}')
        start_time = time.time()
        result = func(*args)
        end_time = time.time() - start_time
        print(f'Время работы функции {end_time} сек\n')
        print(f'Текущее время: {current_time}')
        return result
    return wrapper
