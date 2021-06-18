""" Декораторы для функции обработчика. """
import time



def logging_data(func):

    """ Декоратор записывает входные и выходные данные функции. """

    input_data = []
    output_data = []

    def wrapper(*args):
        nonlocal input_data
        nonlocal output_data

        input_data.append(*args)
        result = func(*args)
        output_data.append(result)

        print(f'Входные данные функции - {func.__name__}: {input_data}')
        print(f'Везультат функции - {func.__name__}: {output_data}\n')

    return wrapper

def test_time(func):

    """ Отмечает затраченное время выполнения функции. """

    def wrapper(*args):

        start_time = time.time()
        result = func(*args)
        end_time = time.time() - start_time

        print(f'Время работы функции {end_time} сек\n')

        return result

    return wrapper
