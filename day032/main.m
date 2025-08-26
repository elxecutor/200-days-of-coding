% Day 032: Random Matrix Operations
A = randi(50, 6, 6);
row_sum = sum(A, 2);
col_sum = sum(A);
disp('Matrix A:');
disp(A);
disp('Row sums:');
disp(row_sum);
disp('Column sums:');
disp(col_sum);
figure;
bar(row_sum);
title('Row Sums of Matrix A');
xlabel('Row');
ylabel('Sum');
