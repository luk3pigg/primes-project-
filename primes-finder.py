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
            
            
def brute_force_primes(upper_limit):
    """
    Finds all prime numbers up to a specified limit using brute force.
    
    Args:
        limit (int): The upper bound (inclusive) up to which to search for primes.
        
    Returns:
        list: A list of all prime numbers from 2 up to the limit.
    """
    if not isinstance(upper_limit, int): #defensive programming - checks that upper_limit belongs to integer class. Returns bool. Could use type() instead, but not industry standard as bool is a subclass of int and can cause bugs (not in this code)
        raise TypeError("Limit must be an integer.") 
    if upper_limit <= 1:
        raise ValueError("Limit must be greater than 1 to find primes.")
    
    primes = [] 
    
    #check all numbers from 2 up to limit
    for i in range(2, upper_limit + 1):
        #assumes number is prime - to disprove this, must find a factor with 0 remainder!
        is_prime = True
        #checks each number from 2 up to i - 1: no way that i divided by a number greater than i can lead to 0 remainder
        for j in range(2, i):
            if i % j == 0: #triggered if there is an exact divisor
                is_prime = False
                break # no point checking anymore j - i definitely cannot be prime
        if is_prime: #if still True after all j have been looped through, must be prime.
            primes.append(i)
    return primes

primes = brute_force_primes(upper_limit = upper_limit)
print(primes)

