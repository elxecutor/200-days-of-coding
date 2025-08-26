% Random Practice MATLAB Code

% Generate a random vector of 20 elements between 0 and 1
v = rand(1, 20);

% Compute basic statistics
v_mean = mean(v);
v_median = median(v);
v_std = std(v);

% Find the minimum value and its index
[min_val, min_idx] = min(v);

% Display results
disp('Random Vector v:');
disp(v);
fprintf('Mean: %.4f\n', v_mean);
fprintf('Median: %.4f\n', v_median);
fprintf('Standard Deviation: %.4f\n', v_std);
fprintf('Minimum value: %.4f at index %d\n', min_val, min_idx);

% Plot the vector
figure;
plot(v, 'o-', 'LineWidth', 2);
xlabel('Index');
ylabel('Value');
title('Random Vector Plot');
grid on;