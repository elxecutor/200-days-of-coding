# Day 13: Newton's Method for Square Roots

This project implements Newton's method to find the square root of a number. The solution is showcased using a Python Jupyter Notebook.

---

## Overview

In this project, we:
- Prompt the user to enter a number and an initial guess.
- Iteratively refine the approximation using Newton's method.
- Display the iteration count, approximation, function evaluation, and relative error at each step.
- Stop once the error falls below a predefined tolerance.

---

## How It Works

1. **Function Definitions:**  
  The function f(x) = x² - k and its derivative f'(x) = 2x are defined to represent the problem of finding √k.

2. **User Input:**  
  The notebook requests the number to compute its square root and an initial approximation.

3. **Newton’s Iteration:**  
  - The method updates the approximation using:  
    xₖ = xₚ - f(xₚ) / f'(xₚ)
  - Each iteration prints the current approximation, computed function value, and the relative error.
  - The iteration stops when the relative error falls below the given tolerance (TOL).

4. **Output:**  
  The output includes detailed iteration steps, converging to the square root of the given number.
