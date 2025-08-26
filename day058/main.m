
% Day 058: Random Histogram Generation

% Generate random data
data = randi(100, 1, 200);

% Plot histogram
figure;
histogram(data, 20);
title('Random Histogram');
xlabel('Value'); ylabel('Frequency');
