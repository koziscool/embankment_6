        
import time

number_letter_count = { 
        0:0, 1: 3, 2: 3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
        11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
        20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,
        100: 10, 200: 10, 300: 12, 400: 11, 500:11, 600:10, 700:12, 800:12, 900:11, 1000: 11
    }

def e17():
    def num_letter_length(n):
        if n in number_letter_count:
            return number_letter_count[n]

        if n >= 100:
            hundreds = n / 100
            remainder = n % 100
            return num_letter_length(hundreds * 100) + 3 + num_letter_length(remainder)
        else:
            ones = n % 10
            tens = n / 10
            return num_letter_length( tens * 10 ) + num_letter_length( ones )


    end_range = 1000
    return sum( num_letter_length(i) for i in xrange(1, end_range + 1) )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 17 solution is:",  e17()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
