
% Day 066: Random Matrix Multiplication and Heatmap

A = randi(10, 3, 3);
B = randi(10, 3, 3);
C = A * B;
disp('Matrix A:'); disp(A);
disp('Matrix B:'); disp(B);
disp('Product C = A * B:'); disp(C);
figure; imagesc(C); colorbar;
title('Product Matrix C');
