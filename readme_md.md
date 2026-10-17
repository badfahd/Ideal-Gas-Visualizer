# 3D Ideal Gas Visualizer

A high-performance, real-time 3D simulation of an ideal gas container built using **Python**, **VPython**, and **NumPy**. This project models macroscopic thermodynamic behavior by visualizing microscopic particle dynamics, elastic wall collisions, and spatial coordinate mapping inside a bounded 3D volume.

---

## Features

- **Interactive 3D Environment**: Built on a custom Cartesian coordinate system ($X$-axis in red, $Y$-axis in green, $Z$-axis in blue) for clear spatial orientation.
- **Semi-Transparent Container**: A bounded cubic volume (`vp.box`) featuring an optimized cyan opacity (`0.15`) that allows clear visibility of internal particle motion from any camera angle.
- **Dynamic Particle Swarm**: Simulates hundreds of independent spherical gas molecules (`vp.sphere`) with randomized initial positions and velocity vectors.
- **Elastic Wall Collisions**: Fully implemented vector reflection physics ensuring momentum is conserved when particles strike container boundaries without leaking outside the mesh.
- **High-Performance Rendering**: Utilizes `vpython` canvas rendering locked at a smooth simulation refresh rate (`100 Hz`).

---

## Prerequisites

Make sure you have Python installed on your system. You will need two external libraries: **VPython** for 3D rendering and **NumPy** for vector and random math operations.

Install them via terminal or command prompt:
```bash
pip install vpython numpy
```

---

## Installation & Running the Simulation

1. Clone or download this repository to your local machine.
2. Create a Python script file (e.g., `gas_visualizer.py`) and paste the simulation code into it.
3. Run the script using your Python interpreter:
   ```bash
   python gas_visualizer.py
   ```
4. A browser window will automatically launch displaying your interactive 3D simulation canvas.

---

## Code Architecture

The core program is structured into three primary phases:

1. **Scene & Visual Setup**: Initializes the rendering viewport, background color, and custom-scaled coordinate indicator arrows along with the transparent bounding container.
2. **Particle Initialization**: Instantiates an array of $N$ particles with randomized spatial coordinates safely offset from container walls, alongside randomized directional components (using spherical coordinates).
3. **Simulation Loop**: Executes continuous position updates ($p = p + v \cdot dt$) and checks boundary conditions using conditional sign-reversals to handle elastic wall impacts.

---

## Future Improvements

- **Inter-particle Collisions**: Integrating elastic sphere-to-sphere momentum exchange mechanics to allow natural thermalization and energy redistribution.
- **Thermodynamic Controls**: Real-time sliders to alter container volume, particle count, or temperature dynamically.

---

## License

This project is open-source and available for educational and personal exploration.