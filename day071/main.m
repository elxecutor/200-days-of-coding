
% Day 071: Random Matrix and Column Statistics

A = randi(100, 5, 5);
col_mean = mean(A);
col_std = std(A);
disp('Random Matrix A:');
disp(A);
fprintf('Column means: %s\n', mat2str(col_mean));
fprintf('Column standard deviations: %s\n', mat2str(col_std));
