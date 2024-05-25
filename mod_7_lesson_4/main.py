import os
import time

directory = '/Users/semras0tresh/Desktop/Dev/urban_lessons/'
count = 0
for dirpath, dirnames, filenames in os.walk(directory):
    count += len(filenames)
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        secs = time.gmtime(os.path.getmtime(full_file_path))
        file_time = f'Дата создания: {secs[2]}-{secs[1]}-{secs[0]}'
        file_size = f'Размер: {os.path.getsize(full_file_path)}'
        par_directore = f'Родительская директория: {os.path.dirname(full_file_path)}'
        print('- - - -  -- - ')
        print(full_file_path, file_time, file_size, par_directore)
