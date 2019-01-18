# -*- coding: utf-8 -*-
"""
проверяю ссылки между файлами словаря.
"""
import json, sys

def check_rt():
    """
    проверяю ссылки из словаря РТ на индекс, и задно проверяю индекс ширшова
        /home/vovva/PycharmProjects/specesdb/text/shirshov-herb-index.json
        /home/vovva/PycharmProjects/specesdb/text/rt-herb-index.json

    исходный файл из которого идут ссылки
        /home/vovva/PycharmProjects/specesdb/text/rt-rast.json

    выдает несшитые имена и число сколько плохих индексов
    :return:
    """
    json_data = open('text/shirshov-herb-index.json').read()
    sh_idx = json.loads(json_data)

    json_data = open('text/rt-herb-index.json').read()
    rt_idx = json.loads(json_data)

    json_data = open('text/rt-rast.json').read()
    rt_root_ids = json.loads(json_data)
    cnt_rt = cnt_sh = 0
    err_rt = err_sh = 0
    for it in rt_root_ids:
        if not "Заменитель" in it:
            print("%s ?" % (str(it)))
            continue
        for h in it["Заменитель"]:
            if h.lower() in sh_idx:
                cnt_sh = cnt_sh + 1
            else:
                print("%s: not found in shir" % (h))
                err_sh = err_sh + 1
            if h.lower() in rt_idx:
                cnt_rt = cnt_rt + 1
            else:
                print("%s: not found in RT"% (h))
                err_rt = err_rt + 1

    print("*result: {shir:%d-%d, rt:%d-%d}" % (cnt_sh, err_sh, cnt_rt, err_rt))

def main(argv):
    check_rt()

if __name__ == '__main__':
    main(sys.argv)
