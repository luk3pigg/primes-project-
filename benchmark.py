import time
import prime_algorithms as p

def time_algorithm(algorithm_func, limit):
    """
    Runs a given prime-finding function and measures its execution time.
    
    Args:
        algorithm_func (callable): The function to be tested.
        limit (int): The upper limit to pass to the function.
        
    Returns:
        tuple: (list of primes, time taken in seconds)
    """
    # Start the high-resolution timer
    start_time = time.perf_counter()
    
    # Runs the algorithm
    primes = algorithm_func(limit)
    
    # Stops the timer
    end_time = time.perf_counter()
    
    time_taken = end_time - start_time
    
    return primes, time_taken

if __name__ == "__main__":
    #Set test limit 
    test_limit = 100000 
    
    # Creates dictionary of test algorithms and limit use
    algorithms_to_test = {
        p.brute_force_primes: 100000,
        p.optimised_trial_division_with_2: 1000000
        }
        # optimised_trial_division,
        # sieve_of_eratosthenes
    
    
    results = []
    
    # 3. Run them one at a time and store the data
    print(f"Benchmarking different prime algorithms...\n")
    
    for algo, limit in algorithms_to_test.items():
        # algo.__name__ grabs the name attribute of each function, as a string
        print(f"Running {algo.__name__} up to {limit}...") 
        
        primes, duration = time_algorithm(algorithm_func = algo, limit = limit)
        
        prime_count = len(primes)
        prime_largest = primes[-1] if primes else 0 #this is O(1), whereas max(primes) is O(N) - obvs doesnt matte here because not being timed here. 
        minutes = int(duration // 60)
        seconds = duration % 60
        total_time = f"{minutes}m {seconds:.6f}s"
        
        # Stores the results in a dictionary
        results.append({
            "Name": algo.__name__,
            "Limit": limit,
            "Count": prime_count,
            "Largest": prime_largest,
            "Time": total_time
        })
        
    # Outputs the final formatted table to the terminal
    print("\n--- FINAL RESULTS ---")
    header = (f"{'Algorithm Name':<35} | {'Limit':<10} | {'Primes Found':<15} | {'Largest Prime':<15} | {'Time':<8}")
    print(header)
    print("-" * len(header))
    
    for res in results:
        # The :<35 means "pad this string with spaces so it takes up exactly 35 characters"
        # The :.6f means "format this float to exactly 6 decimal places"
        print(f"{res['Name']:<35} | {res['Limit']:<10} | {res['Count']:<15} | {res['Largest']:<15} | {res['Time']}")