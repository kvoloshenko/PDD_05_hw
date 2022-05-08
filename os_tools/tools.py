import os

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
    dir_name = input('   Введите имя папки: ')
    if os.path.exists(dir_name):
        if os.path.isfile(dir_name):
            os.remove(dir_name)
        else: os.rmdir(dir_name)

if __name__ == '__main__':
    create_dir()
    del_dir()