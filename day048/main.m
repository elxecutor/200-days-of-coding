% Day 048: Random Sorting
A = randi(100, 1, 10);
B = sort(A);
disp('Original Array:'); disp(A);
disp('Sorted Array:'); disp(B);
bar(B);
title('Sorted Random Array');
