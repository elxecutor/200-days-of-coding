% Day 049: Random Prime Finder
A = randi([1, 100], 1, 20);
primes_in_A = A(isprime(A));
disp('Random Array:'); disp(A);
disp('Prime Numbers:'); disp(primes_in_A);
