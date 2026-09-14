#!/usr/bin/env python3
import timeit

def data():
    gmails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return gmails * 5

def loop(gmails):
    list = []
    for i in gmails:
        if '@gmail.com' in i:
            list.append(i)
    return list

def generator(gmails):
    return [email for email in gmails if '@gmail.com' in email]

def map_generator(gmails):
    return map(lambda email: email if '@gmail.com' in email else None, gmails)

def time():
    number = 90000000
    gmails = data()

    time_loop = timeit.timeit(lambda:loop(gmails), number=number)
    time_generator = timeit.timeit(lambda:generator(gmails), number=number)
    time_map = timeit.timeit(lambda:map_generator(gmails), number=number)
    
    result = {time_loop, time_generator, time_map}

    sorted_result = sorted(result)

    if sorted_result[0] == time_map:
        is_better = 'it is better to use a map'
    elif sorted_result[0] == time_generator:
        is_better = 'it is better to use a list comprehension'
    else:
        is_better = 'it is better to use a loop'

    print(f'{is_better}\n {sorted_result[0]} vs {sorted_result[1]} vs {sorted_result[2]}')

if __name__ == '__main__':
    time()