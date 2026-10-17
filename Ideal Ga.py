import vpython as vp
import numpy as np

# --- 1. Setup Scene & Axes ---
scene = vp.canvas(title="3D Ideal Gas Visualizer", width=1200, height=800, background=vp.color.black)

L = 4.0  # Container half-length
axis_length = 10
thin_width = 0.03

# Reference Axes
vp.arrow(pos=vp.vector(0, 0, 0), axis=vp.vector(axis_length, 0, 0), color=vp.color.red, shaftwidth=thin_width)
vp.arrow(pos=vp.vector(0, 0, 0), axis=vp.vector(0, axis_length, 0), color=vp.color.green, shaftwidth=thin_width)
vp.arrow(pos=vp.vector(0, 0, 0), axis=vp.vector(0, 0, axis_length), color=vp.color.blue, shaftwidth=thin_width)

# Container Box
container = vp.box(pos=vp.vector(0, 0, 0), size=vp.vector(2*L, 2*L, 2*L), color=vp.color.cyan, opacity=0.15)

# --- 2. Initialize Gas Particles ---
N_particles = 200
particles = []
radius = 0.15

for i in range(N_particles):
    # Random initial positions safely inside the box
    x = np.random.uniform(-L + radius, L - radius)
    y = np.random.uniform(-L + radius, L - radius)
    z = np.random.uniform(-L + radius, L - radius)
    
    # Random initial velocity components
    v_mag = np.random.uniform(2.0, 5.0)
    theta = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, np.pi)
    
    vx = v_mag * np.sin(phi) * np.cos(theta)
    vy = v_mag * np.sin(phi) * np.sin(theta)
    vz = v_mag * np.cos(phi)
    
    p = vp.sphere(pos=vp.vector(x, y, z), radius=radius, color=vp.color.orange)
    p.v = vp.vector(vx, vy, vz)
    particles.append(p)

# --- 3. Simulation Loop ---
dt = 0.02

while True:
    vp.rate(100)
    
    for p in particles:
        # Update position
        p.pos = p.pos + p.v * dt
        
        # Wall collision checks and elastic bounces
        if p.pos.x > (L - radius):
            p.v.x = -p.v.x
            p.pos.x = L - radius
        elif p.pos.x < -(L - radius):
            p.v.x = -p.v.x
            p.pos.x = -(L - radius)
            
        if p.pos.y > (L - radius):
            p.v.y = -p.v.y
            p.pos.y = L - radius
        elif p.pos.y < -(L - radius):
            p.v.y = -p.v.y
            p.pos.y = -(L - radius)
            
        if p.pos.z > (L - radius):
            p.v.z = -p.v.z
            p.pos.z = L - radius
        elif p.pos.z < -(L - radius):
            p.v.z = -p.v.z
            p.pos.z = -(L - radius)