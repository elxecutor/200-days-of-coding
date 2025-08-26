% Day 098: Random Histogram and Mean/Median Calculation
data = randi(100, 1, 100);
mean_val = mean(data);
median_val = median(data);
histogram(data, 10);
title('Random Histogram');
xlabel('Value');
ylabel('Frequency');
fprintf('Mean: %.2f\n', mean_val);
fprintf('Median: %.2f\n', median_val);
