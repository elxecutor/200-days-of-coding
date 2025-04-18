# day5/cube_root/main.py

import time
import random
import matplotlib.pyplot as plt

def cube_root(n):
    low = 0  # lowest number of the range
    high = n  # highest number of the range
    if n < 0:  # deal with negative case
        low, high = n, 0  # switch the high and low
    epsilon = 1e-3  # minimum allowed deviation
    count = 0  # number of steps taken

    # Binary search for cube root
    while True:
        count += 1
        mid = (low + high) / 2  # midpoint of the range
        mid_cubed = mid ** 3  # cube of the midpoint

        if abs(mid_cubed - n) < epsilon:  # check if the deviation of the cube is within the allowed
            break
        elif mid_cubed < n:  # check if guessed answer is less than the proper answer
            low = mid  # assign the new low to be the midpoint
        else:  # check if guessed answer is greater than the proper answer
            high = mid  # assign the new high to be the midpoint
    return count  # return the number of steps

def measure_step_time(n):  # return the steps and time taken to find the cube root
    start_time = time.time()
    step = cube_root(n)
    end_time = time.time()
    return step, end_time - start_time


if __name__ == "__main__":

    max_digits = 10  # You can set this to any maximum number of digits
    input_sizes, steps, times = [], [], []

    for digits in range(1, max_digits + 1):  # Loop through different number of digits
        number = 10**digits  # Generate random number with 'digits' digits
        step, time_taken = measure_step_time(number)
        input_sizes.append(digits)  # Record the number of digits
        steps.append(step)  # Measure the steps taken
        times.append(time_taken)  # Measure the time taken

    plt.figure(figsize=(14, 6))

    # Plotting the result
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, steps, marker='o')
    plt.xlabel('Number of Digits (n)')
    plt.ylabel('Steps Taken')
    plt.title('Graph of Steps Taken vs Number of Digits')
    plt.grid(True)

    # Plotting the time complexity
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, times, label='Time Complexity O(log n)', marker='o')
    plt.xlabel('Number of Digits (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Complexity of Cube Root Function')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('day5/cube_root/docs/cube_root.png')
