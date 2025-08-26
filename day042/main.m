% Day 042: Random Histogram
X = randi(100, 1, 200);
histogram(X, 20);
title('Histogram of Random Integers');
xlabel('Value'); ylabel('Frequency');
