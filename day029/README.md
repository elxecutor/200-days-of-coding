# Day 29: Logistic Growth Simulation

This project simulates population growth using the logistic growth model in MATLAB. Two implementations are provided: one with a for loop and another with a while loop.

---

## Overview

- **Growth Model:** Logistic growth with parameters:
  - r: Growth rate
  - K: Carrying capacity
  - P0: Initial population
  - t_final: Total simulation time
  - dt: Time step

- **Implementations:**
  - **For Loop:** Iterates for a fixed number of steps.
  - **While Loop:** Iterates until the simulation time exceeds t_final.

- **Visualization:** Results from both simulations are plotted on the same graph for comparison.

---

## Simulation Details

The code performs the following steps:

1. **Parameter Initialization:** Sets the growth rate, carrying capacity, initial population, and simulation time.
2. **For Loop Simulation:** Computes population evolution over a fixed number of time steps.
3. **While Loop Simulation:** Computes population evolution while tracking simulation time dynamically.
4. **Graphing:** Plots the populations from both simulation methods with appropriate labels and legends.

---

## Usage

1. Open the `main.m` file in MATLAB.
2. Run the script to:
   - Perform both simulation methods.
   - Visualize the logistic growth model.
3. Analyze the graph to compare the simulation approaches.

---

## Key Takeaways

- Demonstrates two approaches (for and while loops) for simulating numerical models.
- Visual comparison helps validate consistency between different iterative methods.
- Provides a simple example of modeling real-world population dynamics using MATLAB.
