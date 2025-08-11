import math
import csv
from datetime import datetime

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

def get_omega_R(n):
    """
    Calculates the Omega_R metric for an odd number n by subtracting the largest
    power of 2 and counting the prime factors of the remainder.
    For even numbers or n<=1, it returns 0.
    """
    if n <= 1 or n % 2 == 0:
        return 0
    
    # Subtract the largest power of 2
    power_of_2 = 1 << (n.bit_length() - 1)
    remainder = n - power_of_2
    
    if remainder <= 1:
        return 0
    
    factors = get_prime_factors(remainder)
    return len(factors)

def analyze_collatz_sequence(start_num):
    """
    Analyzes a single Collatz sequence and returns a dictionary of metrics.
    """
    current_num = start_num
    total_steps = 0
    odd_steps = 0
    max_omega_R = 0
    lyapunov_values = []
    omega_R_increase_count = 0
    omega_R_decrease_count = 0
    omega_R_neutral_count = 0
    
    while current_num != 1:
        total_steps += 1
        
        if current_num % 2 != 0:
            odd_steps += 1
            
            # Omega_R for the current odd number
            omega_current = get_omega_R(current_num)
            max_omega_R = max(max_omega_R, omega_current)
            
            # Determine the next odd number
            next_num = (3 * current_num + 1)
            while next_num % 2 == 0:
                next_num //= 2
            
            # Omega_R for the next odd number
            omega_next = get_omega_R(next_num)
            
            # Track omega_R trend for statistics
            if omega_next > omega_current:
                omega_R_increase_count += 1
            elif omega_next < omega_current:
                omega_R_decrease_count += 1
            else:
                omega_R_neutral_count += 1

            # Calculate and store the Lyapunov-like value if applicable
            if omega_current > 0 and omega_next > 0:
                lyapunov_values.append(math.log(omega_next / omega_current))
            
            current_num = next_num
        else:
            current_num //= 2

    lyapunov_exponent = sum(lyapunov_values) / len(lyapunov_values) if lyapunov_values else 0

    return {
        'start_number': start_num,
        'total_steps': total_steps,
        'odd_steps': odd_steps,
        'max_omega_R': max_omega_R,
        'lyapunov_exponent': lyapunov_exponent,
        'omega_R_increase_count': omega_R_increase_count,
        'omega_R_decrease_count': omega_R_decrease_count,
        'omega_R_neutral_count': omega_R_neutral_count,
        'total_omega_R_transitions': odd_steps -1 if odd_steps > 0 else 0
    }

def main(start_range, end_range, filename='collatz_analysis.csv'):
    """
    Main function to run the analysis over a range and write to CSV.
    """
    all_data = []
    start_time = datetime.now()
    
    # Define the headers for the CSV file
    headers = [
        'start_number', 'total_steps', 'odd_steps', 'max_omega_R', 
        'lyapunov_exponent', 'omega_R_increase_count', 'omega_R_decrease_count',
        'omega_R_neutral_count', 'total_omega_R_transitions'
    ]
    
    print(f"Starting analysis for the range {start_range} to {end_range}...")
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        for i in range(start_range, end_range + 1):
            if i % 1000 == 0:
                print(f"Processing number {i} of {end_range}...")
            
            result = analyze_collatz_sequence(i)
            writer.writerow(result)
            
    end_time = datetime.now()
    print(f"Analysis complete. Data written to {filename}")
    print(f"Total time taken: {end_time - start_time}")

if __name__ == '__main__':
    # Set your desired range here
    START_NUMBER = 9500001
    END_NUMBER = 10000000
    
    main(START_NUMBER, END_NUMBER)