# 3D Ideal Gas Visualizer

A high-performance, real-time 3D simulation of an ideal gas container built using **Python** and **VPython**. This project models physical gas dynamics, elastic boundary collisions, and particle movement within a bounded 3D Cartesian coordinate system.

---

## Features

* **3D Cartesian Coordinate System**: Visualized using clean, scaled reference axes (X: Red, Y: Green, Z: Blue).
* **Bounded Container**: A semi-transparent 3D wireframe box (`vp.box`) representing the physical volume constraints.
* **Particle Dynamics**: Simulates a swarm of orange gas spheres (`vp.sphere`) initialized with randomized positions and velocities.
* **Elastic Wall Collisions**: Fully implemented physics reflection logic ensuring particles bounce cleanly off container boundaries without escaping or getting stuck.
* **Smooth Performance**: Runs at a steady frame rate optimized via VPython's real-time rendering loop.
  ##OUTPUT:

https://github.com/user-attachments/assets/bce1a2fc-7a12-494d-956e-8012b2254489



---

## Requirements

To run this simulation, you need Python installed along with the following libraries:

* `vpython`
* `numpy`

You can install them via pip:
```bash
pip install vpython numpy
python Ideal Ga.py

