""" Обработчик get запросов """
import requests
import decorators


@decorators.logging_data
@decorators.test_time
def make_request(url):
    """ Функция обработки get запроса"""
    response = requests.get(f'https://{url}')
    return response.text


if __name__ == '__main__':
    make_request(input())
