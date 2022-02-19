from multiprocessing import Pool
from multiprocessing import Queue


def cube(number):
    return number * number * number


if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close

    result = pool.map(cube, numbers)    # automatically runs in parallel
    # pool.apply(cube, numbers[0])      # runs only once
    pool.close()
    pool.join()

    print(result)
