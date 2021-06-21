""" Модуль декораторов"""
import time
import datetime
from functools import wraps


def logging_data(func):
    """ Декоратор записывает входные и выходные данные функции. """
    @wraps(func)
    def wrapper(*args):
        print(f"Входные параметры функции: {args}")
        result = func(*args)
        print(f'Везультат функции - {func.__name__}: {result}')
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
