        
import time
from utils import is_pal

def e4():
    begin_range, end_range, max_pal = 100, 1000, 0
    for i in xrange( begin_range, end_range ):
        for j in xrange( i, end_range ):
            if is_pal( i*j ) and i*j > max_pal:
                max_pal = i*j

    return max_pal

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 4 solution is:",  e4()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
