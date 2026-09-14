#!/usr/bin/env python3
import timeit,sys

def data():
    gmails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return gmails * 5

def loop(gmails):
    lopp_list = []
    for i in gmails:
        if '@gmail.com' in i:
            lopp_list.append(i)
    return lopp_list

def list_comprehension(gmails):
    return [email for email in gmails if email.endswith('@gmail.com')]

def map_filtation(gmails):
    return map(lambda email: email if email.endswith('@gmail.com') else None, gmails)

def filter_filtration(gmails):
    return filter(lambda email: email.endswith('@gmail.com'), gmails)

def benchmark(gmails, func, count):
    function = {
        'loop': lambda:loop(gmails),
        'list_comprehension': lambda:list_comprehension(gmails),
        'map': lambda:map_filtation(gmails),
        'filter': lambda: filter_filtration(gmails)
    }    
    return timeit.timeit(function[func], number=count)

def main():
    if len(sys.argv) == 3:    
        gmails = data()
        func = sys.argv[1].lower()

        try:
            count = int(sys.argv[2])
            if count <= 0:
                raise ValueError('Проверьте правильность ввода количества вызовов.')
        except ValueError as e:
            print(f'{e}\nКоличество вызовов должно быть целым положительным числом')
            return
        
        if func in ['loop', 'list_comprehension', 'map', 'filter']:
            print(benchmark(gmails, func, count))

        else:  print('Проверьте правильность ввода имени функции.\nДоступные имена функций: loop, list_comprehension, map, filter')
    else: print('Введите имя функции (loop, list_comprehension, map, filter) и количество вызовов')

if __name__ == '__main__':
    main()