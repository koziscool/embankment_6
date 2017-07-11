        
import time

from string_literals import e11_raw_num_string

def e11():
    num_lines = e11_raw_num_string.strip().split("\n")
    num_array = []
    for l in num_lines:
        num_line_array = map( lambda s: int(s), l.strip().split() )
        num_array.append( num_line_array )

    array_square_side_length, adjacent_digit_len, max_prod = 20, 4, 0

    for i in xrange(array_square_side_length): 
        for j in xrange(array_square_side_length): 
            downProduct, rightProduct, rDiagProduct, lDiagProduct = 1, 1, 1, 1
            for k in xrange( adjacent_digit_len ):
                if j + k < array_square_side_length:
                    rightProduct *= num_array[i][j+k]
                if i + k < array_square_side_length:
                    downProduct *= num_array[i+k][j]
                if i + k < array_square_side_length and j + k < array_square_side_length:
                    rDiagProduct *= num_array[i+k][j+k]
                if i + k < array_square_side_length and j - k >= 0:
                    lDiagProduct *= num_array[i+k][j-k]

            max_prod = max( max_prod, rightProduct, downProduct, rDiagProduct, lDiagProduct)

    return max_prod

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 11 solution is:",  e11()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
