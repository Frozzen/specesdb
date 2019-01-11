# -*- coding: utf-8 -*-
"""
    разложить синонимы в массив:
        "Синонимы": "танг-ку [5, 13]" -> [танг-ку [5, 13]]
        "Синонимы": "спйи-бжур, шинг-снгон [6], дэ-ба-шинг-снгон [1]", -> ["спйи-бжур", "шинг-снгон [6]", "дэ-ба-шинг-снгон [1]"]



"""
import json
import re
import sys
from pprint import pprint


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


def parce_botanic(data):
    """
        "различают две разновидности канда-ка-ри - канда-ка-ри-дкар-по (канда-ка-ри),
        в качестве которой берутся лишенные кожуры и внутреннего стержня стебли и
        ветки растения Rubus niveus Thunb. /малина снежно-белая/ [6, 8, 13],
        и канда-ка-ри-смуг-по (га-бра), в качестве которой берутся лишенные кожуры и
        внутреннего стержня стебли и ветки растения Rubus subornatus Focke /малина малоукрашенная
        (?)/ [6, 13] или Rubus biflorus Buch.-Ham. ex Sm. /малина двухцветковая/ [7]"  ==>
        {"comment":"различают две разновидности канда-ка-ри - канда-ка-ри-дкар-по (канда-ка-ри)",
            {"comment":"в качестве которой берутся лишенные кожуры и внутреннего стержня стебли и
            ветки растения", "latin_name": "Rubus niveus Thunb", "rus_name": "малина снежно-белая",
             "link": "[6, 8, 13]"
            }
        }

        'Истинное сырье: бивни, желчь (гланг-чхэн-мкхрис), желчные камни (ги-ванг), кровь, мясо и шкура животного
        Elephas maximus L. /слон индийский/ [6, 7, 13]" ==>
        "Истинное сырье": [{"comment":"бивни, желчь", "rrwylee": '(гланг-чхэн-мкхрис)'},
        {"comment":"желчные камни", "rrwylee": '(ги-ванг)'},

        ]

       regexp = r'([а-я\-\s()?]+)?[\s]+([A-z\s.\-]+)?[,]?[\s]?(/[а-я\-\s()?",]+/)?[\s]?(\[[0-9, ]+\])?'
    :param data:
    :return:
    """
    res = []
    regex = re.compile(r'([а-я\-\s()?]+)?[\s]+([A-z\s\.\-^\[]+)?[,]?[\s]?(/[а-я\-\s()?",]+/)?[\s]?(\[[0-9, ]+\])?',
                       re.MULTILINE)
    for item in data:
        if 'Истинное сырье' in item:
            text = item['Истинное сырье']
            r = find_spices_src(regex, res, text)
            item['Истинное сырье'] = r
        if 'Заменитель' in item:
            text = item['Заменитель']
            r = find_spices_src(regex, res, text)
            item['Заменитель'] = r
        res.append(item)
    return res


def find_spices_src(regex, res, text):
    matches = [m.groups() for m in regex.finditer(text)]
    res = []
    for m in matches:
        t = {}
        if m[0] is not None:
            t["comment"] = m[0].strip()
        if m[1] is not None:
            t["rus_name"] = m[1].strip().replace('/','')
        if m[2] is not None:
             t["latin_name"] = m[2].strip()
        if m[3] is not None:
             t["ref"] = m[3].strip()
        if t != {}:
            res.append(t)
    return res


def main(fname):
    with open(fname) as f:
        data = json.load(f)
        # data = extract_equv(data)
        data = parce_botanic(data)
    outf = "kosoburov-rast.json";
    with open(outf, 'w') as fp:
        json.dump(data, fp, ensure_ascii=False)


if __name__ == '__main__':
    main('/home/vovva/PycharmProjects/specesdb/text/kosoburov-rast.json')
