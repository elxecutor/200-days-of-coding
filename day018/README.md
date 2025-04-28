# Day 18: Advanced Object-Oriented Programming & Simulation

In this project, the design centers around the power of classes and subclasses to organize and extend functionalities for data visualization and simulation.

## Object-Oriented Design

### Base Classes & Subclasses
- **Base Class Approach:**  
  The foundational logic and attributes for various operations are encapsulated in base classes. This promotes code reuse and simplifies maintenance.

- **Specialized Subclasses:**  
  Subclasses extend the functionality of base classes to target specific tasks. This project demonstrates subclassing where common behaviors are inherited and customized for different applications.

## Mortgage Analysis

- **Loan Base Class & Mortgage Subclass:**  
  - A generic `Loan` class encapsulates fundamental loan parameters and computations.  
  - The `Mortgage` subclass extends `Loan` to include mortgage-specific calculations such as monthly payments, outstanding balances, and cumulative cost tracking.
  
- **Visualization Integration:**  
  Plotting functions utilize the state maintained within these classes to generate comparative financial charts.

## COVID-19 Simulation

- **Simulation Base Class & COVIDSimulation Subclass:**  
  - A `BaseSimulation` class lays out common simulation mechanics.  
  - The `COVIDSimulation` subclass customizes these mechanics by incorporating epidemiological parameters (population, contact rates, and contagious periods) to model infection spread.
  
- **Dynamic Plotting:**  
  The simulation’s evolving state is visualized through dedicated plotting functions that update infection curves in real-time.
