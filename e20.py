        
import time
from utils import factorial

def e20():
    return sum( map(lambda c: int(c), str(factorial(100)) ))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 20 solution is:",  e20()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
