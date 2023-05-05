# Bitly url shorter

## Описание скрипта

Скрипт выполняет преобразование длинных ссылок в короткую версию с помощью сервиса bitly, а также выводит количество переходов по короткой ссылке. Работа осуществляется через консоль.

## Установка скрипта
Для работы скрипта потребуется установленный Python3.<br>
Установить его можно с официального сайта http://www.python.org

После установки Python3 нужно выполнить эти команды

Для Windows:
```
py -m pip install -r requirements.txt
```

Для Unix/MacOS
```
python -m pip install -r requirements.txt
```
## Запуск скрипта

Для работы скрипта необходимо зарегистрировать на сайте bit.ly и получить ключ к API Bitly<br> (https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-)

Пример ключа - "f036e1e61492ca4ffb2853b4195e5a896ba4fb13"

Создать файл '.env' в папке со скриптом и записать ключ в переменную BITLY_TOKEN.<br>
![image](https://user-images.githubusercontent.com/88648536/235207354-61b73c11-19d8-44b8-87a3-01cb753897bc.png)


Затем выполнить 
```
python3 main.py
```

## Результат выполнения
При вводе длинной ссылки (для сокращения):<br>
![image](https://user-images.githubusercontent.com/88648536/235088292-aff89fab-8900-4991-90af-264f170b8f3c.png)

При вводе короткой ссылки Битлинк (для получения количества кликов):<br>
![image](https://user-images.githubusercontent.com/88648536/235088415-ed4d9c13-ded3-4c39-a417-5620aa86c3f2.png)


## Цель проекта

Код написан для образовательных целей
