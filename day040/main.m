% Day 040: Random Matrix Multiplication
A = randi(10, 3, 3);
B = randi(10, 3, 3);
C = A * B;
disp('Matrix A:'); disp(A);
disp('Matrix B:'); disp(B);
disp('Product C = A * B:'); disp(C);
figure; imagesc(C); colorbar;
title('Product Matrix C');
