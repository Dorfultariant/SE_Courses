def primes(N):
    if N < 1:
        return 0
    # if the N is not less than 1, it means that it is atleast 1 and 1 is a prime so there are atleast 1 primes in the range of N
    nbrPrimes = 1
    # Loop for iterating every integer between 1 and N
    for integer in range(0,N+1):
        isPrime = False
        # Loop for iterating every possible factor for a given integer, as prime can only be divisible by 1 or the number itself, we can start testing from 2nd number and 
            # by using range we need to take that into account with end point 
        for factor in range(2, int(integer/2) + 2):
            # if the remainder is 0 that means that integer is divisible by the factor and thus its not prime and the looping can be stopped for a given integer
            if (integer % factor == 0):
                isPrime = False
                break
            # Integer is prime if the remainder is != 0
            isPrime = True
        # Number of primes is counted.
        if (isPrime):    
            nbrPrimes += 1
    
    return nbrPrimes


if __name__ == "__main__":
    print(primes(70000))
