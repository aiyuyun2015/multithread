#!/usr/bin/python

import threading
import time

# Define a function for the thread
def print_time( start, end):
    ans = 0
    for i in range(start, end, 1):
        ans +=1
    return ans


def test1(number):

    start_time = time.time()
    t1 = threading.Thread(target=print_time, args=(0, number//2))
    t2 = threading.Thread(target=print_time, args=(number//2, number))

    t1.start()
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    print("two threading done")

    run_time = time.time() - start_time
    print("run time {}".format( run_time))

def test2(number):
    start_time = time.time()

    print_time(0, number)
    print("one threading done!")
    run_time = time.time() - start_time
    print("run time {}".format( run_time))

if __name__ == "__main__":
    number = 50000000
    test1(number)
    test2(number)
