📐 Geometry – NACA 0012 Airfoil Project
Overview
This folder contains the geometry files for the NACA 0012 airfoil at different angles of attack (AoA).
The geometries were created using ANSYS DesignModeler and saved with snapshots for documentation.

Geometry Details
Airfoil: NACA 0012 (symmetric, 12% thickness-to-chord ratio).
Chord length (c): 100 mm (0.1 m).
Maximum thickness (t): 12 mm (0.12c), located at 30 mm from leading edge (0.3c).
Far-field boundaries: Extended to 10 × chord length (~1 m) in all directions.
Angles of Attack (AoA): 0°, 5°, 10° (geometry rotation method).
Files
NACA0012_AoA0.geo → Baseline geometry at 0° AoA.
NACA0012_AoA5.geo → Geometry rotated to 5° AoA.
NACA0012_AoA10.geo → Geometry rotated to 10° AoA.
Snapshots/ → Contains images of geometry setup for reference.
Notes
Geometry created in DesignModeler and exported for CFD workflow.
Rotation method chosen for AoA variation to ensure clarity in documentation.
These geometries will be used for meshing and simulation in subsequent steps.
