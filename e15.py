        
import time
from utils import factorial, combinations

def e15():
    pascals_triangle_row = lambda n: [ combinations(n, i) for i in xrange(n+1)]
    end_row = pascals_triangle_row( 20 )
    return sum(map(lambda n: n*n, end_row))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 15 solution is:",  e15()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
