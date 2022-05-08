import os
import shutil

"""
создание папки
"""
def create_dir():
    dir_name = input('   Введите имя папки: ')
    if not os.path.exists(dir_name):
        # сздать папку передаем путь
        os.mkdir(dir_name)
"""
удаление файла(папки)
"""

def del_dir():
    #print(os.getcwd())
    dir_name = input('   Введите имя папки или файла : ')
    path = os.path.join(os.getcwd(), dir_name)
    #print('path=',path)
    if os.path.exists(path):
        if os.path.isfile(dir_name):
            os.remove(dir_name)
        else: os.rmdir(dir_name)
    else: print('      Файл или папка отсутсвует')

"""
копировать (файл/папку)
"""
def copy_dir():
    #print(os.getcwd())
    dir_name = input('   Введите имя папки или файла: ')
    dir_new = input('   Введите новое имя папки или файла: ')
    if os.path.exists(dir_name):
        if os.path.isfile(dir_name):
            shutil.copy(dir_name, dir_new)
        else: shutil.copytree(dir_name, dir_new, False, None)
    else:
        print('      Файл или папка отсутсвует')

if __name__ == '__main__':
    #del_dir()
    copy_dir()
