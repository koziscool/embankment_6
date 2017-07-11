        
import time

regular_cal = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }
leap_year_cal = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

def e19():
    def advance_month( year, month, days_from_zero):
        if year % 4 == 0 and year != 1900:
            days_from_zero += leap_year_cal[month]
        else:
            days_from_zero += regular_cal[month]
        return days_from_zero

    num_sundays, days_from_zero = 0, 0
    for year in xrange(1900, 2001):
        for month in xrange(1, 13):
            if year >= 1901 and year <= 2000 and days_from_zero % 7 == 6:
                num_sundays += 1
            days_from_zero = advance_month( year, month, days_from_zero )
    return num_sundays

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 19 solution is:",  e19()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
