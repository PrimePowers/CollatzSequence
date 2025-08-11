import math

def get_prime_factors(n):
    """
    Finds the prime factors of a number n.
    Returns a list of these factors.
    """
    factors = []
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            while temp_n % d == 0:
                factors.append(d)
                temp_n //= d
        d += 1
    if temp_n > 1:
        factors.append(temp_n)
    return factors

def get_omega(n):
    """
    Calculates the Omega metric for a number n based on the number of
    prime factors of its remainder after subtracting the largest power of 2.
    - Ω is 0 for even numbers.
    - Ω is 0 for odd numbers where the remainder R is 1.
    """
    if n <= 1:
        return 0
    if n % 2 == 0:
        return 0
    
    # Get the largest power of 2 less than n
    power_of_2 = 1 << (n.bit_length() - 1)
    remainder = n - power_of_2
    
    if remainder <= 1:
        return 0
    
    factors = get_prime_factors(remainder)
    
    # The Omega metric is the count of all prime factors of the remainder.
    return len(factors)

def analyze_collatz_with_lyapunov(start_num):
    """
    Analyzes the Collatz sequence and calculates the Lyapunov-like exponent
    based on the change in the Omega metric.
    """
    current_num = start_num
    step_count = 0
    omega_values_for_lyapunov = []
    
    print(f"--- Analysis for starting number: {start_num} ---")
    
    while current_num != 1:
        if current_num % 2 == 0:
            current_num = current_num // 2
            continue
        
        # This is an odd number, calculate Omega and the next odd number
        omega_n = get_omega(current_num)
        step_count += 1
        
        # Determine the next odd number in the sequence
        next_num = (3 * current_num + 1)
        while next_num % 2 == 0:
            next_num //= 2
        
        omega_next_num = get_omega(next_num)

        # Determine the trend of the Omega value
        omega_trend = 'Neutral'
        if omega_next_num > omega_n:
            omega_trend = 'Upward'
        elif omega_next_num < omega_n:
            omega_trend = 'Downward'

        # Print the detailed step for odd numbers
        power_of_2 = 1 << (current_num.bit_length() - 1)
        remainder = current_num - power_of_2
        factors = get_prime_factors(remainder)
        factors_str = ' * '.join(map(str, factors))
        
        decomposition_str = f"{power_of_2} + "
        if len(factors) > 1:
            decomposition_str += f"({factors_str})"
        else:
            decomposition_str += factors_str if factors else '1'
        
        print(f"\nStep{step_count}: Current odd number (n): {current_num} (Ω={omega_n})")
        print(f"  - Decomposition of n: {current_num} = {decomposition_str}")
        print(f"  - Next odd number (n'): {next_num} (Ω={omega_next_num})")
        print(f"  - Ω-Trend: {omega_trend}")

        # Calculate and store the Lyapunov-like value
        if omega_n > 0 and omega_next_num > 0:
            rate_of_change = omega_next_num / omega_n
            omega_values_for_lyapunov.append(math.log(rate_of_change))
        
        current_num = next_num
    
    print("\n--- Sequence reached 1. ---")
    
    total_steps = len(omega_values_for_lyapunov)
    if total_steps > 0:
        average_lyapunov_exponent = sum(omega_values_for_lyapunov) / total_steps
        print(f"\n--- Lyapunov Exponent Calculation Summary ---")
        print(f"The Lyapunov-like exponent measures the average rate of change of the Ω-metric.")
        print(f"It is calculated by summing the natural logarithm of the ratio of consecutive Ω-values.")
        print(f"This sum is then divided by the number of transitions to get the average.")
        print(f"For the sequence starting at {start_num}, the average exponent is: {average_lyapunov_exponent:.4f}")
    else:
        print(f"\nNo odd steps for {start_num} (already 1 reached).")
        
if __name__ == '__main__':
    start_range = 9500001
    analyze_collatz_with_lyapunov(start_range)
    print("\nAnalysis complete.")