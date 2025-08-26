% Random Practice MATLAB Code

% Generate a random matrix of size 5x5
A = randi(100, 5, 5);

% Calculate the mean and standard deviation of each column
col_mean = mean(A);
col_std = std(A);

% Find the maximum value and its position
[max_val, idx] = max(A(:));
[row, col] = ind2sub(size(A), idx);

% Display results
disp('Random Matrix A:');
disp(A);
fprintf('Column means: %s\n', mat2str(col_mean));
fprintf('Column standard deviations: %s\n', mat2str(col_std));
fprintf('Maximum value: %d at position (%d, %d)\n', max_val, row, col);

% Plot the matrix as a heatmap
figure;
imagesc(A);
colorbar;
title('Heatmap of Random Matrix A');
xlabel('Column');
ylabel('Row');