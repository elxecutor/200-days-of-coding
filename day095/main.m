% Day 095: Random Polynomial Roots
coeffs = randi([-10, 10], 1, 4);
roots_poly = roots(coeffs);
disp('Polynomial Coefficients:'); disp(coeffs);
disp('Roots:'); disp(roots_poly);
