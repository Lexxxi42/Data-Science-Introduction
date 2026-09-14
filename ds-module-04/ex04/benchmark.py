#!/usr/bin/env python3
import random, timeit
from collections import Counter

def generator():
    return [random.randint(0,100) for _ in range(1000000)]

def my_dict_generator(numbers):
    result = {}
    for i in numbers:
        result[i] = result.get(i,0) + 1
    return result

def my_most_common_num(numbers):
    return sorted(my_dict_generator(numbers).items(), key=lambda item: -item[1])[:10]

def collections(numbers):
    return dict(Counter(numbers))

def most_common(numbers):
    return Counter(numbers).most_common(10)

if __name__ == '__main__':
    numbers = generator()
    num = 100
    
    my_function = timeit.timeit(lambda: my_dict_generator(numbers), number=num)
    my_top = timeit.timeit(lambda: my_most_common_num(numbers), number=num)
    Counter_function = timeit.timeit(lambda: collections(numbers), number=num)
    Counter_top = timeit.timeit(lambda: most_common(numbers), number=num)

    print(f'my function: {my_function}')
    print(f'Counter: {Counter_function}')
    print(f'my top: {my_top}')
    print(f"Counter\'s top: {Counter_top}")