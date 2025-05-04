% Create a 3x3 matrix
A = [1 2 3; 4 5 6; 7 8 9];

% Access the element at row 2, column 3
element = A(2,3);
disp(['Element at row 2, column 3: ' num2str(element)]);

% Extract the entire second row
row2 = A(2,:);
disp('Second row:');
disp(row2);

% Extract the entire third column
col3 = A(:,3);
disp('Third column:');
disp(col3);

% Modify an element: replace element at row 1, column 1 with 10
A(1,1) = 10;
disp('Matrix A after modifying row 1, column 1 to 10:');
disp(A);

% Accessing matrix elements using linear indexing
% MATLAB stores matrices in column-major order; the 5th element corresponds to row 2, column 2
linearElement = A(5);
disp(['Fifth element (linear indexing): ' num2str(linearElement)]);