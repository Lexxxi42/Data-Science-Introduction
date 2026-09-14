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

def time():
    number = 90000000
    gmails = data()
    time_loop = timeit.timeit(lambda:loop(gmails), number=number)
    time_generator = timeit.timeit(lambda:generator(gmails), number=number)

    if time_generator <= time_loop:
        is_better = 'it is better to use a list comprehension'
        print(f'{is_better}\n{time_generator} vs {time_loop}')
    else:
        is_better = 'it is better to use a loop'
        print(f'{is_better}\n{time_loop} vs {time_generator}')

if __name__ == '__main__':
    time()