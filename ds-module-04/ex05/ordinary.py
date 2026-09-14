#!/usr/bin/env python3
import sys, os
import resource

def read(file_path):
    with open(file_path,'r') as file:
        return file.readlines()

def main(file_path):
    for i in read(file_path):
        pass

def process_analyze():
    process = resource.getrusage(resource.RUSAGE_SELF)
    print(f"Peak Memory Usage = {process.ru_maxrss/1024**2 :.3f} GB")
    print(f'User Mode Time + System Mode Time = {process.ru_utime + process.ru_stime :.2f}s')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_path = sys.argv[1]

        if os.path.exists(file_path):
            main(file_path)
            process_analyze()
        else: print('Файл не существует.')
    else: print('Ведите название файла.')