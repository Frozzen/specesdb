# -*- coding: utf-8 -*-
"""
    разложить синонимы в массив:
        "Синонимы": "танг-ку [5, 13]" -> [танг-ку [5, 13]]
        "Синонимы": "спйи-бжур, шинг-снгон [6], дэ-ба-шинг-снгон [1]", -> ["спйи-бжур", "шинг-снгон [6]", "дэ-ба-шинг-снгон [1]"]
"""
import json
import sys
from pprint import pprint


def main(fname):
    with open(fname) as f:
        data = json.load(f)
        data = extract_equv(data)


def extract_equv(data):
    """
    разобрать синонимы в словаре
    :param fname:
    :return:
    """
    res = []
    for item in data:
        if 'Синонимы' in item:
            a = [x.strip() for x in item['Синонимы'].split(',')]
            item['Синонимы'] = a
        res.append(item)
    return res


if __name__ == '__main__':
    main('/home/vovva/PycharmProjects/specesdb/text/kosoburov-rast.json')
