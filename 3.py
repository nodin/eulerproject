"""
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

"""

number=600851475143
#solution 1
def prime_factors(n):
    """ Returns all the prime factors of a postive integer"""
    factors = []
    d = 2
    while n>1:
        while n%d == 0:
            factors.append(d)
            n/=d
        d = d+1
    return factors
primes = prime_factors(number)

largest_prime_factor=max(primes)

print 'largest prime  %d', largest_prime_factor
