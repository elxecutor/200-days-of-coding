
% Day 075: Random Polynomial Evaluation and Plot

coeffs = randi([-5, 5], 1, 4);
x = linspace(-10, 10, 200);
y = polyval(coeffs, x);
disp('Polynomial coefficients:');
disp(coeffs);
figure;
plot(x, y);
title('Random Polynomial');
xlabel('x'); ylabel('y');
grid on;
