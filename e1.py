        
import time

def e1():
    end_range = 1000
    return sum(filter( lambda n: n % 3 == 0 or n % 5 == 0, range(1, end_range)))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 1 solution is:",  e1()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
