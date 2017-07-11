        
import time

def e14():
    collatz_chain_length_dict = { 1:1, 2:2, 4:3 }

    def collatz_chain_length( n ):
        if n in collatz_chain_length_dict:
            return collatz_chain_length_dict[n]

        if n % 2 == 0:
            length = collatz_chain_length( n / 2) + 1
            collatz_chain_length_dict[n] = length
            return length
        else:
            length = collatz_chain_length( 3*n + 1 ) + 1
            collatz_chain_length_dict[n] = length
            return length

    end_range = 10 ** 6
    max_length, max_starting_number = 1, 1 
    for i in xrange(1, end_range):
        length = collatz_chain_length(i)
        if length > max_length:
            max_length = length
            max_starting_number = i

    return max_starting_number


if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 14 solution is:",  e14()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
