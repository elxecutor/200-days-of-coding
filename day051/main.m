% Day 051: Random Quadratic Equation Solver

% Generate random coefficients for ax^2 + bx + c = 0
a = randi([-10, 10]);
b = randi([-10, 10]);
c = randi([-10, 10]);

% Calculate roots
roots_eq = roots([a b c]);

% Display equation and roots
fprintf('Equation: %dx^2 + %dx + %d = 0\n', a, b, c);
fprintf('Roots: %s\n', mat2str(roots_eq));
