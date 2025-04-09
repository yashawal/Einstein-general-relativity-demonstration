import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def main():
    print("Einstein's General Theory of Relativity Simulation")
    print("=" * 50)
    print("This simulation demonstrates three key aspects of General Relativity:")
    print("1. Spacetime curvature around massive objects")
    print("2. Gravitational lensing effect")
    print("3. Gravitational time dilation")
    
    choice = get_user_choice()
    
    if choice == 1:
        spacetime_curvature_simulation()
    elif choice == 2:
        gravitational_lensing_simulation()
    elif choice == 3:
        gravitational_time_dilation_simulation()
    else:
        print("Invalid choice. Please run the program again.")

def get_user_choice():
    print("\nChoose a simulation to run:")
    print("1. Spacetime curvature")
    print("2. Gravitational lensing")
    print("3. Gravitational time dilation")
    
    try:
        choice = int(input("\nEnter your choice (1-3): "))
        if 1 <= choice <= 3:
            return choice
        else:
            print("Please enter a number between 1 and 3.")
            return get_user_choice()
    except ValueError:
        print("Please enter a valid number.")
        return get_user_choice()

def spacetime_curvature_simulation():
    print("\nSimulating spacetime curvature around a massive object...")
    
    # Set up the figure with improved style
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create a grid of points for the spacetime fabric
    grid_size = 30
    x = np.linspace(-15, 15, grid_size)
    y = np.linspace(-15, 15, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Define the mass and G constant for the simulation
    mass = 100
    G = 1  # Simplified gravitational constant
    
    # Calculate the spacetime curvature using a simplified Schwarzschild metric
    R = np.sqrt(X**2 + Y**2)
    Z = -G * mass / (R + 1e-10)  # Add a small value to prevent division by zero
    
    # Normalize Z for better visualization
    Z = Z / np.abs(Z.min()) * 3
    
    # Create the 3D surface with enhanced colors
    surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                             linewidth=0, antialiased=True)
    
    # Add a central sphere representing the massive object
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    sphere_radius = 1.0
    sphere_x = sphere_radius * np.cos(u) * np.sin(v)
    sphere_y = sphere_radius * np.sin(u) * np.sin(v)
    sphere_z = Z.min() * 1.2 + sphere_radius * np.cos(v)
    ax.plot_surface(sphere_x, sphere_y, sphere_z, color="yellow", alpha=1)
    
    # Add a small particle orbiting the central mass
    orbit_frames = 100
    theta = np.linspace(0, 2*np.pi, orbit_frames)
    orbit_radius = 5
    orbit_x = orbit_radius * np.cos(theta)
    orbit_y = orbit_radius * np.sin(theta)
    
    # Fix the orbit_z calculation to handle index errors
    orbit_z = np.zeros(orbit_frames)
    for i in range(orbit_frames):
        # Find the nearest grid points
        x_idx = np.argmin(np.abs(x - orbit_x[i]))
        y_idx = np.argmin(np.abs(y - orbit_y[i]))
        # Get the z value at those points
        orbit_z[i] = Z[y_idx, x_idx]  # Note the order: Z[y_idx, x_idx]
    
    # Create the particle
    particle, = ax.plot([], [], [], 'ro', markersize=8)
    
    # Add title and labels with enhanced styling
    ax.set_title('Spacetime Curvature in General Relativity', fontsize=16, color='white')
    ax.set_xlabel('X', fontsize=12, labelpad=10)
    ax.set_ylabel('Y', fontsize=12, labelpad=10)
    ax.set_zlabel('Spacetime Curvature', fontsize=12, labelpad=10)
    
    # Remove axes for cleaner look
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    # Set perspective
    ax.view_init(elev=30, azim=30)
    
    # Animation function
    def update(frame):
        particle.set_data([orbit_x[frame]], [orbit_y[frame]])
        particle.set_3d_properties([orbit_z[frame]])
        ax.view_init(elev=30, azim=30 + frame/2)
        return particle,
    
    # Create animation
    ani = FuncAnimation(fig, update, frames=orbit_frames, 
                       interval=50, blit=True)
    
    plt.tight_layout()
    plt.show()
    
    # Return the animation object to prevent it from being garbage collected
    return ani

