# Day 23: Matrix Indexing in MATLAB

This project introduces the basics of creating matrices and accessing their elements using different indexing methods in MATLAB.

---

## Overview

In this project, we explore:
- **Matrix creation:** Defining matrices with explicit values.
- **Indexing methods:** Using row-column indexing, linear indexing, and logical indexing.
- **Submatrix extraction:** Extracting specific portions of a matrix.
- **Modifying elements:** Changing values within a matrix.

---

## Examples

### Creating a Matrix
A 3x3 matrix can be created as follows:
```matlab
A = [1 2 3; 4 5 6; 7 8 9];
```

### Indexing by Row and Column
- Access the element at row 2, column 3:
  ```matlab
  element = A(2,3);
  ```
- Extract the entire second row:
  ```matlab
  row2 = A(2,:);
  ```
- Extract the entire third column:
  ```matlab
  col3 = A(:,3);
  ```

### Modifying Elements
Replace the element at row 1, column 1 with 10:
```matlab
A(1,1) = 10;
```

### Linear Indexing
MATLAB stores matrices in column-major order:
- Access the 5th element (corresponds to row 2, column 2):
  ```matlab
  linearElement = A(5);
  ```
