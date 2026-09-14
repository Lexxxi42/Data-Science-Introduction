#!/usr/bin/env python3
import timeit, sys
from functools import reduce

def loop(num_of_sum):
    sum = 0
    for i in range(1, 1+num_of_sum):
        sum += i*i
    return sum

def reducing(num_of_sum):
    return reduce(lambda sum, i: sum+i*i, range(1, 1+num_of_sum),0)

def benchmark(func, count_of_call, num_of_sum):
    function = {
        'loop': lambda:loop(num_of_sum),
        'reduce': lambda:reducing(num_of_sum)
    }
    print(reducing(num_of_sum))
    return timeit.timeit(function[func], number=count_of_call)

def main():
    if len(sys.argv) == 4:
        func = sys.argv[1].lower()

        try:
            count_of_call = int(sys.argv[2])
            num_of_sum = int(sys.argv[3])
            
            if count_of_call <= 0 or num_of_sum <= 0:
                raise ValueError('Проверьте правильность ввода количества вызовов.')
            
        except ValueError as e:
            print(f'{e}\nКоличество вызовов должно быть целым положительным числом')
            return
        
        if func in ['loop', 'reduce']:
            print(benchmark(func, count_of_call, num_of_sum))
            
        else:  print('Проверьте правильность ввода имени функции.\nДоступные имена функций: loop or reduce')
    else: print('Введите имя функции (loop or reduce) и количество вызовов. Например, ./benchmark.py loop 10000000 5')

if __name__ == '__main__':
    main()