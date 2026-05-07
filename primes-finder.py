import math
upper_limit = 10

def is_valid(n):
    if not isinstance(n, int): #defensive programming - checks that upper_limit belongs to integer class. Returns bool. Could use type() instead, but not industry standard as bool is a subclass of int and can cause bugs (not in this code)
        raise TypeError(f"Limit must be an integer, but got {n}.") 
    if n <= 1:
        raise ValueError(f"Limit must be greater than 1 to find primes, but got {n}.")
    
    
            
def brute_force_primes(upper_limit):
    """
    Finds all prime numbers up to a specified limit using brute force.
    
    Args:
        limit (int): The upper bound (inclusive) up to which to search for primes.
        
    Returns:
        list: A list of all prime numbers from 2 up to the limit.
    """
    is_valid(upper_limit)
    
    primes = [] 
    
    #check all numbers from 2 up to limit
    for i in range(2, upper_limit + 1):
        #assumes number is prime - to disprove this, must find a factor with 0 remainder!
        is_prime = True
        #checks each factor from 2 up to i - 1: no way that i divided by a number greater than i can lead to 0 remainder
        for j in range(2, i): #check this range: checking for all factors bar 1 and itself
            if i % j == 0: #triggered if there is an exact divisor
                is_prime = False
                break # no point checking anymore j - i definitely cannot be prime
        if is_prime: #if still True after all j have been looped through, must be prime.
            primes.append(i)
    return primes

#does prove that 2 is prime, because 2 % 2 = 0 - doesn't just skip over 2.
# proves that 2 is prime: assumes a number is prime until it finds a factor with 0 remainder. But there are no (integer) factors of 2 between 1 and 2 (itself) - so no factors for remainder to be 0, so must be prime. so for i=2, inner for loop is skipped entirely

primes = brute_force_primes(upper_limit = upper_limit)
print(primes)



def optimised_trial_division_with_2(upper_limit):
    """
    Finds all prime numbers up to a specified limit using trial division.
    Optimised by only checking potential factors up to the square root of the target.
    
    Args:
        limit (int): The upper bound (inclusive) up to which to search for primes.
        
    Returns:
        list: A list of all prime numbers from 2 up to the limit.
    """
    is_valid(upper_limit)
    
    primes = []
    
    for i in range(2, upper_limit + 1): 
        is_prime = True
        max_factor = math.isqrt(i) #isqrt square roots then rounds down!
        for j in range(2, max_factor + 1): #check this range: checking for all factors that aren't 1, and are less than sqrt of itself.
            if i % j == 0: #triggered if there is an exact divisor
                is_prime = False
                break # no point checking anymore j - i definitely cannot be prime
        if is_prime: #if still True after all j have been looped through, must be prime.
            primes.append(i)
    return primes

#still technically proves that 2 is prime: assumes a number is prime until it finds a factor with 0 remainder. But there are no (integer) factors of 2 between 1 and sqrt2 - so no factors for remainder to be 0, so must be prime. explain this better
#for 2: max factor = 1.414, so isqrt = 1, so inner loop is for j in range(2, 2) which never runs, so 2 is prime.
#for 3, max factor = 1.732, so isqrt = 1, so again, inner loop never runs! 
#for pure mathematcis, do we need a method where need to check that 3/2 is not = 0? How to put this in?

#isqrt used: a.) range() requires integers b.) floating point arithemtic can have small roduning errors for larger numbers

#note: small things like defining max factor first then using in range() does not make much difference to algoirhtm speed because python is clever enough to realise this: but better to calculate it once outside anyway to avoid repeatedly doing it inside range.


primes = optimised_trial_division_with_2(upper_limit = upper_limit)
print(primes)


#deliberate technique to improve algorithm time: handle base cases ie 1 not prime, 2 is prime, then find rest.
    
def optimised_trial_division(upper_limit):
    """
    Finds all prime numbers up to a specified limit using trial division.
    Optimised by handling 2 separately, skipping all even numbers, and 
    only checking potential factors up to the square root of the target.
    
    Args:
        limit (int): The upper bound (inclusive) up to which to search for primes.
        
    Returns:
        list: A list of all prime numbers from 2 up to the limit.
    """
    is_valid(upper_limit)
    
    primes = [2] #handles the only even prime immediately
    
    # Start checking at 3, and step by 2 to skip all evens
    for i in range(3, upper_limit + 1, 2):
        is_prime = True
        max_factor = math.isqrt(i)
        
        # We also only need to check odd factors (step by 2)
        for j in range(3, max_factor + 1, 2):
            if i % j == 0:
                is_prime = False
                break
                
        if is_prime:
            primes.append(i)
            
    return primes

#this method assumes 2 is prime, but massively speeds up computation
#assuming 2 is prime eliminates 50% of numbers from checks
#asumming 3 is prime skips roughly 67% of numbers (0.5 are multiples of 2, then 1/3 numbers are multiples of 3 but 0.5 of these already accounted for so do 0.5 + 0.33*0.5 = 2/3), but would need to use more complex loop, but would be quicker:
    #assuming 5 is prime: 0.67 + 1/3 of multiples of 5 = 0.733 numbers skipped! But loop becomes comlex, eventually outweighing skipped numbers
#can assume more primes, but speed increase is diminishing!
#sweet spot is hard coding 2 and 3 - try this! quicker than just hard coding 2? what about 5? for 1,000,000? 

primes = optimised_trial_division(upper_limit = upper_limit)
print(primes) 

def sieve_of_eratosthenes(upper_limit):
    """
    Finds all prime numbers up to a specified limit using the Sieve of Eratosthenes.
    This method avoids division entirely by systematically crossing out multiples 
    of known primes.
    
    Args:
        limit (int): The upper bound (inclusive) up to which to search for primes.
        
    Returns:
        list: A list of all prime numbers from 2 up to the limit.
    """
    is_valid(upper_limit)

    # Create a boolean array, assuming all numbers are prime initially.
    sieve = [True] * (upper_limit + 1)
    
    # 0 and 1 are mathematically not prime, so we cross them out immediately.
    sieve[0] = sieve[1] = False
    
    # We only need to sieve up to the square root of the limit, because: 
    for p in range(2, math.isqrt(upper_limit) + 1):
        # If sieve[p] is still True, p is a prime
        if sieve[p]:
            # Cross out all multiples of p - becomes less discriminatory as p increases
            # We can optimise by starting the crossing out at p squared, 
            # because any smaller multiple (e.g., p * 2) was already crossed out by a smaller prime.
            # We step by p to jump to the next multiple.
            for multiple in range(p * p, upper_limit + 1, p):
                sieve[multiple] = False
                
    # Finally, collect all the indices that remained True
    primes = [p for p in range(2, upper_limit + 1) if sieve[p]]
    
    return primes
#adjusting speed of this one: start crossing out at p**2 rather than p, sieve up to sqrt of limit rather than limit.   
