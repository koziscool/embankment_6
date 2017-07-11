        
import time
from utils import first_n_primes

def e7():
    end_range = 10001
    return first_n_primes( end_range )[-1]

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 7 solution is:",  e7()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
