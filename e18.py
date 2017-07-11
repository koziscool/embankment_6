        
import time
from string_literals import e18_triangle_string

def e18():
    lines = e18_triangle_string.strip().split('\n')
    numbers, max_path_sum = [], []
    for s in lines:
        numbers.append( [int(c) for c in s.strip().split(' ') ] ) 
        max_path_sum.append( [ 0 for c in s.strip().split(' ') ] )

    def max_path_rows_up_to( limit_row ):
        for i in xrange( limit_row ):
            if i == 0:
                max_path_sum[i][i] = numbers[i][i]
            for j in xrange(i+1):
                if j == 0:
                    max_path_sum[i][j] = max_path_sum[i-1][j] + numbers[i][j]
                if j == i:
                    max_path_sum[i][j] = max_path_sum[i-1][j-1] + numbers[i][j]
                if j > 0 and j < i:
                    max_path_sum[i][j] = max( max_path_sum[i-1][j], max_path_sum[i-1][j-1] )  + numbers[i][j]
        return max( max_path_sum[ limit_row - 1])
                    
    return max_path_rows_up_to( len(numbers) )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 18 solution is:",  e18()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
