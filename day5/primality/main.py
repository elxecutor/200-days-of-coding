# day5/primality/main.py


primes = set() # using set to avoid duplicates

def is_prime(n):
    if n <= 1: # numbers less than or equal to 1 are not prime
        return None
    for i in range(2, int(n**0.5) + 1): # check for factors up to the square root of n to avoid unnecessary multiplications. For example, n = 100, 2 * 50 == 50 * 2.
        if n % i == 0: # check for divisibility
            return None
    return n


count = 0
for i in range(2, 1000000):
    low, high = i, 1000000 - i # get the pair of numbers where low + high = 1000000 to minimize the number of steps, kind of like a binary search
    if i == 1000000 // 2: # since we are checking pairs, we can only search half of the numbers
        break 
    if is_prime(low): # check if the low number is prime
        primes.add(low)
    if is_prime(high): # check if the high number is prime
        primes.add(high)
    count+=1


print(len(primes))
print(count)