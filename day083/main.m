% Day 083: Random Polynomial Plot
coeffs = randi([-5, 5], 1, 4);
x = linspace(-10, 10, 200);
y = polyval(coeffs, x);
plot(x, y);
title('Random Polynomial');
xlabel('x');
ylabel('y');
grid on;
