import math
upper_limit = 10

# #1.) brute force baseline method
# primes = []
# for i in range(lower_lim, upper_lim + 1):
#     j = lower_lim
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#         primes.append(i)
 
    
# print(primes)
           
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
        for j in range(2, i):
            if i % j == 0: #triggered if there is an exact divisor
                is_prime = False
                break # no point checking anymore j - i definitely cannot be prime
        if is_prime: #if still True after all j have been looped through, must be prime.
            primes.append(i)
    return primes

#does prove that 2 is prime, because 2 % 2 = 0 - doesn't just skip over 2.

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
        max_factor = math.isqrt(i) # does defining this outside slow down program
        for j in range(2, max_factor + 1):
            if i % j == 0: #triggered if there is an exact divisor
                is_prime = False
                break # no point checking anymore j - i definitely cannot be prime
        if is_prime: #if still True after all j have been looped through, must be prime.
            primes.append(i)
    return primes

#still proves that 2 is prime

primes = optimised_trial_division_with_2(upper_limit = upper_limit)
print(primes)
    
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

primes = optimised_trial_division(upper_limit = upper_limit)
print(primes) 

    
