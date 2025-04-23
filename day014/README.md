# Day 14: Comparing Square Root Methods

This project compares two popular numerical methods for computing the square root of a number: the Bisection method and the Newton-Raphson method. The implementation is provided in a Jupyter Notebook (`main.ipynb`).

---

## Overview

- **Objective:**  
  Compute the square root of a given number using two different algorithms and compare their performance.
  
- **Methods Compared:**  
  - **Bisection Method:** Iteratively halves the interval containing the root until the approximation error is within a predefined tolerance.
  - **Newton-Raphson Method:** Uses function derivatives to quickly converge to an accurate approximation.
  
- **Use Case:**  
  Understand the trade-offs between the simplicity of the bisection method and the faster convergence of Newton-Raphson.

---

## How It Works

1. **Bisection Method**  
   - Starts with a lower bound (`0`) and an upper bound (`max(1, x)`).
   - Repeatedly computes the midpoint and adjusts the interval until the squared midpoint approximates x within the allowed error (epsilon).

2. **Newton-Raphson Method**  
   - Begins with an initial guess (`x/2` for x ≥ 1, otherwise x).
   - Iteratively refines the guess using the formula:  
     new_guess = guess - (guess² - x) / (2 * guess)  
   - Continues until the change between successive estimates is less than epsilon.

3. **Comparison Function**  
   - Both methods are executed on the same input.
   - The approximated square roots and step counts are returned for side-by-side performance evaluation.

---

## Key Takeaways

- **Algorithm Efficiency:**  
  Newton-Raphson typically converges faster than the bisection method due to its use of derivatives.

- **Robustness:**  
  The bisection method offers guaranteed convergence for continuous functions under the right conditions, making it useful when derivative information is unavailable.

- **Practical Insight:**  
  Comparing these methods provides valuable insights into numerical analysis and algorithm selection based on the problem context.