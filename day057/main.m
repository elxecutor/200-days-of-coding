
% Day 057: Random Scatter Plot Generation

% Generate random x and y data
x = randn(1, 100);
y = randn(1, 100);

% Plot scatter
figure;
scatter(x, y);
title('Random Scatter Plot');
xlabel('X'); ylabel('Y');
grid on;
