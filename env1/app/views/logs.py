import os
import sys
import fnmatch

def get_logs():
    # criar programa que leia diretorio de logs e retorne lista de logs
    # print('entrei get_logs')
    logs = []
    # file_count = 0
    for file in os.listdir('C:/Users/gabri/Documents/Projects/teste'):
        if file.endswith('.log'):
            logs.append(file)
            # file_count += 1
            print(logs)
    
    return logs


# # @directory example "/usr/lib"
def count_logs_in_directory(directory):
    # _, _, files = next(os.walk(directory))
    # file_count = len(files)
    # return file_count
    file_count = 0
    for file in os.listdir(directory):
        if file.endswith('.log'):
            file_count += 1
            
    return file_count


# def delete_logs_in_directory():
#     pass


# OR

# import fnmatch

# print len(fnmatch.filter(os.listdir(dirpath), '*.txt'))