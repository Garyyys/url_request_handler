""" Обработчик get запросов """
import requests
import decorators


@decorators.test_time
@decorators.logging_data
def make_request(url):
    """ Функция обработки get запроса."""
    response = requests.get(f'https://{url}')
    return response.text


if __name__ == '__main__':
    make_request(input())
