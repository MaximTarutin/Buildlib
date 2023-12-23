import os
from sys import argv
from typing import List

if __name__ == '__main__':
    filename = argv
    lines = []
    path_in = ""        # путь откуда копируем
    path_out = ""       # путь куда копируем
    try:
        check_file = os.path.exists(filename[1])        # проверяем существует ли файл
        if not check_file:
            exit()
        else:
            command: str = 'ldd ' + filename[1] + ' > out.tmp'
            os.system(command)

# --------------- Парсим файл out.tmp для определения путей и файлов для копирования --------------------

            with open('out.tmp', 'r') as file:
                lines = file.readlines()
            for temp in lines:
                first_index = temp.find('/')
                last_index = temp.rfind('/')
                if first_index != -1 and last_index != -1:
                    path_in = temp[first_index:]
                    path_out = temp[:last_index]
                    path_out = path_out[first_index:] + '/'
                    path_in = path_in.split('.', 1)[0]
                    path_in = path_in + '*'
                print(path_in)
                print(path_out)
                check_file = os.path.exists("buildlib_out/"+path_out)
                if not check_file:
                    os.system('mkdir -p '+path_out)
    except:
        print("Не указано имя файла или такого файла нет ...")
