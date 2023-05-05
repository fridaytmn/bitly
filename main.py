import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    link = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    body = {'long_url': url}
    short_link = requests.post(link, headers=headers, json=body)
    short_link.raise_for_status()
    print(short_link.ok)
    bitlink = short_link.json()
    return bitlink['id']


def count_clicks(token, bitlink):
    try:
        link = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'units': '-1',
                  'unit_reference': ''}
        clicks_count = requests.get(link, headers=headers, params=params)
        clicks_count.raise_for_status()
        clicks_count = clicks_count.json()
    except requests.RequestException:
        return 'Этот битлинк не пренадлежит Вам'
    return f'Количество переходов: {clicks_count["total_clicks"]}'


def is_bitlink(url):
    if url.startswith('http://') or url.startswith('https://'):
        return False
    else:
        response = requests.get(f'http://{url}')
        response.raise_for_status()
        return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    url = input('Введите ссылку: ')
    try:
        if is_bitlink(url):
            print(count_clicks(token, url))
        else:
            print(shorten_link(token, url))
    except requests.ConnectionError:
        print('Сайт недоступен')
    except requests.RequestException:
        print('Неверные данные для запроса')


if __name__ == '__main__':
    main()
