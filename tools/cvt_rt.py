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
            print(len(path) * u'---', file, '\t\t',fto)
            os.chdir(root)
            os.rename(file, fto)
            cnt = cnt+1


def convert_kosoburov_lek_syr(fname, outf):
    """
    конвертировать тексты в json
    :param fname:
    :return:
    """
    result = []
    item = {}
    state = 'start'
    with open(fname, 'rt') as fp:
        for ln in fp:
            ln = ln.rstrip()
            if state == 'start':
                item = {"tib_name": ln}
                state = 'property'
            elif state == 'property':
                if ln == "":
                    state = 'start'
                    result.append(item)
                else:
                    iv = ln.split(':')
                    item[iv[0]] = iv[1]

    with open(outf, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)


def main(argv):
    #convert_rt('~/work/spicedb/Растительное сырье/тибетская классификация')
    #convert_rt('~/work/spicedb/Растительное сырье/русская классификация')
    convert_kosoburov_lek_syr('text/Кособуров-сырье-растительное.txt',
                              'text/kosoburov-rast.json')

if __name__ == '__main__':
    main(sys.argv)