from multiprocessing import Process
from multiprocessing import Queue


def square(numbers, queue, lock):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue, lock):
    for i in numbers:
        queue.put(-i)


if __name__ == '__main__':

    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    print('end main')
