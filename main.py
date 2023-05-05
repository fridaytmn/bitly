import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    link = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    body = {'long_url': url}
    short_link = requests.post(link, headers=headers, json=body)
    short_link.raise_for_status()
    bitlink = short_link.json()
    return f'Битлинк {bitlink['id']}'


def count_clicks(token, bitlink):
    link = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'unit': 'day',
              'units': '-1',
              'unit_reference': ''}
    clicks_count = requests.get(link, headers=headers, params=params)
    clicks_count.raise_for_status()
    clicks_count = clicks_count.json()
    return clicks_count['total_clicks']


def is_bitlink(url):
    load_dotenv()
    token = os.environ['TOKEN']
    if url.startswith('bit.ly'):
        return f'Количество кликов: {count_clicks(token, url)}'
    else:
        return f'Битлинк {shorten_link(token, url)}'


def main():
    url = input('Введите ссылку: ')
    try:
        print(is_bitlink(url))
    except requests.exceptions.HTTPError:
        print('Введена неверная ссылка Битлинк')
    except requests.exceptions.ConnectionError:
        print('Нет доступа к сайту')


if __name__ == '__main__':
    main()
