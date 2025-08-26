
% Day 052: Random Matrix Determinant and Eigenvalues

% Generate a random 4x4 matrix
A = randi(20, 4, 4);

% Calculate determinant and eigenvalues
det_A = det(A);
eig_A = eig(A);

% Display results
disp('Matrix A:');
disp(A);
fprintf('Determinant: %.2f\n', det_A);
fprintf('Eigenvalues: %s\n', mat2str(eig_A));
