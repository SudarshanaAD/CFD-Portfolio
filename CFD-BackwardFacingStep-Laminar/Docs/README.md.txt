# CFD – Backward-Facing Step (Laminar Flow)

## Overview
This project simulates laminar flow over a backward-facing step using ANSYS Fluent (Student Edition).  
The case demonstrates flow separation, recirculation, and wall shear stress analysis.

## Geometry
- Channel height: 1.0 m
- Step height: 0.2 m
- Upstream length: 1.0 m
- Downstream length: 3.0 m

## Fluid Properties
- Fluid: Water
- Density: 1000 kg/m³
- Viscosity: 0.001 Pa·s
- Reynolds number: 100 (based on step height)

## Boundary Conditions
- Inlet: Velocity inlet (U = 0.0037 m/s)
- Outlet: Pressure outlet (0 Pa gauge)
- Walls: No-slip

## Solver Settings
- Pressure-based, steady-state
- Laminar model
- SIMPLE scheme
- Residuals converged to ~1e-6

## Results
- Flow separation captured at the step
- Recirculation bubble extends downstream
- Wall shear stress remains negative → reattachment point outside domain

## Limitations
- Outlet too close to capture reattachment
- Mesh refinement near wall can be improved

## Next Steps
- Extend downstream length (≥15–20 × step height)
- Perform grid independence study
- Compare reattachment length with literature values
