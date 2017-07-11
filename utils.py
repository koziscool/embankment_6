
from collections import defaultdict

def primes_up_to( limit ):
    primes, current_counter = [2], 3
    while primes[-1] < limit:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append( current_counter )
        current_counter += 1
    primes.pop()
    return primes

def first_n_primes( n ):
    primes, current_counter = [2], 3
    while len( primes ) < n:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append( current_counter )
        current_counter += 1
    return primes

def factorize_into_primes( num, primes ):
    factors, primes_index = [], 0
    current_quotient = num
    while current_quotient > 1:
        p = primes[ primes_index ]
        while current_quotient % p == 0:
            current_quotient /= p
            factors.append( p )
        primes_index += 1
    return factors

def num_factors( num, primes ):
    factors_dic = defaultdict(int)
    primes_index = 0
    currentQuotient = num
    while currentQuotient > 1:
        p = primes[ primes_index ]
        while currentQuotient % p == 0:
            currentQuotient /= p
            factors_dic[p] +=1
        primes_index += 1

    ret_val = 1
    for v in factors_dic.values():
        ret_val *= v + 1
    return ret_val

is_pal = lambda n: int(str(n)[::-1]) == n

factorial = lambda n: reduce( lambda x, y: x*y, [1] + range(1, n+1) )
combinations = lambda n, r: factorial(n) / factorial(r) / factorial( n-r )

