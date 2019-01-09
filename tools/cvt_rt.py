# -*- coding: utf-8 -*-
"""
конвертеры исходных данных база картинок РТ
- исправить имена файлов
"""
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
            fto =  "%s-%s%s" % (dirn, str(cnt), ext.lower())
            print(len(path) * u'---', file, '\t\t',fto)
            os.chdir(root)
            os.rename(file, fto)
            cnt = cnt+1


def convert_kosoburov_lek_syr(fname):
    """
    конвертировать тексты в json
    :param fname:
    :return:
    """
    fp = open(fname, 'rt')
    for ln in fp:
        pass
    fp.close()


def main(argv):
    #convert_rt('~/work/spicedb/Растительное сырье/тибетская классификация')
    #convert_rt('~/work/spicedb/Растительное сырье/русская классификация')
    convert_kosoburov_lek_syr('../text/Кособуров-сырье-растительное.txt')

if __name__ == '__main__':
    main(sys.argv)