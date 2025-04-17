# Day 9: Understanding Variable Scope in Python

This folder contains a project focused on exploring variable scope in Python, including global, local, and nested scopes.

---

## Overview

The **Variable Scope** project demonstrates how Python handles variables in different scopes:
- **Global Scope**: Variables defined outside any function.
- **Local Scope**: Variables defined within a function.
- **Nested Scope**: Variables defined in nested functions.

The project includes examples to illustrate how variable values are accessed and modified in different scopes.

---

## Learnings and Insights

- **Global Scope**: Variables declared outside functions are accessible throughout the program unless shadowed by local variables.
- **Local Scope**: Variables declared inside a function are limited to that function.
- **Nested Scope**: Inner functions can access variables from their enclosing functions.

---

## Key Takeaways

- Understanding variable scope is crucial for writing clear and bug-free code.
- Nested functions can access variables from their enclosing scope, but changes to those variables require the `nonlocal` or `global` keyword.