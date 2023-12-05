from typing import Tuple
import re

from tablerow import TableRow
import pandas as pd


def wikipedia_test(user_popularity: int) -> Tuple:
    """ Функция-тест"""
    # с помощью pandas достаём таблицы с веб-страницы
    site_object = pd.read_html("https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")
    my_data = site_object[0]
    row_list = []
    error_text = ''
    # С помощью цикла идём по строкам таблицы
    for i, row in my_data.iterrows():
        unique_visitors = row['Popularity (unique visitors per month)[1]']
        if not unique_visitors.isdigit():
            #  С помощью регулярных выражений и функций: join, split преобразовываем строку к нужному нам формату.
            unique_visitors = re.match(r'\d+[,.]\d+[,.]\d+[,.]*\d*', unique_visitors).group(0)
            if '.' in unique_visitors:
                unique_visitors = ''.join(unique_visitors.split('.'))
            else:
                unique_visitors = ''.join(unique_visitors.split(','))
        # Проверяем значение popularity и выводим ошибку, если оно меньше заданного параметра
        if int(unique_visitors) < user_popularity:
            error_text += '{site} (Frontend:{frontend_language}|Backend:{backend_language} ' \
                         'has {unique_visitors} unique visitors per month. (Expected more than {user_number})\n'.format(
                          site=row['Websites'],
                          frontend_language=row['Front-end (Client-side)'],
                          backend_language=row['Back-end (Server-side)'],
                          unique_visitors=unique_visitors,
                          user_number=str(user_popularity))

        # Добавляем в список строк дата класс со значениями из таблицы
        row_list.append(TableRow(website=row['Websites'], popularity=unique_visitors,
                                 frontend=row['Front-end (Client-side)'], backend=row['Back-end (Server-side)'],
                                 database=row['Database'], notes=row['Notes']))
    # Если ошибок не было, то выводим сообщение о том, что ошибок не выявлено
    if error_text == '':
        error_text = 'The check did not reveal any errors.'
    return error_text, row_list
