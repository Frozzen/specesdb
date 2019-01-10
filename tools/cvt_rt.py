# -*- coding: utf-8 -*-
"""
конвертеры исходных данных база картинок РТ
- исправить имена файлов
"""
import json
import os
import sys


def convert_rt(fpath):
    """
    переименовываем файлы на название растения + cnt - по факту это название последней папки
    :param fpath:
    :return:
    """
    for root, dir, files in os.walk(fpath):
        path = root.split(os.sep)
        dirn = os.path.basename(root)
        print((len(path) - 1) * u'---', dirn)
        cnt = 0
        for file in files:
            fname, ext = os.path.splitext(file)
            fto = "%s-%s%s" % (dirn, str(cnt), ext.lower())
            print(len(path) * u'---', file, '\t\t', fto)
            os.chdir(root)
            os.rename(file, fto)
            cnt = cnt + 1


def convert_kosoburov_lek_syr(fname, outf):
    """
    конвертировать тексты в json

    :param fname:
    :return:
    """
    result = []
    item = {}
    state = 'title'
    last_key = ''
    with open(fname, 'rt') as fp:
        for ln in fp:
            ln = ln.rstrip()
            if state == 'title':
                result.append({"source": ln})
                state = 'start'
            elif state == 'start':
                item = {"tib_name": ln.strip()}
                state = 'property'
            elif state == 'property':
                if ln == "":
                    state = 'start'
                    result.append(item)
                else:
                    iv = ln.split(':')
                    if len(iv) == 1:
                        item[last_key] += iv[0]
                    else:
                        last_key =iv[0]
                        item[last_key] = iv[1].strip()

    with open(outf, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)


def build_rt_syn(fpath, outf):
    """
    составить исходник название - аналог по РТ
    :param outf:
    :param fpath:
    :return:
    """
    result = []
    item = {"source": "Ринчен Тензин давал на лекциях"}
    for root, dir, files in os.walk(fpath):
        path = root.split(os.sep)
        dirn = os.path.basename(root)
        level = (len(path) - 1)
        print(level * u'---', dirn)
        if level == 7:
            result.append(item)
            item = {"rwylee": path[-1], "Заменитель": []}
        elif level == 8:
            item['Заменитель'].append(path[-1])

    with open(outf, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)



def main(argv):
    # convert_rt('~/work/spicedb/Растительное сырье/тибетская классификация')
    # convert_rt('~/work/spicedb/Растительное сырье/русская классификация')
    # convert_kosoburov_lek_syr('text/Лекарственное сырье тибетской медицины современный взгляд - 2006.txt',
    #                           'text/kosoburov-rast.json')
    # build_rt_syn('/home/vovva/work/spicedb/Растительное сырье/тибетская классификация',
    #              'text/rt-rast.json')
    # convert_kosoburov_lek_syr('text/Технологическая обработка лекарственного сырья тибетской медицины - 2005-животное.txt',
    #                           'text/kosoburov-process-anim.json')
    convert_kosoburov_lek_syr('text/Технологическая обработка лекарственного сырья тибетской медицины - 2005-минеральное.txt',
                              'text/kosoburov-process-stone.json')


if __name__ == '__main__':
    main(sys.argv)
