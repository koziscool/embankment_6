
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

is_pal = lambda n: int(str(n)[::-1]) == n
