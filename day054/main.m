
% Day 054: Random Polynomial Evaluation and Plot

% Generate random polynomial coefficients
coeffs = randi([-5, 5], 1, 4);
x = linspace(-10, 10, 200);
y = polyval(coeffs, x);

% Display coefficients
disp('Polynomial coefficients:');
disp(coeffs);

% Plot polynomial
figure;
plot(x, y);
title('Random Polynomial');
xlabel('x'); ylabel('y');
grid on;
