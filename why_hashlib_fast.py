import sys
from time import time_ns as time
import hashlib
import threading


def wrapper2(M, k):
    for i in range(0, k):
        hashlib.sha256(hashlib.sha256(M).digest()).digest()

def test(M):
    start = time()
    for i in range(0, k):
        o2 = hashlib.sha256(hashlib.sha256(M).digest()).digest()
    end    = time()
    endtns2 = (end-start)/k
    endts2  = endtns2 * 1e-9
    print('@hashlib.sha256() Each iteration takes:  {} (ns) and {} (sec).'.format(endtns2, endts2))
    print('@hashlib.sha256() Calculated Hash power: {} (Kh/s)'.format(int(2/endts2/1024)))


    start = time()
    N = 2
    t1 = threading.Thread(target=wrapper2, args=(M, k//N))
    t2 = threading.Thread(target=wrapper2, args=(M, k//N))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end    = time()
    endtns2 = (end-start)/k
    endts2  = endtns2 * 1e-9
    print('@hashlib.sha256() Each iteration takes:  {} (ns) and {} (sec).'.format(endtns2, endts2))
    print('@hashlib.sha256() Calculated Hash power: {} (Kh/s)'.format(int(2/endts2/1024)))

if __name__ == "__main__":

    k = 100000
    for i in range(4):
        M = bytes.fromhex('00000000000000000001d2c45d09a2b4596323f926dcb240838fa3b47717bff6'* (10**i)) #block #548867
        print("byte size {}".format(sys.getsizeof(M)))

        test(M)

