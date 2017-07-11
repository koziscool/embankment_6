        
import time
from utils import primes_up_to, num_factors

def e12():
    primes = primes_up_to( 10 ** 6 )
    triangle = lambda n: n * (n+1) / 2

    current_counter = 1
    while num_factors( triangle(current_counter), primes ) <= 500:
        current_counter += 1

    return triangle(current_counter)

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 12 solution is:",  e12()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
