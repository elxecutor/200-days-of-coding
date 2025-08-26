
% Day 076: Random Matrix Determinant and Eigenvalues

A = randi(20, 4, 4);
det_A = det(A);
eig_A = eig(A);
disp('Matrix A:');
disp(A);
fprintf('Determinant: %.2f\n', det_A);
fprintf('Eigenvalues: %s\n', mat2str(eig_A));
