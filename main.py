import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


def shorten_link(token, url):

    headers = {'Authorization': f'Bearer {token}'}
    link = 'https://api-ssl.bitly.com/v4/shorten'
    body = {'long_url': url}
    response = requests.post(link, headers=headers, json=body)
    response.raise_for_status()
    link = response.json()['link']
    return link


def get_striped(url):
    
    parsed_url = urlparse(url)
    return parsed_url.netloc + parsed_url.path


def count_clicks(token, bitlink):
    
    headers = {'Authorization': f'Bearer {token}'}
    params = {'units': '-1',
              'unit_reference': ''}
    short_link = get_striped(bitlink)
    link = f'https://api-ssl.bitly.com/v4/bitlinks/{short_link}/clicks/summary'
    response = requests.get(link, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']

    return clicks_count


def create_parser():
    description = ('Формирует битлинк и считает кол-во переходов по битлинку')
    help = 'Длинная ссылка (одна из 2-ух разновидностей)'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('link', help=help)

    return parser


def is_bitlink(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    short_link = get_striped(url)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{short_link}'
    response = requests.get(url, headers=headers)

    return response.ok


def main():

    load_dotenv()
    
    token = os.environ['BITLY_TOKEN']
    parser = create_parser()
    args = parser.parse_args()
    url = args.link

    try:
        bitlink = is_bitlink(url, token)
        if bitlink:
            print(f'Количество переходов по ссылке: {count_clicks(token, url)}')
        else:
            print(f'Ваш Битлинк: {shorten_link(token, url)}')
    except requests.HTTPError:
        print('Некорректно введеная ссылка')
    except requests.RequestException:
        print('Неверные данные для запроса')


if __name__ == '__main__':
    main()