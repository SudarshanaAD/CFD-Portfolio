# CFD Cylinder Vortex Shedding (Re = 100)

## 📌 Project Overview
This project investigates vortex shedding behind a 2D cylinder at Reynolds number 100 using ANSYS Fluent.  
The goal is to capture the unsteady wake dynamics, validate Strouhal number predictions, and visualize flow oscillations.

---

## 🗂 Folder Structure
- **Case_files/** → ANSYS Workbench project files and solver setup  
- **Geometry&Mesh/** → Geometry definition and mesh screenshots  
- **Results/** → Post‑processing plots (lift, drag, pressure, velocity, frequency analysis)  
- **README.md** → Documentation of the project  

---

## ⚙️ Simulation Setup
- **Geometry**: 2D circular cylinder in channel flow  
- **Mesh**: Structured mesh with refinement in wake region  
- **Solver**: ANSYS Fluent, transient simulation  
- **Boundary Conditions**:  
  - Inlet: Uniform velocity  
  - Outlet: Pressure outlet  
  - Walls: No‑slip  

---

## 📊 Results
- **Lift & Drag Coefficients**: Time history showing periodic oscillations  
- **Frequency Analysis**: FFT of lift signal → Strouhal number ≈ 0.16–0.18  
- **Flow Visualizations**: Pressure and velocity contours, vortex shedding animation  

---

## 🐍 Python Validation
Planned Python scripts:
- Import lift/drag `.out` files  
- Perform FFT using `numpy` and `scipy`  
- Plot coefficient histories with `matplotlib`  
- Compare Strouhal number with benchmark literature  

---

## 🎞️ Animation Work
- Generate contour animations (pressure, velocity) using Fluent data exports  
- Convert image sequences to `.mp4` using Python (`matplotlib.animation` or `imageio`)  
- Embed animations in GitHub Pages for interactive portfolio presentation  

---

## ✅ Next Steps
- Finalize Python scripts for validation  
- Automate plot generation with GitHub Actions  
- Upload animations to `Results/` for visualization 
