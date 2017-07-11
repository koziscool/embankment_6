        
import time
from collections import defaultdict

def e5():
    little_primes = [ 2, 3, 5, 7, 11, 13, 17, 19]
    lcm_factors = defaultdict(int)
    for i in xrange(2, 21):
        current_quotient = i 
        for p in little_primes:
            divisor_count = 0
            while current_quotient % p ==0:
                divisor_count += 1
                if divisor_count > lcm_factors[p]:
                    lcm_factors[p] += 1
                current_quotient /= p

    print lcm_factors
    lcm = 1
    for k, v in lcm_factors.items():
        lcm *= k ** v
    return lcm

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 5 solution is:",  e5()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
