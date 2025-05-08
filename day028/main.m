% Generate numbers from 1 to 1000
numbers = 1:1000;
squares = numbers .^ 2;

% Create a figure for the plot
figure;
plot(numbers, squares, 'b-', 'LineWidth', 2);
plot();
xlabel('Number');
ylabel('Square');
title('Squares of Numbers from 1 to 1000');
grid on;