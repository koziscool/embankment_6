        
import time
from string_literals import e13_digits_array_string

def e13():
    num_array = [ int(s) for s in e13_digits_array_string.strip().split() ]
    return str( sum(num_array) )[:10]

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 13 solution is:",  e13()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
