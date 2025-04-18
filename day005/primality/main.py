# day5/primality/main.py

import time
import random
import matplotlib.pyplot as plt

# Primality Check Function with Step Counting
primes = set()  # using set to avoid duplicates

def is_prime(n):
    steps = 0  # Initialize step count
    if n <= 1:  # numbers less than or equal to 1 are not prime
        return None, steps
    for i in range(2, int(n**0.5) + 1):  # check for factors up to the square root of n
        steps += 1  # Increment step for each division attempt
        if n % i == 0:  # check for divisibility
            return None, steps
    return n, steps  # Return the prime number and the step count

# Measure the primality and execution time
def measure_primality_time_and_steps(digits):
    random_number = 10**digits
    start_time = time.time()
    _, steps_taken = is_prime(random_number)  # Get steps taken to check primality
    end_time = time.time()
    time_taken = end_time - start_time
    return steps_taken, time_taken


if __name__ == "__main__":
    max_digits = 100  # Maximum number of digits for generating numbers
    input_sizes, steps, times = [], [], []

    for digits in range(1, max_digits + 1):  # Loop through different number of digits
        step, time_taken = measure_primality_time_and_steps(digits)
        input_sizes.append(digits)  # Record the number of digits
        steps.append(step)  # Record the steps taken
        times.append(time_taken)  # Record the time taken

    # Plotting the results
    plt.figure(figsize=(14, 6))

    # Plot 1: Number of steps taken vs. number of digits
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, steps, marker='o')
    plt.xlabel('Number of Digits (n)')
    plt.ylabel('Steps Taken')
    plt.title('Steps Taken vs Number of Digits')
    plt.grid(True)

    # Plot 2: Time taken vs. number of digits
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, times, marker='o', label='Time Complexity')
    plt.xlabel('Number of Digits (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Taken for Primality Check vs Number of Digits')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('day5/primality/docs/primality_steps_time.png')
