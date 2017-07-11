
        
import time
from utils import factorize_into_primes, primes_up_to

def e3():
    input_number, primes_limit = 600851475143, 10 ** 6
    primes = primes_up_to( primes_limit )
    factors = factorize_into_primes( input_number, primes )
    return max(factors)


if __name__ == '__main__':
    start = time.time()
    print 
    print "Euler 3 solution is:",  e3()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
    