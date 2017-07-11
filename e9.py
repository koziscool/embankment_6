        
import time

def e9():
    begin_range, end_range = 5, 1000
    for c in xrange(begin_range, end_range):
        a, b = 1, 1
        while b < c:
            if a*a + b*b == c*c and a+b+c == 1000:
                return a*b*c

            if a < b:
                a += 1
            else:
                a, b = 1, b+1
            

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 9 solution is:",  e9()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
