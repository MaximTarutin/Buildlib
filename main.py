import os
from sys import argv

if __name__ == '__main__':
    filename = argv
    try:
        check_file = os.path.exists(filename[1])
        if check_file:
            command: str = 'ldd ' + filename[1]
            os.system(command)
        else:
            exit()
    except:
        print("Не указано имя файла или такого файла нет ...")
