# -*- coding: utf-8 -*-
"""
конвертеры исходных данных база картинок РТ
- исправить имена файлов
"""
import json
import os
import re
import sys
import uuid


def fix_files_in_folder(fpath):
    """
    переименовываем файлы на название растения + cnt - по факту это название последней папки
    :param fpath: нужен абсолютный путь
    :return:
    """
    cdir = os.getcwd()
    for root, dir, files in os.walk(fpath):
        path = root.split(os.sep)
        dirn = os.path.basename(root)
        print((len(path) - 1) * u'---', dirn)
        cnt = 0
        for file in files:
            fname, ext = os.path.splitext(file)
            fto = ("%s-%s%s" % (dirn, str(cnt), ext)).lower()
            print(len(path) * u'---', file, '\t\t', fto)
            os.chdir(root)
            os.rename(file, fto)
            cnt = cnt + 1
    os.chdir(cdir)


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
                    ln = re.sub(r'\[([а-яa-z ]+)\]', r'\1', ln)
                    iv = ln.split(':')
                    if len(iv) == 1:
                        item[last_key] += iv[0]
                    else:
                        last_key = iv[0]
                        item[last_key] = iv[1].strip().replace('"', '')

    with open(outf, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)


def build_rt_syn(fpath, outf, source):
    """
    составить исходник название - аналог по РТ
    :param outf:
    :param fpath:
    :return:
    """
    result = []
    source['GUID'] = uuid.uuid4().hex
    item = source
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


def do_src_index(fpath, outf, source):
    """
    сканируем папку и строим индекс трав в наличии
    :param fpath:
    :param outf:
    :param source:
    :return: {
    "source": {"source":"...", "GUID":"...",
    "herb": ['file1', 'file2']
    }
    """
    uid = source['GUID'] = uuid.uuid4().hex
    result = {"source": source }

    for root, dir, files in os.walk(fpath):
        path = root.split(os.sep)
        dirn = os.path.basename(root)
        if len(files) > 0:
            herb = root.split(os.sep)[-1].lower()
            result[herb] = files

    with open(outf, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)



def main(argv):
    # fix_files_in_folder('~/work/spicedb/Растительное сырье/тибетская классификация')
    # fix_files_in_folder('/home/vovva/work/spicedb/Растительное сырье/русская классификация')
    fix_files_in_folder('/home/vovva/work/spicedb/Ширшов/Фотогербарий')
    # build_rt_syn('/home/vovva/work/spicedb/Растительное сырье/тибетская классификация',
    #              'text/rt-rast.json', {"source": "Ринчен Тензин давал на лекциях аналоги"})
    # do_src_index('/home/vovva/work/spicedb/Растительное сырье/русская классификация',
    #              'text/rt-herb-index.json', {"source": "Ринчен Тензин давал на лекциях аналоги"})
    do_src_index('/home/vovva/work/spicedb/Ширшов/Фотогербарий',
                 'text/shirshov-herb-index.json', {"source": "ширшовский гербарий"})
    # convert_kosoburov_lek_syr('text/Лекарственное сырье тибетской медицины современный взгляд - 2006.txt',
    #                           'text/kosoburov-rast.json')
    # convert_kosoburov_lek_syr('text/Технологическая обработка лекарственного сырья тибетской медицины - 2005-животное.txt',
    #                           'text/kosoburov-process-anim.json')
    # convert_kosoburov_lek_syr('text/Технологическая обработка лекарственного сырья тибетской медицины - 2005-минеральное.txt',
    #                           'text/kosoburov-process-stone.json')


if __name__ == '__main__':
    main(sys.argv)
