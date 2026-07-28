# 1D Steady-State Heat Conduction Solver

## 📌 Overview
This project implements a simple **1D steady-state heat conduction solver** using iterative relaxation.  
It demonstrates numerical discretization, iterative convergence, and comparison with the analytical solution.

## ⚙️ Method
- Domain length: L = 1.0  
- Grid points: N = 11  
- Boundary conditions: T(0) = 0, T(L) = 1  
- Iterative update scheme:
  

\[
  T_i^{new} = \frac{T_{i-1} + T_{i+1}}{2}
  \]


- Convergence tolerance: ε = 1e-8

## 📊 Results
- Numerical solution converges to a linear profile.  
- Analytical solution: T(x) = x/L.  
- Plot shows excellent agreement between numerical and analytical results.

## 🛠 Skills Demonstrated
- Python (NumPy, Matplotlib)  
- Numerical methods (finite difference, iterative relaxation)  
- Error analysis and convergence criteria  
- Visualization of scientific results  

## ▶️ How to Run
```bash
python heat_conduction_1D.py