def gravitational_lensing_simulation():
    print("\nSimulating gravitational lensing effect...")
    
    # Set up the figure with improved style
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create a grid of points for light sources
    grid_size = 20
    n_points = grid_size * grid_size
    x = np.linspace(-10, 10, grid_size)
    y = np.linspace(-10, 10, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Flatten for ease of manipulation
    points_x = X.flatten()
    points_y = Y.flatten()
    
    # Define the massive object at the center
    mass_x, mass_y = 0, 0
    mass = 50  # Relative mass of the lensing object
    
    # Calculate the displacement due to gravitational lensing
    def calculate_lensing(x, y):
        dx = x - mass_x
        dy = y - mass_y
        r = np.sqrt(dx**2 + dy**2)
        # Avoid division by zero
        if r < 0.1:
            return x, y
        
        # Simplified lensing equation
        factor = mass / (r**2)
        # Direction of displacement (away from mass)
        displacement_x = factor * dx / r
        displacement_y = factor * dy / r
        
        return x + displacement_x, y + displacement_y
    
    # Apply lensing effect to all points
    lensed_points_x = np.zeros_like(points_x)
    lensed_points_y = np.zeros_like(points_y)
    
    for i in range(n_points):
        lensed_points_x[i], lensed_points_y[i] = calculate_lensing(points_x[i], points_y[i])
    
    # Plot original grid points
    ax.scatter(points_x, points_y, s=5, color='blue', alpha=0.3, label='Original Light Source')
    
    # Plot lensed grid points
    ax.scatter(lensed_points_x, lensed_points_y, s=8, color='cyan', label='Lensed Light')
    
    # Draw the massive object
    circle = plt.Circle((mass_x, mass_y), 1.5, color='yellow', alpha=0.8)
    ax.add_patch(circle)
    
    # Draw arrows showing displacement for a sample of points
    sample_indices = np.random.choice(n_points, 50, replace=False)
    for i in sample_indices:
        ax.arrow(points_x[i], points_y[i], 
                lensed_points_x[i] - points_x[i], 
                lensed_points_y[i] - points_y[i], 
                head_width=0.2, head_length=0.3, fc='white', ec='white', alpha=0.5)
    
    # Add title and labels with enhanced styling
    ax.set_title('Gravitational Lensing Effect', fontsize=16, color='white')
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.legend(loc='upper right')
    
    # Equal aspect ratio for better visualization
    ax.set_aspect('equal')
    ax.grid(False)
    
    plt.tight_layout()
    plt.show()

def gravitational_time_dilation_simulation():
    print("\nSimulating gravitational time dilation...")
    
    # Set up the figure with improved style
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Physical constants (in simplified units)
    G = 1  # Gravitational constant
    c = 1  # Speed of light
    M = 10  # Mass of the object
    
    # Define Schwarzschild radius
    r_s = 2 * G * M / c**2
    
    # Define distances from center
    distances = np.linspace(r_s*1.01, r_s*10, 1000)
    
    # Calculate time dilation factor using Schwarzschild metric
    # t' = t * sqrt(1 - r_s/r)
    time_dilation = np.sqrt(1 - r_s / distances)
    
    # Calculate radial distances for visualization
    earth_distance = r_s * 5
    satellite_distance = r_s * 2
    
    # Reference time
    reference_time = 24  # hours
    
    # Create a colorful plot
    ax.plot(distances / r_s, time_dilation, linewidth=3, color='cyan')
    ax.fill_between(distances / r_s, 0, time_dilation, alpha=0.3, color='cyan')
    
    # Plot the Earth's position
    earth_dilation = np.sqrt(1 - r_s / earth_distance)
    ax.scatter(earth_distance / r_s, earth_dilation, s=120, marker='o', 
              color='blue', edgecolor='white', zorder=5, label=f'Earth (Time: {reference_time * earth_dilation:.2f} hrs)')
    
    # Plot the Satellite's position
    satellite_dilation = np.sqrt(1 - r_s / satellite_distance)
    ax.scatter(satellite_distance / r_s, satellite_dilation, s=80, marker='d', 
              color='red', edgecolor='white', zorder=5, label=f'Satellite (Time: {reference_time * satellite_dilation:.2f} hrs)')
    
    # Add vertical lines for reference
    ax.axvline(x=earth_distance / r_s, linestyle='--', color='blue', alpha=0.5)
    ax.axvline(x=satellite_distance / r_s, linestyle='--', color='red', alpha=0.5)
    
    # Add horizontal lines to show time difference
    ax.axhline(y=earth_dilation, linestyle=':', color='blue', alpha=0.5)
    ax.axhline(y=satellite_dilation, linestyle=':', color='red', alpha=0.5)
    
    # Black hole representation
    ax.axvspan(1, 1.5, alpha=0.8, color='yellow')
    ax.text(1.25, 0.2, 'Massive\nObject', ha='center', fontsize=12, color='black', fontweight='bold')
    
    # Add event horizon
    ax.axvline(x=1, linestyle='-', color='red', linewidth=2, label='Event Horizon')
    
    # Add title and labels with enhanced styling
    ax.set_title('Gravitational Time Dilation', fontsize=16, color='white')
    ax.set_xlabel('Distance (in Schwarzschild radii)', fontsize=12)
    ax.set_ylabel('Time Dilation Factor (t\'/t)', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # Add informative text
    ax.text(0.98, 0.02, 
           f"Reference time: {reference_time} hrs\n"
           f"Time difference: {reference_time * (earth_dilation - satellite_dilation):.2f} hrs",
           transform=ax.transAxes, fontsize=12, va='bottom', ha='right',
           bbox=dict(boxstyle='round', facecolor='black', alpha=0.8, edgecolor='white'))
    
    # Add explanation
    explanation = (
        "Einstein's General Relativity predicts that time runs slower\n"
        "in stronger gravitational fields. This effect is crucial for\n"
        "GPS satellites, which must account for time dilation to\n"
        "maintain accuracy."
    )
    ax.text(0.02, 0.98, explanation, transform=ax.transAxes, fontsize=10,
           va='top', ha='left', bbox=dict(boxstyle='round', facecolor='black', alpha=0.8, edgecolor='white'))
    
    ax.legend(loc='lower right')
    ax.set_ylim(0, 1.05)
    ax.set_xlim(1, 10)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()